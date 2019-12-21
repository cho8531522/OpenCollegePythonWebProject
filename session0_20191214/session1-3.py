#list
#리스트의 생성은 list()를 사용하거나[]사용

a = list()
print(type(a))

b = []
print(type(b))

c = [1, 2, 3]
d = ['치킨', '피자', '명륜진사갈비']

print(c)
print(d)

print(c[0])
print(len(c))

#list에 다른 숫자 넣기
c[1] = -1
print(c)