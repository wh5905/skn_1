PI = 3.13159265359

def number_input():
    output = input("숫자 입력> ")
    return float(output)
def get_circumference(radius):
    return 2 * PI * radius

def get_cicle_area(radius):
    return PI * radius * radius