import pandas as pd
import pandas_datareader.data as web
import datetime
import csv
import os
import matplotlib.pyplot as plt
import time
import plotly 
from plotly.graph_objs import Scatter,Layout
from plotly.offline import plot

"""start = datetime.datetime(2016, 9, 1)
end = datetime.datetime(2016, 9, 2)
df_2330 = web.DataReader(f'2330.TW', 'yahoo', start, end)
c=df_2330
c.plot()"""
def get_df_by_pandas(stock_id, start_time, end_time):
    # 台灣股市的話要用 股票代號 加上 .TW
    if stock_id[0]=='Stock':
        df = web.DataReader(f'{stock_id[1]}.TW', 'yahoo', start_time, end_time)
    elif stock_id[0]=='OTC':
        df = web.DataReader(f'{stock_id[1]}.TWO', 'yahoo', start_time, end_time)
    return df

Stocks = [
        ['OTC','0001']
        #['OTC' or 'Stock', stockNumber, year]
]

# 台積電集團
Stocks += [
    #['Stock', '2330'],
    #['Stock', '3443']
]
# 台塑集團
"""Stocks += [
    ['Stock', '1301'],
    ['Stock', '1303'],
    ['Stock', '1326'],
    ['Stock', '1434'],
    ['Stock', '2408'],
    ['Stock', '6505'],
    ['Stock', '8046'],
    ['Stock', '3532']
]"""
# 鴻海集團
"""Stocks += [
    ['Stock', '2317'],
    #['Stock', '2328'],
    #['Stock', '2354'],
    #['Stock', '2392'],
    #['Stock', '3062'],
    #['Stock', '3481']
]
"""# 台積電關係股
"""Stocks += [
    ['Stock', '6196'],
    ['Stock', '2404'],
    ['Stock', '3413']
]"""

if __name__ == "__main__":
    not_finish = True
    Stocks_list = []
    Stocks_list = Stocks
    while(not_finish):
        not_finish = False
        notFinished_list = []
        for stock_id in Stocks_list:
            try:
                # result = create_df(stock[2], stock[1], stock[0])
                start_time = datetime.datetime(2010, 1, 1)
                end_time = datetime.datetime(2021, 12, 31)
                result = get_df_by_pandas(stock_id, start_time, end_time)
                save_path = f'C:/Users/Emily Wu/Desktop/庭妤的資料/專題/stock/{stock_id[0]}-{stock_id[1]}.csv'
                print('='*20)
                print(f'save data to {save_path}')
                print('='*20)
                result.to_csv(save_path, index=True, header=True)
            except Exception:
                not_finish = True
                print('='*20)
                print(f'{stock_id[0]}-{stock_id[1]} has error')
                print('='*20)
                notFinished_list.append(stock_id)
        print('\n')
        print('='*80)
        print(f'not Finish list:')
        for i in notFinished_list:
            print(i)
        print('='*80)
        Stocks_list = notFinished_list
