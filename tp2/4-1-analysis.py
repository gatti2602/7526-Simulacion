import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mp

out_1 = pd.read_csv('1-out.txt', sep=' ')
out_4 = pd.read_csv('4-out.txt', sep=' ')

#out_1.loc[out_1['time'] < 5000].boxplot(by='alternative',column='time').set_title('')
mp.figure()
sns.boxplot(data=out_1.loc[out_1['time'] < 5000], x='alternative', y='time').set_title('Distribucion de tiempo de instruccion')
mp.savefig("1-box.png")

mp.figure()
sns.violinplot(data=out_1.loc[out_1['time'] < 5000], x='alternative', y='time').set_title('Distribucion de tiempo de instruccion')
mp.savefig("1-violin.png")

mp.figure()
sns.boxplot(data=out_4.loc[out_4['time'] < 5000], x='alternative', y='time').set_title('Distribucion de tiempo de instruccion')
mp.savefig("4-box.png")

mp.figure()
sns.violinplot(data=out_4.loc[out_4['time'] < 5000], x='alternative', y='time').set_title('Distribucion de tiempo de instruccion')
mp.savefig("4-violin.png")