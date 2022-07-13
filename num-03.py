"""
재귀함수를 이용하여 Factorial 을 구하는 함수를 구하시오.
"""

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


result = factorial(4) 

print(result)