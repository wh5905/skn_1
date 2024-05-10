from helpers.debug import *  # pt, pl
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


