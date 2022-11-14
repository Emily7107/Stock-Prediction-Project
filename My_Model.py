import tensorflow as tf
import keras
from keras.models import Model
from keras.layers import *

class MyModel():
    
    def __init__(self,model):
        self.model=model
    
    def LSTM():
        model=tf.keras.models.Sequential()
        #TIME_STEPS=5 INPUT_SIZE=4
        model.add(Input(shape=(20,4)))
        model.add(LSTM(units=500,activation='relu',unroll=True,return_sequences=True))
        model.add(LSTM(units=500,activation='relu',unroll=True,return_sequences=True))
        model.add(LSTM(units=500,activation='relu',unroll=True,return_sequences=True))
        model.add(LSTM(units=500,activation='relu',unroll=True,return_sequences=False))
        model.add(Dropout(0.2))
        #model.add(Dense(units=1))
        model.add(Dense(units=12,activation='softmax'))
        
        return model
    
    def LSTM_tanh():
        model=tf.keras.models.Sequential()
        #TIME_STEPS=5 INPUT_SIZE=4
        model.add(LSTM(128,activation='tanh',return_sequences=True,input_shape=(5,4)))
        model.add(Dropout(0.3))
        model.add(LSTM(128,activation='tanh',return_sequences=True))
        model.add(Dropout(0.3))
        model.add(LSTM(128,activation='tanh',return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(128,activation='tanh',return_sequences=False))
        model.add(Dropout(0.2))
        model.add(Dense(1))
        
        return model
    
    def LSTM_less():
        model=tf.keras.models.Sequential()
        #TIME_STEPS=5 INPUT_SIZE=4
        model.add(Input(shape=(20,4)))
        model.add(LSTM(units=16,activation='relu',unroll=True,return_sequences=True))
        model.add(LSTM(units=16,activation='relu',unroll=True,return_sequences=True))
        model.add(LSTM(units=16,activation='relu',unroll=True,return_sequences=False))
        model.add(Dropout(0.2))
        #model.add(Dense(units=1))
        model.add(Dense(units=12,activation='softmax'))
        
        return model
    
    def LSTM_tanh_less():
        model=tf.keras.models.Sequential()
        #TIME_STEPS=5 INPUT_SIZE=4
        model.add(LSTM(12,activation='tanh',return_sequences=True,input_shape=(5,4)))
        model.add(Dropout(0.3))
        model.add(LSTM(12,activation='tanh',return_sequences=True))
        model.add(Dropout(0.3))
        model.add(LSTM(12,activation='tanh',return_sequences=False))
        model.add(Dropout(0.2))
        model.add(Dense(1))
        
        return model
    
    def CNN_LSTM():
        model=tf.keras.models.Sequential()
        model.add(Input(shape=(20,4)))
        model.add(Conv1D(filters=64, kernel_size=2, activation='relu', padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1)) 
        model.add(Conv1D(filters=64, kernel_size=2, activation='relu', padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Conv1D(filters=64, kernel_size=2, activation='relu', padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.5))
        model.add(LSTM(units=50))
        model.add(Dropout(0.2))

        model.add(Dense(units=50))
        model.add(Dense(units=50))
        model.add(Dense(units=50))
        model.add(Dense(units=12,activation='softmax'))
        #model.compile(loss="mse",optimizer="adam",metrics=['mse'])
        
        return model
    
    def CNN_stacked_LSTM():
        model=tf.keras.models.Sequential()
        #TIME_STEPS=5 INPUT_SIZE=4
        model.add(Input(shape=(5,4)))
        model.add(Conv1D(filters=64,kernel_size=2,activation='relu',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Conv1D(filters=64,kernel_size=2,activation='relu',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Conv1D(filters=64,kernel_size=2,activation='relu',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.5))
        model.add(LSTM(units=150,unroll=False,return_sequences=True))
        model.add(LSTM(units=150,unroll=False,return_sequences=False))
        model.add(Dropout(0.4))
        model.add(Dense(units=50))
        model.add(Dense(units=50))
        model.add(Dense(units=50))
        model.add(Dense(units=1))
        
        return model
    def CNN_LSTM_CI():
        x_inputs = Input(shape=(20,4))
        cnn1 = Conv1D(filters=128, kernel_size=2, activation='relu', padding='same')(x_inputs)
        cnn1 = MaxPooling1D(pool_size=2,padding='same')(cnn1)
        cnn1 = Dropout(0.2)(cnn1)
        cnn2 = Conv1D(filters=128, kernel_size=2, activation='relu', padding='same')(cnn1)
        cnn2 = Dropout(0.2)(cnn2)
        cnn3 = Conv1D(filters=128, kernel_size=2, activation='relu', padding='same')(cnn2)
        cnn3 = Dropout(0.2)(cnn3)
        LSTM_1 = LSTM(300, return_sequences=True)(cnn3)
        LSTM_2 = LSTM(300, return_sequences=False)(LSTM_1)
        LSTM_2 = Dropout(0.2)(LSTM_2)
        
        x_flatten = Flatten()(x_inputs)
        concatted = Concatenate()([x_flatten, LSTM_2])
        Dense_1 = Dense(int(50/2)*4)(concatted)
        y_outputs = Dense(12,activation='softmax')(Dense_1)
        #y_outputs = Dense(1)(Dense_1)
        model=Model(x_inputs,y_outputs)
        
        return model
    
    def CNN_LSTM_CI_tanh_lesslayer():
        x_inputs = Input(shape=(20,4))
        cnn1 = Conv1D(filters=64, kernel_size=10, activation='relu', padding='same')(x_inputs)#f:30 #k:8
        cnn1 = MaxPooling1D(pool_size=10,padding='same')(cnn1)
        cnn1 = Dropout(0.4)(cnn1)
        #cnn2 = Conv1D(filters=128, kernel_size=2, activation='tanh', padding='same')(cnn1)
        #cnn2 = Dropout(0.2)(cnn2)
        #cnn3 = Conv1D(filters=128, kernel_size=2, activation='tanh', padding='same')(cnn2)
        #cnn3 = Dropout(0.2)(cnn3)
        LSTM_1 = LSTM(50, return_sequences=False,activation='relu')(cnn1)
        #LSTM_2 = LSTM(300, return_sequences=False)(LSTM_1)
        #LSTM_1= Bidirectional(LSTM(units=60,activation='tanh',return_sequences=False))(cnn1)
        LSTM_1 = Dropout(0.4)(LSTM_1)
        
        x_flatten = Flatten()(x_inputs)
        concatted = Concatenate()([x_flatten, LSTM_1])
        Dense_1 = Dense(50)(concatted)
        y_outputs = Dense(8,activation='softmax')(Dense_1)
        #y_outputs = Dense(1)(Dense_1)
        model=Model(x_inputs,y_outputs)
        
        return model
    
    def DNN():
        model = tf.keras.models.Sequential()
        model.add(Input(shape=(5,4)))
        model.add(tf.keras.layers.Dense(units=16, activation='relu', input_dim=5))
        model.add(tf.keras.layers.Dense(units=32, activation='relu'))
        model.add(tf.keras.layers.Dense(units=64, activation='relu'))
        model.add(tf.keras.layers.Dense(units=128, activation='relu'))
        model.add(tf.keras.layers.Dense(units=3, activation='linear'))
        
        return model
    
    def CNN():
        model=tf.keras.models.Sequential()
        #TIME_STEPS=20 INPUT_SIZE=4
        times_steps=20
        #times_steps=5
        model.add(Input(shape=(times_steps,4)))
        model.add(Conv1D(filters=64,kernel_size=2,activation='relu',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Conv1D(filters=64,kernel_size=2,activation='relu',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Conv1D(filters=64,kernel_size=2,activation='relu',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Conv1D(filters=64,kernel_size=2,activation='relu',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Conv1D(filters=64,kernel_size=2,activation='relu',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Flatten())
        model.add(Dense(units=500,activation='relu'))
        model.add(Dense(units=12,activation='softmax'))
        
        return model
    
    def CNN_tanh():
        model=tf.keras.models.Sequential()
        #TIME_STEPS=20 INPUT_SIZE=4
        model.add(Input(shape=(20,4)))
        model.add(Conv1D(filters=64,kernel_size=2,activation='tanh',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Conv1D(filters=64,kernel_size=2,activation='tanh',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Conv1D(filters=64,kernel_size=2,activation='tanh',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Conv1D(filters=64,kernel_size=2,activation='tanh',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Conv1D(filters=64,kernel_size=2,activation='tanh',padding='same'))
        model.add(MaxPooling1D(pool_size=2,padding='same'))
        model.add(Dropout(0.1))
        model.add(Flatten())
        model.add(Dense(units=500,activation='tanh'))
        model.add(Dense(units=12,activation='softmax'))
        
        return model
    
    def BiLSTM():
        model=tf.keras.models.Sequential()
        model.add(Input(shape=(20,4)))
        model.add(Bidirectional(LSTM(units=20,activation='tanh',return_sequences=True)))
        model.add(Bidirectional(LSTM(units=20,activation='tanh',return_sequences=False)))
        model.add(Dropout(0.2))
        model.add(Dense(units=12,activation='softmax'))
        
        return model
    
    def CNN_BiLSTM_CI():
        x_inputs = Input(shape=(20,4))
        cnn1 = Conv1D(filters=64, kernel_size=2, activation='relu', padding='same')(x_inputs)#f:30 #k:8
        cnn1 = MaxPooling1D(pool_size=10,padding='same')(cnn1)
        cnn1 = Dropout(0.5)(cnn1)
        #cnn2 = Conv1D(filters=128, kernel_size=2, activation='tanh', padding='same')(cnn1)
        #cnn2 = Dropout(0.2)(cnn2)
        #cnn3 = Conv1D(filters=128, kernel_size=2, activation='tanh', padding='same')(cnn2)
        #cnn3 = Dropout(0.2)(cnn3)
        BiLSTM_1 = Bidirectional(LSTM(50, return_sequences=False,activation='relu'))(cnn1)
        #LSTM_2 = LSTM(300, return_sequences=False)(LSTM_1)
        #LSTM_1= Bidirectional(LSTM(units=60,activation='tanh',return_sequences=False))(cnn1)
        BiLSTM_1 = Dropout(0.4)(BiLSTM_1)
        
        x_flatten = Flatten()(x_inputs)
        concatted = Concatenate()([x_flatten, BiLSTM_1])
        Dense_1 = Dense(50)(concatted)
        y_outputs = Dense(8,activation='softmax')(Dense_1)
        #y_outputs = Dense(1)(Dense_1)
        model=Model(x_inputs,y_outputs)
        
        return model
    
    def seq2seq():
        features=20
        ch=4
        # inputs=Input((features,ch))
        x=Embedding(features, ch, input_length=features)
        att_in=LSTM(100,return_sequences=True,dropout=0.3,recurrent_dropout=0.2)(x)
        att_out=Attention()(att_in)
        outputs=Dense(8,activation='softmax',trainable=True)(att_out)
        model=Model(x,outputs)

        return model

