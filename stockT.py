import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px
import datetime

st.title('Stock Tracker')

tickerSymbol = 'CMG'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d',start='2024-03-18', end='2024-03-18')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
