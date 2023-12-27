import pandas as pd 
import matplotlib.pyplot as plt 
import yfinance as yf 

from adtk.data import validate_series
from adtk.detector import *

from adtk_modif.src.adtk.visualization import plot  


df_gubre = yf.download('GUBRF.IS', start='2021-06-12', end='2023-12-26', actions=True)['Close']

df_gubretas  = validate_series(df_gubre)

volatiliy_detector = VolatilityShiftAD(c=6.0, side='positive', window=15)
anomalies = volatiliy_detector.fit_detect(df_gubretas)

plot(df_gubretas, anomaly=anomalies, anomaly_color='red', anomaly_tag='marker')
plt.show()