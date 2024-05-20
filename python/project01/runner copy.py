# 프로그램
# 입출력시스템

from helpers.debug import *  

이름 = input("입력하세요: ")  # 입력값을 받아서 a에 저장
print(f"이름이 {이름}이시군요")  # f-string 사용


나이 = input("나이를 입력하세요: ")  # 입력값을 받아서 b에 저장

int(나이)  # 입력값을 정수로 변환
pt(나이) 

print(f"나이가 {나이}이시군요")  # f-string 사용


a= 3.14

print(int(a))

print(float(a))

pt(str(a))


a = 3.0 + 3.14

ppt(a)

ppt(int(a))


inch_cm = inch_to_cm(15.6)
cm_inch = cm_to_inch(10)

print(inch_cm)
print(cm_inch)


리스트 = [12,12,12]

print("a{}sda{}sd{}".format(*리스트))



print("   공백 제거   ".strip())  # 공백 제거
print("   공백 제거   ".lstrip())  # 왼쪽 공백 제거
print("   공백 제거   ".rstrip() ) # 오른쪽 공백 제거
print("   공백 제거   ".replace(" ", ""))  # 공백 제거
print("   공백 제거   ".split())  # 공백 제거

find__dd = "무궁화 꽃이 피었습니다.".find("꽃")  # 문자열 위치 찾기
print(find__dd)
find__dd1 = "무궁화 꽃이 피었습니다.".rfind("꽃")  # 문자열 위치 찾기
print(find__dd1)


a= r"C:\Users\USER\Desktop\workspace01\project01\runner copy.py".split("\\")  # 문자열 나누기

print(a)
print(a[-1].split(".")[1])