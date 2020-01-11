def calc(type, a, b):
    if type == "더하기":
        return a + b
    elif type == "빼기":
        return a - b
    elif type == "곱하기":
        return a * b
    elif type == "나누기":
        return a / b

while True:
    a = input("계산정보를 입력하세요: ")
    input_list = a.split()
    a = int(input_list[1])
    b = int(input_list[2])
    try:
        result = calc(a[0], c, d)
        print("계산결과 : " + str(result))
    except:
        print("계산 에러가 발생했습니다. ")

