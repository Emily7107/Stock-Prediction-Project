import pandas as pd
import numpy as np
from plotly.graph_objs import Scatter,Layout
from sklearn.preprocessing import MinMaxScaler

class LabelMethod():

    def cycle(data_all,datap_all,sequence_length,split=0.8):
        
        data=[]
        datap=[]
        #date_y=[]
        #open_y=[]
        #close_y=[]
        for i in range(len(data_all)-sequence_length):
            data.append(data_all[i:i+sequence_length])#第1~20天當特徵
            datap.append(datap_all[i+sequence_length])#第6天為標籤
            #date_y.append(date_all[i+sequence_length])
            #open_y.append(open_all[i+sequence_length])
            #close_y.append(close_all[i+sequence_length])

        x=np.array(data).astype('float64')
        y=np.array(datap).astype('int')
        #date_y=np.array(date_y).astype('str')
        #open_y=np.array(open_y).astype('float64')
        #close_y=np.array(close_y).astype('float64')
 
        """split_boundary=int(x.shape[0]*split)
        train_x=x[:split_boundary]#80%為訓練
        test_x=x[split_boundary:]#20%為測試

        train_y=y[:split_boundary]
        test_y=y[split_boundary:]
        
        date=date_y[split_boundary:]
        open=open_y[split_boundary:]
        close=close_y[split_boundary:]"""
        
        #train_x,train_y,test_x,test_y,date,open,close=LabelMethod.SelectData(x,y,date_y,open_y,close_y,split)

        return x,y#,date_y,open_y,close_y
        #return train_x,train_y,test_x,test_y,date,open,close
    
    def SelectData(x,y,date_y,open_y,close_y,split):
        split_boundary=int(x.shape[0]*split)
        index_all=[]
        for i in range(len(x)):
            index_all.append(i)
        
        index=np.random.choice(len(x),split_boundary,False)
        index=np.sort(index)
        index_rest=np.setdiff1d(index_all,index)
        
        train_x=x[index]
        test_x=x[index_rest]
        
        train_y=y[index]
        test_y=y[index_rest]
        
        date=date_y[index_rest]
        closeprice=close_y[index_rest]
        openprice=open_y[index_rest]
        
        return train_x,train_y,test_x,test_y,date,openprice,closeprice