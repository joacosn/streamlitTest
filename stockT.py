##Incorporamos las librerias que vamos a usar
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
##import altair as alt
import datetime

st.title('Stock Tracker')

tickerSymbol ='YOJ.SG'


tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period="1M", start="2024-2-18", end="2024-3-18")

tickerDf.reset_index(inplace=True)

fig_close = px.line(tickerDf, x='Date', y='Close', title='Close Price', color_discrete_sequence=['blue'])
fig_close.update_layout(legend_title=tickerSymbol)
fig_volume = px.line(tickerDf, x='Date', y='Volume', title='Volume', color_discrete_sequence=['green'], labels={'Volume': tickerSymbol})
fig_volume.update_traces(mode="lines+markers")  # Add markers to the lines for better visibility
fig_volume.update_layout(legend=dict(x=0, y=1))

st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)



col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "24 ºC", "2.3")
col2.metric("Viento", "60 Km/H", "1")
col3.metric("LLuvia", "14 %", "-3")