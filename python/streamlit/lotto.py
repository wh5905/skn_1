import streamlit as st
import random
import datetime

st.title("로또 번호 생성기")

st.write("로또 번호 생성기입니다. 번호를 생성하시려면 아래의 버튼을 눌러주세요.")


def g_lotto():
    lotto = set()

    while len(lotto) < 6:
        lotto1 = random.randint(1, 46)
        lotto.add(lotto1)
    lotto = list(lotto)
    lotto.sort()
    return lotto


button = st.button("로또 번호 생성")

if button:
    for i in range(1, 6):
        st.subheader(f"{g_lotto()}")

# if button:
#     lotto = random.sample(range(1,46), 6)
#     lotto.sort()
#     st.write(lotto)
#     st.write(datetime.datetime.now())
#     st.write("로또 번호 생성 완료")

from streamlit.components.v1 import html


my__js = """
<script src="https://cdn.jsdelivr.net/npm/@tsparticles/confetti@3.0.3/tsparticles.confetti.bundle.min.js"></script>
<script>
const defaults = {
  spread: 360,
  ticks: 100,
  gravity: 0,
  decay: 0.94,
  startVelocity: 30,
  shapes: ["heart"],
  colors: ["FFC0CB", "FF69B4",  = "FF1493", "C71585"],
};

confetti({
  ...defaults,
  particleCount: 50,
  scalar: 2,
});

confetti({
  ...defaults,
  particleCount: 25,
  scalar: 3,
});

confetti({
  ...defaults,
  particleCount: 10,
  scalar: 4,
});
</script>
"""

my_html = f"{my__js}"

html(my_html)
