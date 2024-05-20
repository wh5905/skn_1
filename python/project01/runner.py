import math
from helpers.debug import *  # pt, pl

if __name__ == "__main__":
    문자열 = "안녕하세요"
    로우로처리 = r"\n"
    더블로처리 = "\\n"
    # 읽을경로파일 = "C:\\Users\\USER\\Desktop\\workspace01\\project01\\runner.py"
    # 읽을경로파일2 = r"C:\Users\USER\Desktop\workspace01\project01\runner.py"
    정수 = 123
    실수 = 123.456
    불 = True

    # print(읽을경로파일)
    # print(읽을경로파일2)

    pt(문자열)
    pt(정수)
    pt(실수)
    pt(불)
    # print(로우로처리)
    # print(더블로처리)

a = "안녕하세요 홍길동님"

print(a[3] + a[3] + a[3])
print(a[6:9])
print(a[-1:-4:-1])
# print(a[10]) # out of range

print(len(a))
# print(dir(a))

# pp(dir(1))
print(math.pow(2, 4))

pi = math.pi
print(pi)  # 3.141592653589793

pi = 3.14
print(pi)  # 3.14 재할당

b = input("Press Enter to continue...")
print(b)  # 입력값 출력
