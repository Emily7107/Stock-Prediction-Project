import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from My_Model import MyModel
from keras.layers import *
import os
import csv
from Method import LabelMethod
from sklearn.preprocessing import MinMaxScaler

class Function():
    
    def ReceiveData():
        Stock_year=[
            # '1998',
            # '1999',
            '2000',
            '2001',
            '2002',
            '2003',
            '2004',
            '2005',
            '2006',
            '2007',
            '2008',
            '2009',
            # '2010',
            # '2011',
            # '2012',
            # '2013',
            # '2014',
            # '2015',
            # '2016',
            # '2017',
            # '2018',
            # '2019',
            # '2020',
            # '2021'
            ]
        Stock_name=[
                    # '2330',
                    # '2317',
                    # '2303',
                    # '0050',
                    '0000',
                    # '3443'
                    ]
        #若沒有要去掉的年份，delete=25
        delete=25
        length=20

        filename=[]

        for j in range(len(Stock_name)):
            for i in range(len(Stock_year)):
                filename.append(f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/stock_data/{Stock_name[j]}/{Stock_name[j]}_{Stock_year[i]}.csv")

        df=[]
        for i in range(len(filename)):
            if os.path.isfile(filename[i]):
                df.append(pd.read_csv(filename[i],encoding='big5'))

        ddtrain=[]
        label=[]
        for i in range(len(df)):
            temp=[]
            temp.append(Function.EnterData(df[i],1))
            ddtrain.append(temp[0][0])
            label.append(temp[0][1])

        trainX=[]
        trainY=[]
        for i in range(len(ddtrain)):
            temp=[]
            if i!=delete:
                if i==0:
                    dataX=ddtrain[i]
                    dataY=label[i]
                else:
                    dataX=np.concatenate((ddtrain[i-1][-length:],ddtrain[i]))
                    dataY=np.concatenate((label[i-1][-length:],label[i]))
                temp.append(LabelMethod.cycle(dataX,dataY,length))
                trainX.append(temp[0][0])
                trainY.append(temp[0][1])

        for i in range(len(trainX)):
            if i==0:
                train_x=trainX[i]
                train_y=trainY[i]
            else:
                train_x=np.concatenate((train_x,trainX[i]))
                train_y=np.concatenate((train_y,trainY[i]))  

        return train_x,train_y


    
    def EnterData(df,type):
        
        #ddtrain=df[['Open','Close','High','Low','Volume']]
        ddtrain=df[['Open','Close','High','Low']]
        closeprice=df[['Close']]
        openprice=df[['Open']]
        label=df[['New_label']]
        date=df[['Date']]
        avg10=df[['10MA']]
        a1=df[['1a line']]
        a27=df[['2.7a line']]
        
        ddtrain=np.array(ddtrain).astype('float64')
        closeprice=np.array(closeprice).astype('float64')
        openprice=np.array(openprice).astype('float64')
        label=np.array(label).astype('int')
        date=np.array(date).astype('str')
        avg10=np.array(avg10).astype('float32')
        a1=np.array(a1).astype('float32')
        a27=np.array(a27).astype('float32')
        
        scaler=MinMaxScaler()
        ddtrain=scaler.fit_transform(ddtrain)
        
        if type==1:
            return ddtrain,label
        else:
            return ddtrain,closeprice,openprice,label,date,avg10,a1,a27
    
    def Split_Data(data_all,close_all,open_all,datap_all,date_all,avg10_all,a1_all,a27_all,sequence_length,split=0.8):
        
        data=[]
        datap=[]
        date_y=[]
        open_y=[]
        close_y=[]
        avg10_y=[]
        a1_y=[]
        a27_y=[]
        for i in range(len(data_all)-sequence_length):
            data.append(data_all[i:i+sequence_length])#第1~20天當特徵
            datap.append(datap_all[i+sequence_length])#第6天為標籤
            date_y.append(date_all[i+sequence_length])
            open_y.append(open_all[i+sequence_length])
            close_y.append(close_all[i+sequence_length])
            avg10_y.append(avg10_all[i+sequence_length])
            a1_y.append(a1_all[i+sequence_length])
            a27_y.append(a27_all[i+sequence_length])
            

        x=np.array(data).astype('float64')
        y=np.array(datap).astype('int')
        date_y=np.array(date_y).astype('str')
        open_y=np.array(open_y).astype('float64')
        close_y=np.array(close_y).astype('float64')
        avg10_y=np.array(avg10_y).astype('float64')
        a1_y=np.array(a1_y).astype('float64')
        a27_y=np.array(a27_y).astype('float64')
        
        # split_boundary=int(x.shape[0]*split)
        # train_x=x[:split_boundary]#80%為訓練
        # test_x=x[split_boundary:]#20%為測試

        # #train_y=y[:split_boundary]
        # test_y=y[split_boundary:]
        
        # date=date_y[split_boundary:]
        # open=open_y[split_boundary:]
        # close=close_y[split_boundary:]
        
        return x,y,date_y,open_y,close_y,avg10_y,a1_y,a27_y
    
    def countdata(train_y,type):
        class_0=0
        class_1=0
        class_2=0
        class_3=0
        class_4=0
        class_5=0
        class_6=0
        class_7=0

        for i in train_y:
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
           
        total=class_0+class_1+class_2+class_3+class_4+class_5+class_6+class_7
        if(type==1):
            print("Train Label")
        elif type==2:
            print("Actual Label")
        else:
            print("Predict Label")
        print("class_0: ",class_0)         
        print("class_1: ",class_1) 
        print("class_2: ",class_2) 
        print("class_3: ",class_3) 
        print("class_4: ",class_4) 
        print("class_5: ",class_5) 
        print("class_6: ",class_6) 
        print("class_7: ",class_7) 
        # print("class_8: ",class_8) 
        # print("class_9: ",class_9) 
        # print("class_10: ",class_10) 
        # print("class_11: ",class_11) 
        print("total: ",total)
        
    def test_Profit(closeprice,openprice,label,date,avg10,a1,a27,type,compare1):

        CurrentMoney=1000000
        Stocknumber=0
        data=[]
        tempMoney=CurrentMoney
                
        initial=int(Stocknumber*closeprice[0]+CurrentMoney)
        if type==1:
            print("Initial Profit:",int(Stocknumber*closeprice[0]+CurrentMoney))


        for i in range(len(label)-1):
            testLabel=int(label[i])
            testClosePrice=float(closeprice[i])
            testOpenPrice=float(openprice[i+1])
            testavg10=float(avg10[i])
            # testavg20=float(avg20[i])
            # testavg60=float(avg60[i])
            testa1=float(a1[i])
            testa27=float(a27[i])
            
            if i==0:
                compare=compare1
            else:
                compare=closeprice[i-1]
            
            if Stocknumber==0:
                # tempStocknumber=Stocknumber
                keep=[]
                
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
                if label[i-1]<=3:
                    if Stocknumber!=0 and 4 not in keep and testClosePrice<openprice[i] and testClosePrice>testOpenPrice:
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

            elif testLabel==1:

                if testClosePrice<openprice[i] and testClosePrice<compare:
                    if 1 not in keep and Stocknumber!=0:
                        sellshares=int(Stocknumber*0.4)
                        CurrentMoney=CurrentMoney+testOpenPrice*sellshares
                        Stocknumber=Stocknumber-sellshares
                        keep.append(testLabel)
                        save=[date[i],testLabel,testClosePrice,testOpenPrice,CurrentMoney,Stocknumber]
                        data.append(save)
                        tempMoney=CurrentMoney
                            
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
                Stocknumber=Stocknumber
                CurrentMoney=CurrentMoney

        if type==1:
            filepath='profit_predict.csv'
        else:
            filepath='0000_2017_profit.csv'
                
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
    
    def CompareLabel(predict,real):
        SellToBuy=0
        BuyToSell=0
        HoldToSell=0
        HoldToBuy=0
        SellToHold=0
        BuyToHold=0
        Correct=0
        NoInfluence=0
        result=[]
        
        for i in range(len(predict)):
            if real[i]<=3 and predict[i]>=9:
                SellToBuy=SellToBuy+1
                result.append('sell to buy')
            elif real[i]>=9 and predict[i]<=3:
                BuyToSell=BuyToSell+1
                result.append('buy to sell')
            elif 4<=real[i]<=8 and predict[i]<=3:
                HoldToSell=HoldToSell+1
                result.append('hold to sell')
            elif 4<=real[i]<=8 and predict[i]>=9:
                HoldToBuy=HoldToBuy+1
                result.append('hold to buy')
            elif real[i]<=3 and 4<=predict[i]<=8:
                SellToHold=SellToHold+1
                result.append('sell to hold')
            elif real[i]>=9 and 4<=predict[i]<=8:
                BuyToHold=BuyToHold+1
                result.append('buy to hold')
            elif real[i]==predict[i]:
                Correct=Correct+1
                result.append('correct')
            else:
                NoInfluence=NoInfluence+1
                result.append('no influence')
            
        print("Sell to Buy: ",SellToBuy)
        print("Buy to Sell: ",BuyToSell)
        print("Hold to Sell: ",HoldToSell)
        print("Hold to Buy: ",HoldToBuy)
        print("Sell to Hold: ",SellToHold)
        print("Buy to Hold: ",BuyToHold)
        print("Correct: ",Correct)
        print("No influence: ",NoInfluence)
            
        return result