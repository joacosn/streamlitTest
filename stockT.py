import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px
import datetime

st.title('Stock Tracker')

tickerSymbol = "CMG"

try:
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start='2024-02-15', end='2024-02-15')
    
    if tickerDf.empty:
        st.error("No data available for the specified date.")
    else:
        st.line_chart(tickerDf.Close)
        st.line_chart(tickerDf.Volume)
except Exception as e:
    st.error(f"Error fetching data: {str(e)}")
