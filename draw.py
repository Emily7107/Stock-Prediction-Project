from cmath import nan
import csv
from tkinter import Label
import pandas as pd
from pymysql import NULL
import os
import matplotlib.pyplot as plt
import time
import plotly 
from plotly.graph_objs import Scatter,Layout
from plotly.offline import plot
import numpy as np
from Method import *

plt.rcParams["font.sans-serif"]="mingliu"
plt.rcParams["axes.unicode_minus"]=False

#filepath=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/stock_data/2330.csv'
filepath='3443_draw.csv'
pdstock=pd.read_csv(filepath,encoding='big5')
price=pdstock[['Close']]
#label=pdstock[['買賣點']]
#label=np.array(label).astype('int')
#sequence_length=20

price=np.array(price).astype('float32')

#datap=[]
"""for i in range(len(price)-sequence_length):
    #copydata.append(datap_all[i:i+sequence_length])
    average=sum(price[i:i+sequence_length])/21
    if price[i+sequence_length]/average>1.1:
        datap.append([11])
    elif price[i+sequence_length]/average>1.08 and price[i+sequence_length]/average<=1.1:
        datap.append([10])
    elif price[i+sequence_length]/average>1.06 and price[i+sequence_length]/average<=1.08:
        datap.append([9])
    elif price[i+sequence_length]/average>1.04 and price[i+sequence_length]/average<=1.06:
        datap.append([8])
    elif price[i+sequence_length]/average>1.02 and price[i+sequence_length]/average<=1.04:
        datap.append([7])
    elif price[i+sequence_length]/average>1 and price[i+sequence_length]/average<=1.02:
        datap.append([6])
    elif price[i+sequence_length]/average>0.98 and price[i+sequence_length]/average<=1:
        datap.append([5])
    elif price[i+sequence_length]/average>0.96 and price[i+sequence_length]/average<=0.98:
        datap.append([4])    
    elif price[i+sequence_length]/average>0.94 and price[i+sequence_length]/average<=0.96:
        datap.append([3])
    elif price[i+sequence_length]/average>0.92 and price[i+sequence_length]/average<=0.94:
        datap.append([2])
    elif price[i+sequence_length]/average>0.9 and price[i+sequence_length]/average<=0.92:
        datap.append([1])
    else:
        datap.append([0])"""

#datap=np.array(datap).astype('int')

#LabelMethod.countdata(label)

"""filepath2='purchase_point.csv'
if not os.path.isfile(filepath2):
    title=["買賣點"]
    outputfile=open(filepath2,'a',newline='',encoding='big5')
    outputwriter=csv.writer(outputfile)

    
    for dataline in (datap):
        outputwriter.writerow(dataline)  
        
    outputfile.close()"""



data=[#Scatter(x=pdstock['日期'],y=pdstock['買賣點'],name='買賣點'),
      Scatter(x=pdstock['Date'],y=pdstock['Close'],name='收盤價')
      ]
plot({"data":data,"layout":Layout(title='創意電子股價趨勢圖')},auto_open=False)