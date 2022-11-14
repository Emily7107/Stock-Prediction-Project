import csv
import pandas as pd
import numpy as np
from Method import LabelMethod
from Program_function import Function
import os

filename=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/0000_2022.csv'
df=pd.read_csv(filename,encoding='big5')
closeprice=df[['Close']]
openprice=df[['Open']]
label=df[['Label']]
date=df[['Date']]
avg20=df[['20MA']]
avg10=df[['10MA']]
a1=df[['1A']]
a27=df[['27A']]
avg60=df[['60MA']]
type=0

closeprice=np.array(closeprice).astype('float32')
openprice=np.array(openprice).astype('float32')
label=np.array(label).astype('int')
date=np.array(date).astype('str')
avg20=np.array(avg20).astype('float32')
avg10=np.array(avg10).astype('float32')
a1=np.array(a1).astype('float32')
a27=np.array(a27).astype('float32')
avg60=np.array(avg60).astype('float32')

#Function.test_Profit(closeprice,openprice,label,date,0)
#label=[7,5,7,7,7,7,7]
CurrentMoney=1000000
Stocknumber=0
data=[]
clear=True
tempMoney=CurrentMoney
        
initial=int(Stocknumber*closeprice[0]+CurrentMoney)
if type==1:
    print("Initial Profit:",int(Stocknumber*closeprice[0]+CurrentMoney))


