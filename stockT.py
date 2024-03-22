##Incorporamos las librerias que vamos a usar
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
import altair as alt
import datetime

st.title('Stock Tracker')

tickerSymbol ='YOJ.SG'

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period="1M", start="2024-2-18", end="2024-3-18")

# Convert 'Date' column to datetime
tickerDf['Date'] = pd.to_datetime(tickerDf.index)

highlight = alt.selection_point(
    on="mouseover", fields=["symbol"], nearest=True
)

# Create line charts with Altair
line_chart_close = alt.Chart(tickerDf).mark_line().encode(
    x='Date',
    y='Close',
    color=alt.value("symbol")
).properties(
    width=600,
    height=300
)

line_chart_volume = alt.Chart(tickerDf).mark_line().encode(
    x='Date',
    y='Volume',
    color=alt.value("green")
).properties(
    width=600,
    height=300
)

st.altair_chart(line_chart_close)
st.altair_chart(line_chart_volume)


col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "24 ºC", "2.3")
col2.metric("Viento", "60 Km/H", "1")
col3.metric("LLuvia", "14 %", "-3")