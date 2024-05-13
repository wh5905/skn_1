import math


# 예외 고급
try:
    number_input_a = int(input("정수 입력"))

    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)


except Exception as exception:
    # 예외 객체를 출력
    print("(exception):", type(exception))
    print("exception:", exception)


# 예외 구분
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외를 처리합니다.
try:
    number_input = int(input("정수 입력"))

    print(f"{number_input}번째 요소: {list_number[number_input]}")

# 예외 발생 시 except 블록이 실행됩니다.
except IndexError as exception:
    print("범위를 벗어난 인덱스입니다.")

except ValueError as exception:
    print("정수를 입력해 주세요.")

except Exception as e:
    print(type(e))
    print(e)


