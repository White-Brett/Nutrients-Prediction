import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
t_1= pd.read_excel("C:/Users/BrettData/Desktop/capst/fertilzer-use.xlsx", sheet_name=0, header=3, names=None, index_col=None, keep_default_na=False)
t1=t_1.iloc[7:59,1:5]
t1.plot()
plt.show()
t1.plot(kind='area')
plt.show()
t_2= pd.read_excel("C:/Users/BrettData/Desktop/capst/fertilizer-use.xlsx", sheet_name=1, header=3, names=None, index_col=None, keep_default_na=False)
t2=t_2.iloc[7:59,1:5]
t2.plot()
plt.show()
t2.plot(kind='area')
plt.show()
t_3=pd.read_excel("C:/Users/BrettData/Desktop/capst/fertiliser-use.xlsx", sheet_name=2, header=2, names=None, idex_col=None, keep_default_na=False)
tt3=t_3.iloc[7:59,1:9]
t3=tt3.drop(columns='Unnamed: 3')
t3.plot()
plt.show()
t3.plot(kind='area')
plt.show()
t_4=pd.read_excel("C:/Users/BrettData/Desktop/capst/fertiliser-use.xlsx", sheet_name=3, header=2, names=None, idex_col=None, keep_default_na=False)
tt4=t_4.iloc[7:35,1:9]
t4=tt4.drop(columns='Unnamed: 5')
t4.plot()
plt.show()
t4.plot(kind='area')
plt.show()