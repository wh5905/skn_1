def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)


def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output


def fibonacci1(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci1(n - 1) + fibonacci1(n - 2)


counter = 0


def fibonacci2(n):
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci2(n - 1) + fibonacci2(n - 2)


print(fibonacci2(10))
print(counter)


dictionary = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output
    


def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))


