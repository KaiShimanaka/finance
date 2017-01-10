# coding: utf-8
import numpy as np
import pandas as pd
from scipy.signal import lfilter, lfilter_zi
from numba import jit
import indicators as ind #indicators.pyのインポート
import math

# dfのデータからtfで指定するタイムフレームの4本足データを作成する関数
def AddHenkaritu(HistData, tankiHaba, tyoukiHaba):
    FastMA = ind.iMA(HistData, tankiHaba) #短期移動平均
    SlowMA = ind.iMA(HistData, tyoukiHaba) #長期移動平均
    
    
    #複数コレクションを同時にループ
    for (i,close),fast,slow in zip(enumerate(HistData['Close']),FastMA,SlowMA):
        
        #nullチェック 
        #平均線の最初は空白のため
        if (not math.isnan(fast)) & (not math.isnan(slow)):
            tankiHenkaritu[i]=close-fast
            tyoukiHenkaritu[i]=close-slow
#            HistData['tankiHenkaritu'][i]=close-fast
#            HistData['tyoukiHenkaritu'][i]=close-slow
        else:
            tankiHenkaritu[i]=0
            tyoukiHenkaritu[i]=0
#            #HistData['tankiHenkaritu'][i]=0
#            #HistData['tyoukiHenkaritu'][i]=0

    HistData.append(tankiHenkaritu)
    HistData.append(tyokiHenkaritu)
    return HistData

