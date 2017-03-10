# coding: utf-8

# In[1]:

import pandas as pd
from pandas_highcharts.display import display_charts
import os

class financeMain:
    pairList={}
    currencyList=[]
    
    def __init__(self):
        self.OpenAllFile(r'C:\\Users\\simnk\\workspace\\finance\\HISTDATA2015', 'H')
        
    #全ファイルを開いてデータを展開
    @classmethod
    def OpenAllFile(self,directory,tf):
        fileNames = os.listdir(directory)
        for fileName in fileNames:
            pair=fileName[10:16]
            histData = pd.read_csv(directory + r'\\' + fileName, sep=';',
                                   names=('Time','Open','High','Low','Close', ''),
                                   index_col='Time', parse_dates=True)
            histData.index += pd.offsets.Hour(7) #7時間のオフセット
            #描画に時間がかかるので１時間足に変換
            #0 +-1 に編集
            self.pairList[pair]=self.TranData(self.TF_ohlc(histData, 'H'))
            
    # dfのデータからtfで指定するタイムフレームの4本足データを作成する関数
    @classmethod
    def TF_ohlc(self, df, tf):
        x = df.resample(tf).ohlc()
        O = x['Open']['open']
        H = x['High']['high']
        L = x['Low']['low']
        C = x['Close']['close']
        ret = pd.DataFrame({'Open': O, 'High': H, 'Low': L, 'Close': C},
                           columns=['Open','High','Low','Close'])
        return ret.dropna()
    
    #最初の値を１００として割合に整形する関数
    @classmethod
    def TranData(self, histData):
        haba=histData['Close'][0]
        histData=histData/haba -1
        return histData
    
    #全通貨の相対価値を表示するチャート
    def ShowVersusAll(self):
        currencies=[]
        for key in self.pairList.keys():
            forward=key[:3]
            backward=key[3:6]
            if not forward in currencies:
                self.ShowVersusCurrency(forward)
                currencies.append(forward)
            if not backward in currencies:
                self.ShowVersusCurrency(backward)
                currencies.append(backward)
        
    #指定した通貨の相対価値を表示するチャート
    @classmethod
    def ShowVersusCurrency(self, currency):
        versusList={}
        for key in self.pairList.keys():
            forward=key[:3]
            backward=key[3:6]
            strVs='VS. '
            if forward==currency:
                # 前半がキー
                versusList[strVs + backward]=self.pairList[key]['Close']
            elif backward==currency:
                # 後半がキー
                # 反転して格納
                versusList[strVs + forward]=self.pairList[key]['Close'] * -1
        df = pd.DataFrame(versusList)
        display_charts(df, chart_type="stock", title=currency+' '+strVs, grid=True)
        
        return df
            
    #全ペアのチャートを表示
    @classmethod
    def ShowAll(self):
        df = pd.DataFrame({'EURUSD': self.pairList['EURUSD']['Close'],
                          'EURJPY': self.pairList['EURJPY']['Close'],
                          'USDJPY': self.pairList['USDJPY']['Close']})
        display_charts(df, chart_type="stock", title="MA cross", grid=True)
    
    #指定したペアのチャートを表示
    @classmethod
    def Show(self, pair):
        df = pd.DataFrame({pair: self.pairList[pair]['Close']})
        display_charts(df, chart_type="stock", title="MA cross", grid=True)
    
            
  