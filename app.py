# uv add streamlit
# streamlit run app.py
import streamlit as st

st.title("用Streamlit架設網站")

#左側選單
st.sidebar.title("選單")
st.sidebar.write("這是選單的內容")

#網頁footer bottom聯絡資訊
st.footer.header("聯絡資訊")
st.footer.write("Email: example@gmail.com")