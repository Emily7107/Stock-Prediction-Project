from cmath import nan
import csv
import pandas as pd
from pymysql import NULL
import twstock
import os
import matplotlib.pyplot as plt
import time
import plotly 
from plotly.graph_objs import Scatter,Layout
from plotly.offline import plot

plt.rcParams["font.sans-serif"]="mingliu"
plt.rcParams["axes.unicode_minus"]=False

filepath=f'2330_feuruary.csv'

if not os.path.isfile(filepath):
    title=["日期","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"]
    outputfile=open(filepath,'a',newline='',encoding='big5')
    outputwriter=csv.writer(outputfile)

    for i in range(2,3):
        stock=twstock.Stock('2330')#以鴻海的股票代號建立Stock物件
        stocklist=stock.fetch(2016,i)#2018/i
        
        
        data=[]
        for stock in stocklist:
            strdate=stock.date.strftime("%Y-%m-%d") #將datetime轉換為字串

            li=[strdate,stock.capacity,stock.turnover,stock.open,stock.high,stock.low,stock.close,stock.change,stock.transaction]
            data.append(li)
        if not data:
            print("data error!")
        
        if i==1:#若是1月就寫入欄位名稱
            outputwriter.writerow(title)#寫入標題
        for dataline in (data):
            outputwriter.writerow(dataline)
        time.sleep(120)

        
    outputfile.close()

pdstock=pd.read_csv(filepath,encoding='big5')
data=[Scatter(x=pdstock['日期'],y=pdstock['開盤價'],name='開盤價'),
      Scatter(x=pdstock['日期'],y=pdstock['最低價'],name='最低價'),
      Scatter(x=pdstock['日期'],y=pdstock['最高價'],name='最高價'),
      Scatter(x=pdstock['日期'],y=pdstock['收盤價'],name='收盤價')]
plot({"data":data,"layout":Layout(title='台積電2330股價趨勢圖')},auto_open=False)
