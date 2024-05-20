class Student:
    def __init__(self, name, kor, math, eng, sci):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng
        self.sci = sci
    def get_student_info(self):
        print(f"이름: {self.name}, 국어: {self.kor}, 수학: {self.math}, 영어: {self.eng}, 과학: {self.sci}")


    def get_student_sum(self):
        print(f"{self.name} 총점: {self.kor + self.math + self.eng + self.sci}")

    def get_student_avg(self):
        print(f"{self.name} 평균: {(self.kor + self.math + self.eng + self.sci)/4}")

    def __str__(self):
        return f"이름: {self.name}, 총점: {self.get_student_sum()}, 평균: {self.get_student_avg()}"
    

