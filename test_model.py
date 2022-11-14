import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly.graph_objs import Scatter,Layout
from plotly.offline import plot
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import os
import csv
from keras.layers import *
plt.rcParams["font.sans-serif"]="mingliu"
plt.rcParams["axes.unicode_minus"]=False
from My_Model import MyModel
from Method import LabelMethod
from Program_function import Function

Stock_year=[
            # '2000',
            # '2001',
            # '2002',
            # '2003',
            # '2004',
            # '2005',
            # '2006',
            # '2007',
            # '2008',
            # '2009',
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
            '2020',
            '2021',
            # '2022'
            ]
Stock=[
       #'2330',
       #'2317',
       #'2303',
       '0000'
      ]
model_name=[
            #"LSTM",
            #"CNN_LSTM",
            #"CNN_stacked_LSTM",
            "CNN_LSTM_CI"
            #"CNN"
           ]
compare={
        '2010':8207.849609,
        '2011':9025.299805,
        '2012':7053.379883,
        '2013':7779.220215,
        '2014':8612.540039,
        '2015':9274.110352,
        '2016':8114.259766,
        '2017':9272.879883,
        '2018':10710.73047,
        '2019':9554.139648,
        '2020':12100.48047,
        '2021':14902.03027  
}

save_path=f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/result/2330/{model_name[0]}/model/{model_name[0]}_relu_0815_t1.h5"
filename=[]

for i in range(len(Stock_year)):
    filename.append(f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/stock_data/{Stock[0]}/{Stock[0]}_{Stock_year[i]}.csv")


df=[]
for i in range(len(filename)):
    if os.path.isfile(filename[i]):
        df.append(pd.read_csv(filename[i],encoding='big5'))

ddtrainX=[]
closepriceY=[]
openpriceY=[]
labelY=[]
dateY=[]
avg10Y=[]
a1Y=[]
a27Y=[]
for i in range(len(df)):
    temp=[]
    temp.append(Function.EnterData(df[i],0))
    ddtrainX.append(temp[0][0])
    closepriceY.append(temp[0][1])
    openpriceY.append(temp[0][2])
    labelY.append(temp[0][3])
    dateY.append(temp[0][4])
    avg10Y.append(temp[0][5])  
    a1Y.append(temp[0][6])
    a27Y.append(temp[0][7])

# ddtrainX2=[]
# closepriceY2=[]
# openpriceY2=[]
# labelY2=[]
# dateY2=[]
# for i in range(len(dateY)):#x,y,date_y,open_y,close_y
#     temp=[]
#     temp.append(Function.Split_Data(ddtrainX[i],closepriceY[i],openpriceY[i],labelY[i],dateY[i],sequence_length=20))
#     ddtrainX2.append(temp[0][0])
#     labelY2.append(temp[0][1])
#     dateY2.append(temp[0][2])
#     openpriceY2.append(temp[0][3])
#     closepriceY2.append(temp[0][4])

for i in range(len(dateY)):
    if i==0:
        if len(dateY)==2:
            ddtrain=ddtrainX[i][-20:]
            closeprice=closepriceY[i][-20:]
            openprice=openpriceY[i][-20:]
            label=labelY[i][-20:]
            date=dateY[i][-20:]
            avg10=avg10Y[i][-20:]
            a1=a1Y[i][-20:]
            a27=a27Y[i][-20:]
        else:
            a1=a1Y[i]
            a27=a27Y[i]
            ddtrain=ddtrainX[i]
            closeprice=closepriceY[i]
            openprice=openpriceY[i]
            label=labelY[i]
            date=dateY[i]
            avg10=avg10Y[i]
            a1=a1Y[i]
            a27=a27Y[i]
    else:
        ddtrain=np.concatenate((ddtrain,ddtrainX[i]))
        closeprice=np.concatenate((closeprice,closepriceY[i]))
        openprice=np.concatenate((openprice,openpriceY[i]))
        label=np.concatenate((label,labelY[i]))
        date=np.concatenate((date,dateY[i]))
        avg10=np.concatenate((avg10,avg10Y[i]))
        a1=np.concatenate((a1,a1Y[i]))
        a27=np.concatenate((a27,a27Y[i]))
        
        
# for i in range(len(dateY2)):
#     if i==0:
#         test_x=ddtrainX2[i]
#         test_close=closepriceY2[i]
#         test_open=openpriceY2[i]
#         test_y=labelY2[i]
#         test_date=dateY2[i]
#     else:
#         test_x=np.concatenate((test_x,ddtrainX2[i]))
#         test_close=np.concatenate((test_close,closepriceY2[i]))
#         test_open=np.concatenate((test_open,openpriceY2[i]))
#         test_y=np.concatenate((test_y,labelY2[i]))
#         test_date=np.concatenate((test_date,dateY2[i]))

#scaler=MinMaxScaler()
#ddtrain=scaler.fit_transform(ddtrain)

test_x,test_y,test_date,test_open,test_close,test_avg10,test_a1,test_a27=Function.Split_Data(ddtrain,closeprice,openprice,label,date,avg10,a1,a27,sequence_length=20)

model=tf.keras.models.load_model(save_path)
model.summary()
predict=model.predict(test_x)
predict=np.argmax(predict,axis=1)
predict=np.reshape(predict,(predict.size, ))

Function.countdata(predict,0)
Function.countdata(test_y,2)

# result=Function.CompareLabel(predict,test_y)

Function.test_Profit(test_close,test_open,predict,test_date,test_avg10,test_a1,test_a27,1,compare[Stock_year[0]])
Function.test_Profit(test_close,test_open,test_y,test_date,test_avg10,test_a1,test_a27,0,compare[Stock_year[0]])

# data=[]
# for i in range(len(test_date)):
#     save=[test_date[i],int(test_y[i]),predict[i],float(test_open[i]),float(test_close[i]),result[i]]
#     data.append(save)
    
# filepath='check_label_0815_t7.csv'

# if not os.path.isfile(filepath):
#     outputfile=open(filepath,'a',newline='',encoding='big5')
#     outputwriter=csv.writer(outputfile)
#     title=["Date","Real Label","Predict Label","Open","Close","Jugement"]
#     outputwriter.writerow(title)#寫入標題

# if os.path.isfile(filepath):
#         outputfile=open(filepath,'a',newline='',encoding='big5')
#         outputwriter=csv.writer(outputfile)
#         for i in (data):
#             outputwriter.writerow(i)
# outputfile.close()

# dd2=pd.DataFrame({"predict":list(predict),"label":list(test_y)})
# dd2["predict"]=np.array(dd2["predict"]).astype('float64')
# dd2["label"]=np.array(dd2["label"]).astype('int')

# data=[Scatter(y=dd2["predict"],name='Predict',line=dict(color="blue",dash="dot")),
#       Scatter(y=dd2["label"],name='Real',line=dict(color="red",dash="dot"))
#       ]
# plot({"data":data,"layout":Layout(title="Predicted by "+model_name[0])},auto_open=False,filename='predict_testData_CNN_LSTM_CI_tanh_0704_add.html')