# KOREA 문자열 만들기


import sys 

t = list(sys.stdin.readline())

print(t)


count = 0
for i in range(len(t)):
    if 'k' in t:
        count += 1
        if 'o' in t:
            count += 1
            if 'k' in t:
                count += 1
                if 'o' in t:
                    count += 1
                    if 'o' in t:
                        count += 1

print(count)
# 딕셔러니 
