class Student:
    def stduy(self):
        print("공부하기")

    def __str__(self):
        return "학생입니다."

class Teacher:
    def teach(self):
        print("가르치기")
    def __str__(self):
        return "선생님입니다."
        