from student.getdata import jsonplaceholder
from student.getstudent import Student
from student.getteacher import Student, Teacher
from matha.mathm import Mathc

if __name__ == "__main__":

    #     student = [{

    #     "name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95
    # }, { "name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98
    # },{ "name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90},
    # { "name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92},{
    #     "name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98
    # }, { "name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92
    # }
    # ]
    # s1 = Student("윤인성", 87, 98, 88, 95)
    # s2 = Student("연하진", 92, 98, 96, 98)
    # s3 = Student("구지연", 76, 96, 94, 90)
    # s4 = Student("나선주", 98, 92, 96, 92)
    # s5 = Student("윤아린", 95, 98, 98, 98)
    # s6 = Student("윤명월", 64, 88, 92, 92)

    # # s1.get_student_info()
    # # s1.get_student_sum()
    # # s1.get_student_avg()

    # classroom = [Student(), Student(), Student(), Student(), Teacher()]

    # for person in classroom:
    #     if isinstance(person, Student):
    #         print("학생입니다.")
    #         str(person)
    #         person.get_student_info()
    #     elif isinstance(person, Teacher):
    #         str(person)
    #         print("선생님입니다.")

    obj = Mathc()

    print(obj == 1)
    print(obj != 1)
    print(obj > 1)
    print(obj >= 1)
    print(obj < 2)
    print(obj <= 2)


class Student:

    count = 0
    students = []

    @classmethod
    def print(cls):
        print("-----학생 목록-----")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("----- ----- -----")

    def __init__(self, name, kor, math, eng, sci):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng
        self.sci = sci
        Student.count += 1
        Student.students.append(self)


    def get_sum(self):
        return self.kor + self.math + self.eng + self.sci
    
    def get_avg(self):
        return self.get_sum() / 4   
    
    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_avg()}"
    




@property # 게터
def name(self):
    return self.__name
@name.setter # 세터
def name(self,name):
    self.name = name