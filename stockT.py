import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
##import plotly.express as px
##import datetime

st.title('Stock Tracker')

tickerSymbol ='YOJ.SG'

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1M', start='2024-2-18', end='2024-3-18')
    
st.line_chart(tickerDf.Close)

st.line_chart(tickerDf.Volume)
