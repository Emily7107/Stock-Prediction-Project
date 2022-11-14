from functools import total_ordering
from matplotlib.pyplot import close
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, label_binarize
from My_Model import MyModel
from keras.layers import *
import os
import csv

#usecols=['Date','Open','High','Low','Close','real_Label','stock_label']
usecols=['Date','Open','High','Low','Close','stock_label']
filename=f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/stock_data/OTC/OTC_2011.csv"
data=pd.read_csv(filename,encoding='big5')
#data.columns=['Date','Open','High','Low','Close','real_Label','stock_label']
data.columns=['Date','Open','High','Low','Close','Label','stock_label']
print(data)

data_close=data[['Close']]
data_close=np.array(data_close).astype('float64')
#print(data_close)
data_label=data[['stock_label']]
data_label=pd.DataFrame(data_label)
data_label=data_label.fillna(0)
data_label=np.array(data_label).astype('float64')
data_Data=data[['Date']]
data_Data=np.array(data_Data).astype('str')
data_Open=data[['Open']]
data_Open=np.array(data_Open).astype('float64')
data_High=data[['High']]
data_High=np.array(data_High).astype('float64')
data_Low=data[['Low']]
data_Low=np.array(data_Low).astype('float64')
#data_real_label=data[['real_Label']]
#data_real_label=np.array(data_real_label).astype('int64')
#print(data_label)


def label(label_data):
    stock=label_data
    if 0<stock<2 or stock==0:
        #print("label=6")
        label=6
        return label
    if 2<stock<4:
        #print("label=7")
        label=7
        return label
    if 4<stock<6:
        #print("label=8")
        label=8
        return label
    if 6<stock<8:
        #print("label=9")
        label=9
        return label
    if 8<stock<10:
        #print("label=10")
        label=10
        return label
    if stock>10:
        #print("label=11")
        label=11
        return label
    if -2<stock<0:
        #print("label=5")
        label=5
        return label
    if -4<stock<-2:
        #print("label=4")
        label=4
        return label
    if -6<stock<-4:
        #print("label=3")
        label=3
        return label
    if -8<stock<-6:
        #print("label=2")
        label=2
        return label
    if -10<stock<-8:
        #print("label=1")
        label=1
        return label
    if  stock<-10:
        #print("label=0")
        label=0
        return label

#print(data_label[1:,0])
#print(data_close[1:,0])
data_a=[]
j=0
for i in range(len(data_close)):
    L=[]
    if (data_label[i])!=0:
        P=data_label[i]    
    if P!=0:
     PR=((P/data_close[i])-1)*100
     L=label(PR)
     #save=[data_Data[i],data_Open[i],data_High[i],data_Low[i],data_close[i],L]
     #data_a.append(save)
     data_a.append([L])
     #print(data_a)
#data_a=np.array(data_a).reshape(j,1)
#data_b=pd.DataFrame(data_a)
#print(data_b)
filepath=f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/stock_data/OTC/OTC_test_label.csv"
outputfile=open(filepath,'a',newline='',encoding='big5')
#title=['Date','Open','High','Low','Close','Label'] 
title=['Label']
outputwriter=csv.writer(outputfile)
outputwriter.writerow(title)
outputfile=open(filepath,'a',newline='',encoding='big5')
for i in (data_a):
      outputwriter.writerow(i)

outputfile.close()


class_0=0
class_1=0
class_2=0
class_3=0
class_4=0
class_5=0
class_6=0
class_7=0
class_8=0
class_9=0
class_10=0
class_11=0

data_a=np.array(data_a).astype('int32')
        
for i in data_a:
    
    i=int(i)

    if i==0:
     class_0=class_0+1
    elif i==1:
        class_1=class_1+1
    elif i==2:
        class_2=class_2+1
    elif i==3:
        class_3=class_3+1
    elif i==4:
        class_4=class_4+1
    elif i==5:
        class_5=class_5+1
    elif i==6:
        class_6=class_6+1
    elif i==7:
        class_7=class_7+1
    elif i==8:
        class_8=class_8+1
    elif i==9:
         class_9=class_9+1
    elif i==10:
        class_10=class_10+1
    elif i==11:
        class_11=class_11+1
total_label=class_1+class_2+class_3+class_4+class_5+class_6+class_7+class_8+class_9+class_10+class_11+class_0
print('Label')
print('class1:',class_0)
print('class2:',class_1)
print('class3:',class_2)
print('class4:',class_3)
print('class5:',class_4)
print('class6:',class_5)
print('class7:',class_6)
print('class8:',class_7)
print('class9:',class_8)
print('class10:',class_9)
print('class11:',class_11)
print('total label:',total_label)
