# 윤년
y = input()
yyyy = int(y)
yy = yyyy % 400
yyy = yyyy % 100
r = yyyy % 4
if yy == 0:
    print("1")
elif yyy == 0:
    print("0")
elif r == 0:
    print("1")
else:
    print("0")
