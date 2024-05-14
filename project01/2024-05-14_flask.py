# from flask import Flask

# app = Flask(__name__)

# #@ is a decorator
# #함수를 다른 함수의 인자로 사용하고 싶을 때 사용
# @app.route('/')
# def hello():
#     return 'Hello, World!'

from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/')

# hello 함수는 웹 페이지에 날씨 정보를 출력하는 함수
def hello():
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    soup = BeautifulSoup(target, "html.parser")

    output = ""

    for loc in soup.select("location"):
        output += "<h3>{}<h3>".format(loc.select_one('city').string)
        output += "날씨{}<br/>".format(loc.select_one('wf').string)
        output += "최저/최고기온: {}/{}".format(loc.select_one("tmn").string, loc.select_one("tmx").string)
        output += "<hr/>"
    return output