for i in range(len(label)-1):
    testLabel=int(label[i])
    testClosePrice=float(closeprice[i])
    testOpenPrice=float(openprice[i+1])
    testavg10=float(avg10[i])
    testavg20=float(avg20[i])
    testavg60=float(avg60[i])
    testa1=float(a1[i])
    testa27=float(a27[i])
    
    if i==0:
        compare=9554.139648
    else:
        compare=closeprice[i-1]
    
    if Stocknumber==0:
        tempStocknumber=Stocknumber
        keep=[]
        
    
    # if 1 and 2 and 5 and 6 and 7 in keep:
    #     if testLabel==3:
    #         keep=[]
    
    # if testClosePrice<testavg60 and clear:
    #     if Stocknumber!=0:
    #             sellshares=Stocknumber
    #             CurrentMoney=CurrentMoney+testOpenPrice*sellshares
    #             Stocknumber=0
    #             keep.append(testLabel)
    #             save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
    #             data.append(save)
    #             tempMoney=CurrentMoney
    #     clear=False
    # else:
    # if testClosePrice*0.99>testOpenPrice:
    #     if Stocknumber!=0 and 0 not in keep:
    #             sellshares=Stocknumber
    #             CurrentMoney=CurrentMoney+testOpenPrice*sellshares
    #             Stocknumber=0
    #             keep.append(testLabel)
    #             save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
    #             data.append(save)
    #             tempMoney=CurrentMoney
    # else:   
    if testLabel==7:
        if Stocknumber==0:
            tempMoney=CurrentMoney
    
        if 7 in keep:
            if keep[len(keep)-1]==7:
                if testClosePrice<temp and CurrentMoney>tempMoney*0.1:
                    buyshares=int(tempMoney*0.1/testOpenPrice)
                    CurrentMoney=CurrentMoney-testOpenPrice*buyshares
                    Stocknumber=Stocknumber+buyshares
                    save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
                    data.append(save)
            
        if CurrentMoney>tempMoney*0.2 and 7 not in keep and testClosePrice>openprice[i]:
            buyshares=int(tempMoney*0.2/testOpenPrice)
            CurrentMoney=CurrentMoney-testOpenPrice*buyshares
            Stocknumber=Stocknumber+buyshares
            save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
        temp=testClosePrice
        keep.append(testLabel)

    elif testLabel==6:

        if 7 not in keep:
            tempMoney=CurrentMoney
        
        if CurrentMoney>tempMoney*0.3 and 6 not in keep and testClosePrice>openprice[i]:
            buyshares=int(tempMoney*0.3/testOpenPrice)
            CurrentMoney=CurrentMoney-testOpenPrice*buyshares
            Stocknumber=Stocknumber+buyshares
            keep.append(testLabel)
            save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
        
    elif testLabel==5:

        if 6 not in keep and 7 not in keep:
            tempMoney=CurrentMoney
        
        if CurrentMoney>tempMoney*0.5 and 5 not in keep and testClosePrice>openprice[i]:
            if 6 not in keep and 7 not in keep:
                buyshares=int(tempMoney*0.5/testOpenPrice)
            else:
                buyshares=int(CurrentMoney/testOpenPrice)
            CurrentMoney=CurrentMoney-testOpenPrice*buyshares
            Stocknumber=Stocknumber+buyshares
            keep.append(testLabel)
            save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
            
    elif testLabel==4:
        if label[i-1]==3:
            if Stocknumber!=0 and 4 not in keep and testOpenPrice<testClosePrice:
                sellshares=Stocknumber
                CurrentMoney=CurrentMoney+testOpenPrice*sellshares
                Stocknumber=0
                keep.append(testLabel)
                save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
                data.append(save)
                tempMoney=CurrentMoney

    elif testLabel==2:

        if testavg10>testa1 and testClosePrice<openprice[i] and testClosePrice<compare:
        
            if 2 not in keep and Stocknumber!=0:
                # tempStocknumber=Stocknumber
                sellshares=int(Stocknumber*0.5)
                CurrentMoney=CurrentMoney+testOpenPrice*sellshares
                Stocknumber=Stocknumber-sellshares
                keep.append(testLabel)
                save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
                data.append(save)
                tempMoney=CurrentMoney

    
        elif testavg10<testa1 and testOpenPrice<testa27:
            if CurrentMoney>tempMoney*0.2 and tempMoney*0.2>testOpenPrice:
                buyshares=int(tempMoney*0.2/testOpenPrice)
                CurrentMoney=CurrentMoney-testOpenPrice*buyshares
                Stocknumber=Stocknumber+buyshares
                save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
                data.append(save)
                # check=1

        
    elif testLabel==1:

        # if check!=1:
        if testClosePrice<openprice[i] and testClosePrice<compare:
            if 1 not in keep and Stocknumber!=0:
                # if 2 not in keep:
                    #tempStocknumber=Stocknumber
                sellshares=int(Stocknumber*0.4)
                CurrentMoney=CurrentMoney+testOpenPrice*sellshares
                Stocknumber=Stocknumber-sellshares
                keep.append(testLabel)
                save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
                data.append(save)
                tempMoney=CurrentMoney
        # else:
        #     if 1 not in keep and Stocknumber!=0:
        #         # if 2 not in keep:
        #         #     tempStocknumber=Stocknumber
        #         sellshares=int(Stocknumber*0.9)
        #         CurrentMoney=CurrentMoney+testOpenPrice*sellshares
        #         Stocknumber=Stocknumber-sellshares
        #         keep.append(testLabel)
        #         save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
        #         data.append(save)
        #         tempMoney=CurrentMoney
        #         check=0
            
        
    elif testLabel==0:

        if testClosePrice<openprice[i] and testClosePrice<compare:
            if Stocknumber!=0 and 0 not in keep:
                sellshares=Stocknumber
                CurrentMoney=CurrentMoney+testOpenPrice*sellshares
                Stocknumber=0
                keep.append(testLabel)
                save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
                data.append(save)
                tempMoney=CurrentMoney
            
    else:
        # if testClosePrice<testavg60:
        #     if Stocknumber!=0:
        #         sellshares=Stocknumber
        #         CurrentMoney=CurrentMoney+testOpenPrice*sellshares
        #         Stocknumber=0
        #         keep.append(testLabel)
        #         save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
        #         data.append(save)
        #         tempMoney=CurrentMoney
        # else:
        Stocknumber=Stocknumber
        CurrentMoney=CurrentMoney
        
        # if testClosePrice>testavg60:
        #     clear=True

if type==1:
    filepath='profit_predict.csv'
else:
    filepath='0000_newLabel_profit_0911_2022.csv'
        
if not os.path.isfile(filepath):
        outputfile=open(filepath,'a',newline='',encoding='big5')
        outputwriter=csv.writer(outputfile)
        title=["Date","Label","Close of The Day","Open of Next Day","Capital","Stock Number"]
        outputwriter.writerow(title)#寫入標題

if os.path.isfile(filepath):
        outputfile=open(filepath,'a',newline='',encoding='big5')
        outputwriter=csv.writer(outputfile)
        for i in (data):
            outputwriter.writerow(i)
outputfile.close()
        
if type==1:
    print("=====Predict Profit=====")
else:
    print("======Real Profit=======")
            
total=int(CurrentMoney+closeprice[-1]*Stocknumber)
print('The number of stocks:',int(Stocknumber))
print('Current money:',int(CurrentMoney))
print('Total profit:',int(CurrentMoney+closeprice[-1]*Stocknumber))
print('Return on Investment:',(total-initial)/initial)