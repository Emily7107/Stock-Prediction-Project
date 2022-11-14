import numpy as np
import csv
import pandas as pd
import os
import matplotlib.pyplot as plt
from plotly.graph_objs import Scatter,Layout
from plotly.offline import plot
from Program_function import Function

filename=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/0000.csv'
df=pd.read_csv(filename,encoding='big5')
closeprice=df[['Close']]
date=df[['Date']]
highprice=df[['High']]
lowprice=df[['Low']]
# openprice=df[['Open']]
# label=df[['Label']]

closeprice=np.array(closeprice).astype('float32')
lowprice=np.array(lowprice).astype('float32')
highprice=np.array(highprice).astype('float32')
# openprice=np.array(openprice).astype('float32')
# label=np.array(label).astype('int')
date=np.array(date).astype('str')

# Function.test_Profit_2(closeprice,openprice,label,date,0)

sequence_length=20
times=3
standard=0

saveDate=[]
saveData=[]
label=[]

for i in range(len(closeprice)-sequence_length+1):
    a=np.std(closeprice[i:i+sequence_length], axis=0)
    avg=sum(closeprice[i:i+sequence_length])/20
    close=closeprice[i+sequence_length-1]
    high=highprice[i+sequence_length-1]
    low=lowprice[i+sequence_length-1]
    saveDate.append(date[i+sequence_length-1])
    
    if a>=standard:  
        if high>=avg+2.7*a>=low or close>=avg+2.7*a:
                label.append(0)
        elif avg+2.7*a>close>=avg+(2)*a:
                label.append(1)
        elif avg+(2)*a>close>=avg+a:
                label.append(2)
        elif avg+a>close>=avg:
                label.append(3)
        elif avg>close>=avg-(1)*a:
                label.append(4)
        elif avg-(1)*a>close>=avg-(2)*a:
                label.append(5)
        elif avg-(2)*a>close>=avg-(times)*a and low>avg-(times)*a:
                label.append(6) 
        elif high>=avg-(times)*a>=low or close<=avg-(times)*a:
                label.append(7)
    else:
        label.append(8)
        
#     temp=[float(avg),float(avg+times*a),float(avg-times*a),float(close),float(a)]
#     saveData.append(temp)

Function.countdata(label,2)

saveDate=np.reshape(saveDate,(len(saveDate)))
# column=['20MA','Up line','Down line','Close','Std']
column=['Label']
label=pd.DataFrame(label,index=saveDate,columns=column)
print(label)
# saveData=pd.DataFrame(saveData,index=saveDate,columns=column)

save_path=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/stock_data/0000/0000_newLabel.csv'
# save_path=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/0000_ball.csv'

label.to_csv(save_path, index=True, header=True)
# saveData.to_csv(save_path, index=True, header=True)