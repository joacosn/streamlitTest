import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px
import datetime

st.title('Stock Tracker')

tickerSymbol = "GOOGL"

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period="1d",start="2020-01-01", end="2020-01-01")

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
