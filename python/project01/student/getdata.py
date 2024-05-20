from urllib import request


def jsonplaceholder():
    target = 'https://jsonplaceholder.typicode.com/users'
    result = request.urlopen(target) 
    print(type(result))
    return result

