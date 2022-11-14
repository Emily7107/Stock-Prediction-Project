import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from plotly.graph_objs import Scatter,Layout
from plotly.offline import plot
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import os
import keras
from keras.layers import *
plt.rcParams["font.sans-serif"]="mingliu"
plt.rcParams["axes.unicode_minus"]=False
from keras import callbacks
from My_Model import MyModel
from Method import LabelMethod
from Program_function import Function

gpus = tf.config.list_physical_devices('GPU')
if gpus:
  try:
    # Currently, memory growth needs to be the same across GPUs
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)

#def train_model(train_x,train_y,test_x,test_y,model_name,stock_name):
def train_model(train_x,train_y,model_name,stock_name):
    #try:
        save_model=f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/result/{stock_name}/{model_name}/model/{model_name}_relu_1114_0009.h5"
        callbacks_list =[callbacks.EarlyStopping(monitor='val_accuracy', patience=150, restore_best_weights=True),
                          callbacks.ModelCheckpoint(filepath=save_model, monitor='val_accuracy', mode='max', save_best_only=True)]
        history=model.fit(train_x,train_y,batch_size=200,epochs=1000,validation_split=0.2,callbacks=callbacks_list)
        #history=model.fit(train_x,train_y,batch_size=300,epochs=1000,validation_split=0.1)
        
        #scores=model.evaluate(test_x,test_y,batch_size=300)
        #print('\n準確率=',scores[1])
        
        m=history.history['accuracy']
        val_m=history.history['val_accuracy']
        loss=history.history['loss']
        val_loss=history.history['val_loss']
        epochs=range(len(loss))
        
        """m=history.history['mse']
        val_m=history.history['val_mse']
        loss=history.history['loss']
        val_loss=history.history['val_loss']
        epochs=range(len(loss))"""

        plt.plot(epochs,m,'b',label='Training accuracy')
        plt.plot(epochs,val_m,'r',label='validation accuracy')
        plt.title('Training and Validation Accuracy')
        plt.legend(loc='upper left')
        save_path=f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/result/{stock_name}/{model_name}/mse/{stock_name}_train_accuracy_relu_1114_0009.png"
        plt.savefig(save_path)
        
        # plt.plot(epochs,m,'b',label='Training MSE')
        # plt.plot(epochs,val_m,'r',label='validation MSE')
        # plt.title('Training and Validation Accuracy')
        # plt.legend(loc='upper left')
        # save_path=f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/result/{stock_name}/{model_name}/mse/{stock_name}_train_mse_tanh_0710.png"
        # plt.savefig(save_path)
        
        plt.figure()
        plt.plot(epochs,loss,'b',label='Training loss')
        plt.plot(epochs,val_loss,'r',label='validation loss')
        plt.title('Training and Validation Loss')
        plt.legend(loc='upper left')
        save_path=f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/result/{stock_name}/{model_name}/loss/{stock_name}_train_loss_relu_1114_0009.png"
        plt.savefig(save_path)
        #predict=model.predict(test_x)
        #predict=np.argmax(predict,axis=1)
        #predict=np.reshape(predict,(predict.size, ))
        
        # save_model=f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/result/{stock_name}/{model_name}/model/{model_name}_relu_1031.h5"
        model.save(save_model)
        #print(predict)
    #except KeyboardInterrupt:
       
        #print(predict)
        #print(test_y)
    #return predict

#主程式
Stock=[
      #  '2330',
       '0000',
       #'2317'
      ]

model_name=[
            #"LSTM",
            #"CNN_LSTM",
            #"CNN_stacked_LSTM",
            "CNN_LSTM_CI",
            #"CNN_BiLSTM_CI",
            #"CNN",
            #"BiLSTM",
            # "Attention"
           ]

pd.options.mode.chained_assignment=None
#filename=f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/stock_data/{Stock[0]}.csv"
#filename='testProfit.csv'
#filename='testProfit_lessdata.csv'

"""df=pd.read_csv(filename,encoding='big5')
ddtrain=df[['開盤價','收盤價','最高價','最低價']]
closeprice=df[['收盤價']]
openprice=df[['開盤價']]
label=df[['買賣點']]
date=df[['日期']]
        
ddtrain=np.array(ddtrain).astype('float64')
closeprice=np.array(closeprice).astype('float64')
openprice=np.array(openprice).astype('float64')
label=np.array(label).astype('int')
date=np.array(date).astype('str')

scaler=MinMaxScaler()#建立處理特徵的MinmaxScaler物件
scalert=MinMaxScaler()#建立處理標籤的MinmaxScaler物件
scalery=MinMaxScaler()

ddtrain=scaler.fit_transform(ddtrain)"""

#train_x,train_y,test_x,test_y,test_date,test_open,test_close=Function.ReceiveData()
#train_x,train_y,test_x,test_y,test_date,test_open,test_close=LabelMethod.mid_cycle(ddtrain,closeprice,openprice,label,date)
train_x,train_y=Function.ReceiveData()

#train_x=scaler.fit_transform(train_x)
#test_x=scalert.fit_transform(test_x)

Function.countdata(train_y,1)
#Function.countdata(test_y)

#MSE 時打開
#train_y=scalert.fit_transform(train_y)
#test_y=scalery.fit_transform(test_y)

#cross entropy時打開
train_y_onehot=tf.keras.utils.to_categorical(train_y)
#test_y_onehot=tf.keras.utils.to_categorical(test_y)

# model=MyModel.LSTM()
# model=MyModel.CNN_LSTM()
# model=MyModel.CNN_stacked_LSTM()
# model=MyModel.CNN_LSTM_CI()
# model=MyModel.CNN()
model=MyModel.CNN_LSTM_CI_tanh_lesslayer()
# model=MyModel.CNN_BiLSTM_CI()
# model=MyModel.CNN_LSTM_CI_tanh_lessCell()
# model=MyModel.LSTM_less()
# model=MyModel.LSTM_tanh_less()
# model=MyModel.BiLSTM()
# model=MyModel.seq2seq()

model.summary()
model.compile(loss=tf.keras.losses.categorical_crossentropy,optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),metrics=['accuracy'])
#model.compile(optimizer='adam',loss='mse',metrics=['mse'])

#predict_y=train_model(train_x,train_y,test_x,test_y,model_name[0],Stock[0])
#predict_y=train_model(train_x,train_y_onehot,test_x,test_y_onehot,model_name[0],Stock[0])
train_model(train_x,train_y_onehot,model_name[0],Stock[0])

#MSE 時打開
#predict_y=scalert.inverse_transform([[i] for i in predict_y])
#test_y=scalery.inverse_transform(test_y)

#predict_y=np.array(predict_y).astype('int')
#test_y=np.array(test_y).astype('int')

#Function.test_Profit(test_close,test_open,predict_y,test_date,1)
#Function.test_Profit(test_close,test_open,test_y,test_date,0)

#Function.countdata(predict_y)

#建立DataFrame,加入predict_y,test_y，準備以plotly繪圖
"""dd2=pd.DataFrame({"predict":list(predict_y),"label":list(test_y)})
dd2["predict"]=np.array(dd2["predict"]).astype('float64')
dd2["label"]=np.array(dd2["label"]).astype('int')

data=[Scatter(y=dd2["predict"],name='預測',line=dict(color="blue",dash="dot")),
      Scatter(y=dd2["label"],name='真實',line=dict(color="red",dash="dot"))
      ]
plot({"data":data,"layout":Layout(title="Predicted by "+model_name[0])},auto_open=False,filename='predict_testX_{model_name[0]}_tanh_0620_1_old.html')"""

