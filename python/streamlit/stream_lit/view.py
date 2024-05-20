import streamlit as st
import numpy as np
import pandas as pd
import datetime
from datetime import datetime as dt


class View:
    def __init__(self, appname):
#         st.title(appname)
#         st.title(":sunglasses:")
#         st.title(":sunglasses:")
#         st.header("데이터를 보여드릴게요! :sparkles:")
#         st.caption("이미지 표시 :sparkles:")
#         sample_code = """
# def func01():
#     print("Hello, World!")
    
# """

#         st.code(sample_code, language="python")
#         st.text("제가 만든 모델입니다.")
#         st.markdown("# 모델을 사용해보세요!")
#         st.html("<h1>HTML 코드를 넣어보세요!</h1>")
#         st.markdown("모델을 사용해보세요! :green[초록색]으로 그리기")
# #         st.html("<hr>")
#         st.title("데이터 프레임")
        
        
        
        dataframe = pd.DataFrame(
            {
                "first column": [1, 2, 3, 4],
                "second column": [10, 20, 30, 40]
            }
        )

#         st.dataframe(dataframe, use_container_width=False)

#         st.table(dataframe)
#         # st.metric(label="온도", value="10도", delta="1.2")
#         # st.metric(label="삼성전자우", value="61,000", delta="-1.2")

#         col1, col2, col3 = st.columns(3)
#         col1.metric(label="온도", value="10도", delta="1.2도")
#         col2.metric(label="삼성전자우", value="61,000", delta="-1.2%")
#         col3.metric(label="애플", value="119,000", delta="3%")

        button1 = st.button("버튼을 눌러보세요!")
        if button1:
            st.write(":blue[버튼]이 눌렸습니다.")
        button2 = st.button("되돌리기")
        if button2:
            st.write("reset")
            st.experimental_rerun()

        st.download_button(
            label="csv 다운로드",
            data= dataframe.to_csv(),
            file_name="sample.csv",
            mime="text/csv"
            
            )
        
        agree = st.checkbox("동의")

        if agree:
            st.write("동의하셨습니다.:100:")
        
        mbti = st.radio("당신의 MBTI는?", ("ENFP", "INTJ", "INFP", "ENTJ"))
        mbti2 = st.selectbox("당신의 MBTI는?", ("ENFP", "INTJ", "INFP", "ENTJ"))
        mbti3 = st.multiselect("당신의 MBTI는?", ("ENFP", "INTJ", "INFP", "ENTJ"))

        values = st.slider("값을 선택하세요.", 0, 100, (25, 75))

        # start_time = st.slider(min_value=dt(2021,1,1,0,0), max_value=dt(2024,1,1,0,0)
        #                        , value=(dt(2021,1,1,0,0))
        #                        step= dt.timedelta(hours=1),
        #                         format="YYYY-MM-DD HH:mm:ss")
        # st.write(start_time)
        

        title = st.text_input(label="나이입력", placeholder=20)
        title = st.number_input(label="나이입력", placeholder=20, step=1)
        

        




        
