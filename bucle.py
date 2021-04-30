def factorial1(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    
    print(ans)

factorial1(40)


def factorial2(y):
    ans = 1 

    while y != 0:
        ans = ans * y
        y = y - 1
    print(ans)

factorial2(10)

def factorial3(p):
    return p * factorial3(p - 1) if p > 1 else 1

print(factorial3(30))