import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# # 폰트 파일 경로
# font_path = r'C:\Windows\Fonts\H2GTRE.TTF'
# font_name = plt.matplotlib.font_manager.FontProperties(fname=font_path).get_name()

# plt.rcParams['font.family'] = font_name
# plt.rc('font', family=font_name)

# 한글 폰트 설정
# plt.rcParams['font.family'] = "AppleGothic"
# Windows, 리눅스 사용자
plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False

# DataFrame 생성
data = pd.DataFrame({
    '이름': ['영식', '철수', '영희'],
    '나이': [22, 31, 25],
    '몸무게': [75.5, 80.2, 55.1]
})

st.dataframe(data, use_container_width=True)

fig, ax = plt.subplots()
ax.bar(data["이름"], data["나이"])
# ax.pie(data["몸무게"], labels=data["이름"], autopct='%1.1f%%')
st.pyplot(fig)

barplot = sns.barplot(x='이름', y='나이', data=data, ax=ax, palette='bright', legend='full')
fig = barplot.get_figure()
st.pyplot(fig)


##### Barcode

code = np.array([
    1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,
    0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
    1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])

pixel_per_bar = 4
dpi = 100

fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')

st.pyplot(fig)
