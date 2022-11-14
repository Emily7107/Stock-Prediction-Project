import csv
from tkinter import Label
import pandas as pd
import numpy as np
from Method import *
import os
import csv

#filepath=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/stock_data/2330.csv'
filepath=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/testProfit.csv'

pdstock=pd.read_csv(filepath,encoding='big5')
closeprice=pdstock[['收盤價']]
openprice=pdstock[['開盤價']]
label=pdstock[['買賣點']]
date=pdstock[['日期']]

closeprice=np.array(closeprice).astype('float32')
openprice=np.array(openprice).astype('float32')
label=np.array(label).astype('int')
date=np.array(date).astype('str')

CurrentMoney=1000000
Stocknumber=10
data=[]


for i in range(len(label)-1):
    testLabel=int(label[i])
    testClosePrice=float(closeprice[i])
    testOpenPrice=float(openprice[i+1])
    testDate=str(date[i])

    if testLabel<=3:
        if Stocknumber!=0:
            sellProfit=testOpenPrice*1000*Stocknumber
            CurrentMoney=CurrentMoney+sellProfit
            Stocknumber=0
            save=[testDate,testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
    elif testLabel==9:
        stockprice=testOpenPrice*1000
        if stockprice<=CurrentMoney*(1/3):
            number=int(CurrentMoney*(1/3)/stockprice)
            Stocknumber=Stocknumber+number
            CurrentMoney=CurrentMoney-number*stockprice
            save=[testDate,testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
    elif testLabel==10:
        stockprice=testOpenPrice*1000
        if stockprice<=CurrentMoney*(2/3):
            number=int(CurrentMoney*(2/3)/stockprice)
            Stocknumber=Stocknumber+number
            CurrentMoney=CurrentMoney-number*stockprice
            save=[testDate,testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
    elif testLabel==11:
        stockprice=testOpenPrice*1000
        if stockprice<=CurrentMoney:
            number=int(CurrentMoney/stockprice)
            Stocknumber=Stocknumber+number
            CurrentMoney=CurrentMoney-number*stockprice
            save=[testDate,testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
    else:
        Stocknumber=Stocknumber
        CurrentMoney=CurrentMoney

filepath='check1.csv'
if not os.path.isfile(filepath):
        outputfile=open(filepath,'a',newline='',encoding='big5')
        outputwriter=csv.writer(outputfile)
        title=["日期","標籤","當日收盤價","隔日開盤價","交易後資本","交易後股票數"]
        outputwriter.writerow(title)#寫入標題

if os.path.isfile(filepath):
        outputfile=open(filepath,'a',newline='',encoding='big5')
        outputwriter=csv.writer(outputfile)
        for i in (data):
            outputwriter.writerow(i)
outputfile.close()
            

print('The number of stocks:',Stocknumber)
print('Current money:',CurrentMoney)
print('Total profit:',CurrentMoney+closeprice[-1]*Stocknumber)