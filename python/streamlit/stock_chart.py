import streamlit as st
import FinanceDataReader as fdr
import datetime
from datetime import datetime, timedelta

from bs4 import BeautifulSoup

date = st.date_input(
    "조회 시작일을 선택해 주세요",
    datetime.now() - timedelta(days=365)
)

code = st.text_input(
    '종목코드', 
    value='005930',
    placeholder='종목코드를 입력해 주세요'
)

if code and date:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'Close']
    st.line_chart(data)