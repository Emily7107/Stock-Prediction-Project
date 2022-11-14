import csv
import pandas as pd
import numpy as np
from Method import LabelMethod
from Program_function import Function

filename=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/0000_20102021.csv'
df=pd.read_csv(filename,encoding='big5')
closeprice=df[['Close']]
openprice=df[['Open']]
label=df[['Label']]
date=df[['Date']]
type=0

closeprice=np.array(closeprice).astype('float32')
openprice=np.array(openprice).astype('float32')
label=np.array(label).astype('int')
date=np.array(date).astype('str')

#Function.test_Profit(closeprice,openprice,label,date,0)
#label=[7,7,6,6,5,5,4,4,3,3,2,2,3,3,4,4,3,3,2,2,1,1,0,0,7,7]
CurrentMoney=1000000
Stocknumber=0
basic=50000
data=[]
        
initial=int(Stocknumber*closeprice[0]+CurrentMoney)
if type==1:
    print("Initial Profit:",int(Stocknumber*closeprice[0]+CurrentMoney))


for i in range(len(label)-1):
    testLabel=int(label[i])
    testClosePrice=float(closeprice[i])
    testOpenPrice=float(openprice[i+1])
    
    if Stocknumber==0:
        tempStocknumber=Stocknumber
        keep=[]
        point=[]

    if testLabel==7:
        if Stocknumber==0:
            tempMoney=CurrentMoney
        if CurrentMoney>basic and 7 not in keep:
            buyshares=int(tempMoney*0.2/basic)
            CurrentMoney=CurrentMoney-basic*buyshares
            Stocknumber=Stocknumber+buyshares
            point.append(testOpenPrice)
            keep.append(testLabel)
            save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
    
    elif testLabel==5:
        if 7 not in keep:
            tempMoney=CurrentMoney
            
        if tempMoney*0.3>testOpenPrice and 5 not in keep:
            buyshares=int(tempMoney*0.3/testOpenPrice)
            CurrentMoney=CurrentMoney-testOpenPrice*buyshares
            Stocknumber=Stocknumber+buyshares
            keep.append(testLabel)
            save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
            
    elif testLabel==3:
        if [5,7] not in keep:
            tempMoney=CurrentMoney
            
        if CurrentMoney>testOpenPrice and 3 not in keep:
            buyshares=int(CurrentMoney/testOpenPrice)
            CurrentMoney=CurrentMoney-testOpenPrice*buyshares
            Stocknumber=Stocknumber+buyshares
            keep.append(testLabel)
            save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
    
    elif testLabel==2:
        if Stocknumber!=0 and 2 not in keep:
            tempStocknumber=Stocknumber
            sellshares=int(tempStocknumber*0.5)
            CurrentMoney=CurrentMoney+testOpenPrice*sellshares
            Stocknumber=Stocknumber-sellshares
            keep.append(testLabel)
            save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
            
    elif testLabel==1:
        if Stocknumber!=0 and 1 not in keep:
            sellshares=int(tempStocknumber*0.3)
            CurrentMoney=CurrentMoney+testOpenPrice*sellshares
            Stocknumber=Stocknumber-sellshares
            keep.append(testLabel)
            save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
            
    elif testLabel==0:
        if Stocknumber!=0 and 0 not in keep:
            sellshares=Stocknumber
            CurrentMoney=CurrentMoney+testOpenPrice*sellshares
            Stocknumber=0
            keep.append(testLabel)
            save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
            data.append(save)
            
    else:
        Stocknumber=Stocknumber
        CurrentMoney=CurrentMoney

if type==1:
    filepath='profit_predict.csv'
else:
    filepath='0000_newLabel_profit_2.csv'
        
# if not os.path.isfile(filepath):
#         outputfile=open(filepath,'a',newline='',encoding='big5')
#         outputwriter=csv.writer(outputfile)
#         title=["Date","Label","Close of The Day","Open of Next Day","Capital","Stock Number"]
#         outputwriter.writerow(title)#寫入標題

# if os.path.isfile(filepath):
#         outputfile=open(filepath,'a',newline='',encoding='big5')
#         outputwriter=csv.writer(outputfile)
#         for i in (data):
#             outputwriter.writerow(i)
# outputfile.close()
        
if type==1:
    print("=====Predict Profit=====")
else:
    print("======Real Profit=======")
            
total=int(CurrentMoney+closeprice[-1]*Stocknumber)
print('The number of stocks:',int(Stocknumber))
print('Current money:',int(CurrentMoney))
print('Total profit:',int(CurrentMoney+closeprice[-1]*Stocknumber))
print('Return on Investment:',(total-initial)/initial)