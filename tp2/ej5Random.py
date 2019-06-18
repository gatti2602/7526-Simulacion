
import numpy
import simpy


class Checkout(object):
    def __init__(self, env, count):
        self.env = env
        self.count = count
        self.cashiers = [simpy.Resource(env) for x in range(count)]
        self.nextCashier = 0

    def serve(self, client):
        cashier = self.select_cashier()
        with cashier.request() as req:
            yield req
            yield self.env.timeout(client.get_pay_duration())

    def select_cashier(self):
        current = numpy.random.randint(0,6)

        return self.cashiers[current]

class Client(object):

    def __init__(self, env):
        self.env = env
        self.type = numpy.random.choice(['A', 'B', 'C'], p=[0.6, 0.25, 0.15])

    def pay(self, checkout):
        yield self.env.process(checkout.serve(self))
        print("%.2f Client type %s attended" % (self.env.now, self.type))

    def get_pay_duration(self):
        if (self.type == 'A'):
            return numpy.random.uniform(65, 85)
        if (self.type == 'B'):
            return numpy.random.uniform(45, 75)
        else:
            return numpy.random.uniform(70, 110)


cashier_count = 6
arrival_rate = 0.045
client_count = 100

def generate_clients(environment, count, interval, checkout):
    for i in range(count):
        client = Client(env)
        environment.process(client.pay(checkout))
        t = numpy.random.exponential(interval)
        yield environment.timeout(t)


env = simpy.Environment()
checkout = Checkout(env, cashier_count)
env.process(generate_clients(env, client_count, arrival_rate, checkout))
env.run()
