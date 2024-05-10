from helpers.debug import *  # pt, pl

import datetime


if __name__ == "__main__":
    # number = input("숫자를 입력하세요: ")
    # number = int(number)

    # if number > 0:
    #     print("양수입니다.")

    # if number < 0:
    #     print("음수입니다.")

    # if number == 0:
    #     print("0입니다.")

    # now = datetime.datetime.now()
    # print(now.year, "년")
    # print(now.month, "월")
    # print(now.day, "일")
    # print(now.hour, "시")
    # print(now.minute, "분")
    # print(now.second, "초")

    # print(f"지금은 {now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초 입니다.")

    # nowTime = now.hour
    # print(nowTime)

    # if nowTime < 12:
    #     print("현재 시각은 {}시로 오전입니다".format(nowTime))
    # else:
    #     print("현재 시각은 {}시로 오후입니다".format(nowTime))

    # 변형된시간 = now.strftime("%Y-%m-%d %A %p %H:%M:%S")
    # 한글화된시간 = 변형된시간.replace("AM", "오전").replace("PM", "오후")
    # print(한글화된시간)

    # # score = int(input("점수를 입력하세요: "))

    # # if score > 100 or score < 0:
    # #     print("잘못된 점수입니다.")
    # # elif score >= 90:
    # #     print("수")
    # # elif score >= 80:
    # #     print("우")
    # # elif score >= 70:
    # #     print("미")
    # # elif score >= 60:
    # #     print("양")
    # # else
    # #     print("가")

    과일들 = [
        "사과",
        "바나나",
        "딸기",
        "포도",
        "수박",
        "참외",
        "키위",
        "복숭아",
        "자두",
        "망고",
    ]
    # 과일들[0] = "수박"
    # print(len(과일들))

    # 과일들.append("귤")
    # 과일들.insert(2, "오렌지")

    # print(과일들)

    # for i in range(0, len(과일들), 1):
    #     print(f"{i+1}번째 과일은 {과일들[i]}입니다.")

    # for idx, 과일 in enumerate(과일들):
    #     print(f"{idx+1}번째 과일은 {과일}입니다.")

    # for idx, 과일 in zip([for i in range(10):], [과일들]):
    #     print(f"{idx+1}번째 과일은 {과일}입니다.")

    # 빈리스트 = []
    # for i in range(11):
    #     if i >= 5:
    #         빈리스트.append(i)
    # print(빈리스트)
    # # =
    # empty_list = [x for x in range(11) if x >=5]
    # print(empty_list)

    # # 구구단
    # for i in range(2,10):
    #     print(f"{i}단".center(10,"="))
    #     for j in range(1,10):
    #         print(f"{i} x {j} = {i*j}")

    리스트딕션너리 = [
        {
            "postId": 1,
            "id": 1,
            "name": "id labore ex et quam laborum",
            "email": "Eliseo@gardner.biz",
            "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium",
        },
        {
            "postId": 1,
            "id": 2,
            "name": "quo vero reiciendis velit similique earum",
            "email": "Jayne_Kuhic@sydney.com",
            "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et",
        },
    ]

    # print(리스트딕션너리[1]["email"])

    # 리스트딕션너리[0]["id"] = 30

    # print(리스트딕션너리)

    # 딕셔너리 = {
    #         "postId": 1,
    #         "id": 2,
    #         "name": "quo vero reiciendis velit similique earum",
    #         "email": "Jayne_Kuhic@sydney.com",
    #         "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et",
    #     }

    # value = 딕셔너리.get("name")

    # for key in 딕셔너리:
    #     print(딕셔너리.get(key))
    # print(딕셔너리[key])

    # for key, vlaue in 딕셔너리.items():
    #     print(key, value)

    numebers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
    couter = {}

    for number in numebers:
        if number in couter:
            couter[number] += 1
        else:
            couter[number] = 1
    print(couter)

    # for number in numebers:
    #     couter[number] = numebers.count(number)
    # print(couter)

    # range(초기값, 끝값, 증가값)

    output = ""

    for i in range(1, 5):
        for j in range(4, i, -1):
            output += " "
        for k in range(0, i * 2 - 1):
            output += "*"
        output += "\n"

    print(output)
