ㅁ = input()
나눈결과 = ㅁ.split()
b = 나눈결과[0]
c = 나눈결과[1]

d = int(b)
e = int(c)

if d < e:
    print('<')

if d > e:
    print('>')

if d == e:
    print('==')