import streamlit as st
import yfinance as yf


st.title("Stock Price")

symbol = st.radio("Stock Symbol", ["MSFT", "DAL"])

ticker = yf.Ticker(symbol)
data = ticker.history(start="2019-01-01")
st.line_chart(data.Close)
st.dataframe(data)