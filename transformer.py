import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import pandas as pd
from Program_function import Function
import os
import matplotlib.pyplot as plt

class TransformerBlock(layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1):
        super(TransformerBlock, self).__init__()
        self.att = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)
        self.ffn = keras.Sequential(
            [layers.Dense(ff_dim, activation="relu"), layers.Dense(embed_dim),]
        )
        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = layers.Dropout(rate)
        self.dropout2 = layers.Dropout(rate)

    def call(self, inputs, training):
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        return self.layernorm2(out1 + ffn_output)
    
class TokenAndPositionEmbedding(layers.Layer):
    def __init__(self, maxlen, vocab_size, embed_dim):
        super(TokenAndPositionEmbedding, self).__init__()
        self.token_emb = layers.Embedding(input_dim=vocab_size, output_dim=embed_dim)
        self.pos_emb = layers.Embedding(input_dim=maxlen, output_dim=embed_dim)

    def call(self, x):
        maxlen = tf.shape(x)[-1]
        positions = tf.range(start=0, limit=maxlen, delta=1)
        positions = self.pos_emb(positions)
        x = self.token_emb(x)
        return x + positions

#Main()
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
            '2010',
            '2011',
            '2012',
            '2013',
            '2014',
            '2015',
            '2016',
            '2017',
            '2018',
            '2019',
            '2020',
            # '2021'
            ]
stock_name=[
            # '2330',
            # '2317',
            # '2303',
            # '0050',
            '0000',
            # '3443'
            ]

model_name=[
            #"LSTM",
            #"CNN_LSTM",
            #"CNN_stacked_LSTM",
            #"CNN_LSTM_CI",
            #"CNN_BiLSTM_CI",
            #"CNN",
            #"BiLSTM",
            "Transformer"
           ]
#若沒有要去掉的年份，delete=25
delete=25
length=20

filename=[]

for j in range(len(stock_name)):
    for i in range(len(Stock_year)):
        filename.append(f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/stock_data/{stock_name[j]}/{stock_name[j]}_{Stock_year[i]}.csv")

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
            trainX=ddtrain[i]
            trainY=label[i]
        else:
            trainX=np.concatenate((trainX,ddtrain[i]))
            trainY=np.concatenate((trainY,label[i]))
trainX=np.array(trainX)
trainY=np.array(trainY)
trainY=trainY.reshape(len(trainY))
# trainY_onehot=tf.keras.utils.to_categorical(trainY)

# Training Model
embed_dim = 32  # Embedding size for each token
num_heads = 2  # Number of attention heads
ff_dim = 32  # Hidden layer size in feed forward network inside transformer

vocab_size = 100  # Only consider the top 20k words
maxlen = 20  # Only consider the first 200 words of each movie review

inputs = layers.Input(shape=(4,))
embedding_layer = TokenAndPositionEmbedding(maxlen, vocab_size, embed_dim)
x = embedding_layer(inputs)
transformer_block = TransformerBlock(embed_dim, num_heads, ff_dim)
x = transformer_block(x)
x = layers.GlobalAveragePooling1D()(x)
x = layers.Dropout(0.1)(x)
x = layers.Dense(20, activation="relu")(x)
x = layers.Dropout(0.1)(x)
outputs = layers.Dense(8, activation="softmax")(x)

model = keras.Model(inputs=inputs, outputs=outputs)

model.summary()

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
history = model.fit(trainX, trainY, batch_size=200, epochs=100, validation_split=0.2)

m=history.history['accuracy']
val_m=history.history['val_accuracy']
loss=history.history['loss']
val_loss=history.history['val_loss']
epochs=range(len(loss))

plt.plot(epochs,m,'b',label='Training accuracy')
plt.plot(epochs,val_m,'r',label='validation accuracy')
plt.title('Training and Validation Accuracy')
plt.legend(loc='upper left')
save_path=f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/result/{stock_name[0]}/{model_name[0]}/mse/{stock_name[0]}_train_accuracy_relu_1114_t1.png"
plt.savefig(save_path)

plt.figure()
plt.plot(epochs,loss,'b',label='Training loss')
plt.plot(epochs,val_loss,'r',label='validation loss')
plt.title('Training and Validation Loss')
plt.legend(loc='upper left')
save_path=f"C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/result/{stock_name[0]}/{model_name[0]}/loss/{stock_name[0]}_train_loss_relu_1114_t1.png"
plt.savefig(save_path)