#함수의 선언

def calculator(calcType, a, b):
    if calcType == "add":
        return a + b
    elif calcType == "sub":
        return a - b
    elif calcType == "mul":
        return a * b
    elif calcType == "div":
        try:
            return a / b
        except: print("계산 에러가 발생했습니다. ")
    else:
        print("올바른 계산 타입이 아닙니다. ")

#파라미터가 없는 함수
def saygoodbye():
    return "Good Bye!"
#리턴이 없는 함수
def printgoodbye():
    print(saygoodbye())

a = calculator("add", 2, 3)
b = calculator("sub", 5, 3)
c = calculator("mul", 2, 3)
d = calculator("div", 4, 0)
print(a)
print(d)

print(saygoodbye())
printgoodbye()