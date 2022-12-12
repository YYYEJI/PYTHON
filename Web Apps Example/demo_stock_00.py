import streamlit as st
import yfinance as yf


st.title("Stock Price")

ticker = yf.Ticker("MSFT")
data = ticker.history(start="2019-01-01")
st.line_chart(data.Close)
