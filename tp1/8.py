import scipy.stats as st

observed = [40113, 29828, 11973, 10103, 7983]
expected = [40000, 30000, 12000, 10000, 8000]
salida = st.chisquare(observed, expected)
print "salida", salida