"""
3 번에서 구현한 함수에서 입력값이 큰 경우 Stack Overflow 가 발생합니다. 이 경우 해결할
수 있는 방법을 구하시오. Ex) factorial(1,000,000)
"""


import timeit

def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac

 
start = timeit.default_timer()

result = factorial(1000000)

stop = timeit.default_timer()

print(result)
print(stop - start)
