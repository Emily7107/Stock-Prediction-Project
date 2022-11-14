from matplotlib.axis import XAxis
import numpy as np
import pandas as pd
import chart_studio.plotly as py
import plotly.offline as pyoff
import plotly.graph_objs as go
from plotly.graph_objs import Layout,Scatter
from plotly.offline import plot

filename=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/stock_data/0000.csv'
df=pd.read_csv(filename,encoding='big5')
closeprice=df[['Close']]
openprice=df[['Open']]
date=df[['Date']]

closeprice=np.array(closeprice).astype('float32')
openprice=np.array(openprice).astype('float32')
date=np.array(date).astype('str')
sequence_length=20
times=3

data=(openprice+closeprice)/2

data=np.reshape(data,len(data)) 
date=np.reshape(date,len(date))      
column=['avg']
data=pd.DataFrame(data,index=date,columns=column)
print(data)

# for i in range(len(closeprice)-sequence_length+1):
#     a=np.std(closeprice[i:i+sequence_length], axis=0)
#     avg=sum(closeprice[i:i+sequence_length])/20
#     close=closeprice[i+sequence_length-1]
#     saveDate.append(date[i+sequence_length-1])
#     temp=[float(avg),float(avg+2.7*a),float(avg-times*a),float(close),float(avg+1*a),float(avg-1*a),float(avg+2*a),float(avg-2*a)]
#     saveData.append(temp)

# for i in range(len(closeprice)-10+1):
#     avg5=sum(closeprice[i:i+10])/10
#     saveDate2.append(date[i+9])
#     temp=[float(avg5)]
#     saveData2.append(temp)
    
# for i in range(len(closeprice)-60+1):
#     avg60=sum(closeprice[i:i+60])/60
#     saveDate3.append(date[i+59])
#     temp=[float(avg60)]
#     saveData3.append(temp)


# saveDate=np.reshape(saveDate,(len(saveDate)))
# saveDate2=np.reshape(saveDate2,(len(saveDate2)))
# saveDate3=np.reshape(saveDate3,(len(saveDate3)))
# column=['20MA','2.7a line','-3a line','Close','1a line','-1a line','2a line','-2a line']
# saveData=pd.DataFrame(saveData,index=saveDate,columns=column)
# # print(saveData)
# column2=['10MA']
# saveData2=pd.DataFrame(saveData2,index=saveDate2,columns=column2)

# column3=['60MA']
# saveData3=pd.DataFrame(saveData3,index=saveDate3,columns=column3)

# save_path=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/0050_boll.csv'

# saveData.to_csv(save_path, index=True, header=True)


# trace1=go.Ohlc(x=df['Date'],
#                 open=df['Open'],
#                 high=df['High'],
#                 low=df['Low'],
#                 close=df['Close'],
#                 increasing_line_color= 'red', decreasing_line_color= 'green',name='K line')

# trace2=go.Scatter(x=saveData.index,y=saveData['20MA'],name='20MA',line_color='#ffe476')
# trace3=go.Scatter(x=saveData.index,y=saveData['2.7a line'],name='2.7a line')  #32CD32
# trace4=go.Scatter(x=saveData.index,y=saveData['-3a line'],name='-3a line')
# #trace5=go.Scatter(x=saveData.index,y=saveData['Std'],name='Std')
# trace5=go.Scatter(x=saveData.index,y=saveData['1a line'],name='1a line')
# trace6=go.Scatter(x=saveData.index,y=saveData['-1a line'],name='-1a line')
# trace7=go.Scatter(x=saveData.index,y=saveData['2a line'],name='2a line')
# trace8=go.Scatter(x=saveData.index,y=saveData['-2a line'],name='-2a line')
# #trace9=go.Scatter(x=saveData.index,y=df['Label'],name='Label',mode='markers')
# trace10=go.Scatter(x=saveData2.index,y=saveData2['10MA'],name='10MA')
# trace11=go.Scatter(x=saveData3.index,y=saveData3['60MA'],name='60MA',line_color='#ffe476')


#trace2=go.Bar(x=df['日期'], y=df['成交股數'],name='成交股數',marker=dict(color ='blue'))

# data=[trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8,trace10,trace11]

#layout = go.Layout(
#    yaxis2=dict(anchor='x', overlaying='y', side='left'))#設置座標軸的格式，一般次座標軸在右側

trace1=go.Scatter(x=data.index,y=data['avg'],name='avg',line_color='#32CD32')
Data=[trace1]
fig = go.Figure(Data)


fig.update(layout_xaxis_rangeslider_visible=False)


fig.update_layout(
    title='0000',
    yaxis_title='Stock price',
)

plot({"data":fig,"layout":Layout(title='0000 ')},auto_open=False)

# save_path=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/20MA_0000.csv'
# saveData.to_csv(save_path, index=True, header=True)
# save_path2=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/10MA_0000.csv'
# saveData2.to_csv(save_path2, index=True, header=True)
# save_path3=f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/60MA_0000.csv'
# saveData3.to_csv(save_path3, index=True, header=True)
