# uv add streamlit
# streamlit run app.py
import streamlit as st

st.title("用Streamlit架設網站")

#左側選單
#st.sidebar.title("選單")
#st.sidebar.write("這是選單的內容")

with st.sidebar:
    st.title("選單標題")
    st.write("選單內容")
    st.button("按鈕A")
    st.button("按鈕K")

#網頁footer bottom聯絡資訊
st.bottom.header("聯絡資訊")
st.bottom.write("Email: example@gmail.com")