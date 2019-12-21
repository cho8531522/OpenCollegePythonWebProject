# 세 수 비교하기
a = input( )
나눈결과 = a.split()
b = int(나눈결과[0])
c = int(나눈결과[1])
d = int(나눈결과[2])

받은값 = [b, c, d]
e = sorted(받은값)
print(e[1])
