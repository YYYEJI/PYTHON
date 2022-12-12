import streamlit as st
import yfinance as yf


st.title("Stock Price")

symbol = st.text_input("Stock Symbol")

ticker = yf.Ticker(symbol)
data = ticker.history(start="2019-01-01")
st.line_chart(data.Close)
