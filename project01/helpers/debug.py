def pt(a):
    print("==>", type(a))


def pl(a):
    print("==>", len(a))


def bool(a):
    print("==>", bool(a))


def pp(a):
    print(a)


def ppt(a):
    print("타입은", type(a))
    print(pt(a))


def inch_to_cm(raw_data):
    inch = int(raw_data)
    cm = inch * 2.54
    return cm


def cm_to_inch(raw_data):
    cm = int(raw_data)
    inch = cm / 2.54
    return inch


def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)


def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output
