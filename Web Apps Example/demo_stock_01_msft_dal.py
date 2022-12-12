import streamlit as st
import yfinance as yf


st.title("Stock Price")

st.write("## Microsoft")

ticker = yf.Ticker("MSFT")
data = ticker.history(start="2019-01-01")
st.line_chart(data.Close)

st.write("## Delta Air Lines")

ticker2 = yf.Ticker("DAL")
data = ticker2.history(start="2019-01-01")
st.line_chart(data.Close)
