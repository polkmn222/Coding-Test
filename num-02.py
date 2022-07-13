"""
아래처럼 “.”으로 함수를 계속 추가할 수 있는 구조(체이닝 메소드)를 이용하여 add,
substract 함수를 구현하고 그 결과를 출력하십시오.
"""

result = 0

class calculator:

    def add(self, inp):
        global result
        result = result + inp
    def sub(self, inp):
        global result
        result = result - inp 

    def toZero(self):
        global result
        result = 0

cal = calculator()
cal.add(4)
cal.add(5)
cal.sub(3)
print(result)