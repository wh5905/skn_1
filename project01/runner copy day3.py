from helpers.debug import *  # pt, pl
from helpers.mathf import *  # sum_all
import time

if __name__ == "__main__":

    # 누적합
    sum = 0
    while True:
        sum += 1

        if sum == 10:
            break
    print(sum)

    list_test = [1, 2, 2, 3, 1]
    value = 2

    while value in list_test:
        list_test.remove(value)

    print(list_test)

    # print(time.time())

    더할수열 = list(range(1, 101))
    합 = 0
    i = 0
    while True:
        i += 1
        if i % 2 == 0:
            continue
        if i >= 100:
            break
        합 += 더할수열[i - 1]
    print(합)

    key_list = ["name", "hp", "mp", "level"]
    value_list = ["기사", 200, 30, 5]
    character = {}

    for i in range(len(key_list)):
        character[key_list[i]] = value_list[i]

    print(character)

    max_value = 0
    a = 0
    b = 0

    for i in range(1, 100):  # 1부터 99까지
        j = 100 - i

        # 최대값 구하기
        if i * j > max_value:  # i * j가 max_value보다 크면
            max_value = i * j  # max_value에 i * j를 넣고
            a = i  # a에 i를 넣고
            b = j  # b에 j를 넣는다
    print(a, b, max_value)

    example_list = ["요소A", "요소B", "요소C"]
    print(list(enumerate(example_list)))
    # [(0, '요소A'), (1, '요소B'), (2, '요소C')]

    list_test1 = [i * i for i in range(0, 20, 2)]
    print(list_test1)

    codon = "ctacaatgtcagtatacccattgcattgcattagccggccta"
    codon_dict = {}
    for i in range(0, len(codon), 3):
        codon_dict[codon[i : i + 3]] = codon_dict.get(codon[i : i + 3], 0) + 1

    print(codon_dict)

    print()

    print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

    print("A.", sum_all(0, 100, 10))
    print("B.", sum_all(end=100))
    print("C.", sum_all(end=100, step=2))

    print(fibonacci2(10))
    print(counter)

    page_read = r"C:\Users\USER\Desktop\workspace01\skn_1\readme.md"

    open_file = open(page_read, encoding="utf-8")

    page_read = open_file.read()
    page_read2 = open_file.readline()
    page_read3 = open_file.readlines()

    print(page_read)

    open_file.close()

    with open(page_read, "r", encoding="utf-8") as file:
        print(file.read())

    import random

    random_file =  r"C:\Users\USER\Desktop\workspace01\skn_1\project01\helpers\random.txt"
    
    hanguls = list("가나다라마바사아자차카타파하")

    with open(random_file, "w") as file:
        for i in range(1000):
            name = random.choice(hanguls) + random.choice(hanguls)
            weight = random.randrange(40, 100)
            height = random.randrange(140, 200)

            file.write("{}, {}, {} \n".format(name, weight, height))

    with open("info.txt", "r") as file:
        for line in file:
            (name, weight, height) = line.strip().split(", ")

            if (not name) or (not weight) or (not height):
                continue

            bmi = int(weight) / ((int(height) / 100) ** 2)

        result = ""

    if 25 <= bmi:
        result = "과체중"
    elif 18.5<= bmi:
        result = "정상 체중"
    else:
        result = "저체중"

    print('\n'.join([
        "이름: {}",
        "몸무게: {}",
        "키: {}",
        "BMI: {}",
        "결과: {}"
    ]).format(name, weight, height, bmi, result))

    
