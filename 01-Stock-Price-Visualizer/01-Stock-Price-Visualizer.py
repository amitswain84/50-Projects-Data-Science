import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Project 01 Stock Price Visualizer

Shown are the Stock **Closing Price** and **Volume** of ***APPLE***
""")

# define the ticker symbol
tickerSymbol = 'AAPL'

# get data on thr ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(
    period='1d', start='2005-01-15', end='2021-01-15')
# Open High Low Close Volume Dividents Stock Splits

st.write("""
## Closing Price 
""")
st.area_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.area_chart(tickerDf.Volume)
