
def 수리수리():
    a,b = map(int, input().split())
    c   =  list(map(int, input().split()))
    count = 0
    for i in range(a):
        for j in range(i, a):
            if b -(c[j]-c[i])  == 1:
                count += 1
    
    print(count)

수리수리()



def 수리수리():
    a,b = map(int, input().split())
    c   =  list(map(int, input().split()))

    tmp = c[0] - 0.5


