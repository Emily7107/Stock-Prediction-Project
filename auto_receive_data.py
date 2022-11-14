import csv
import pandas as pd
import twstock
import os
import matplotlib.pyplot as plt
import time
import plotly 
from plotly.graph_objs import Scatter,Layout
from plotly.offline import plot

plt.rcParams["font.sans-serif"]="mingliu"
plt.rcParams["axes.unicode_minus"]=False
year=2010
start=1
stockname='2303'
filepath='2303.csv'
times=0

while(times<13):
    err=0
    print('time= ',times)
    print('year= ',year)
    if not os.path.isfile(filepath):
        outputfile=open(filepath,'a',newline='',encoding='big5')
        outputwriter=csv.writer(outputfile)
        title=["Date","Volume","Open","High","Low","Close"]
        outputwriter.writerow(title)#寫入標題
    if os.path.isfile(filepath):
        outputfile=open(filepath,'a',newline='',encoding='big5')
        outputwriter=csv.writer(outputfile)
        while(start!=13):
            print('start= ',start)
            for i in range(start,start+2):
                print('i= ',i)
                stock=twstock.Stock(stockname)#以目標股票的股票代號建立Stock物件
                stocklist=stock.fetch(year,i)#year/i
        
                data=[]
                #data=["日期","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"]
                for stock in stocklist:
                    strdate=stock.date.strftime("%Y-%m-%d") #將datetime轉換為字串

                    li=[strdate,stock.capacity,stock.open,stock.high,stock.low,stock.close]
                    data.append(li)
                err=0
                if not data:
                    print("data has error!")
                    err=1
                    break
                for dataline in (data):
                    #print("writedata")
                    outputwriter.writerow(dataline)
                time.sleep(120)
            if start+2==13:
                break
            if err!=1:
                start=start+2
            print('error= ',err)
            time.sleep(900)
            
            
        outputfile.close()
    if err==0:
        year=year+1
        times=times+1
        start=1

print("finish!")
