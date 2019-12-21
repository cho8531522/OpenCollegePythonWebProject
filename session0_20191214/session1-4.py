#list 조작하기 넣었다, 뺐다

opencollegesaturday = list()
opencollegesaturday.append('은지님')
opencollegesaturday.append('혜원님')
opencollegesaturday.append('하경님')
opencollegesaturday.append('선혜님')

print(opencollegesaturday)

opencollegesaturday.remove('선혜님')

print(opencollegesaturday)

a = [-1, 2, 200, 0, 3]
a.sort()
print(a)

a.sort(reverse=True)
print(a)
b = sorted(a)
print(b)

#변경못하는 리스트 튜플 ()로 표현한 리스트
a = ("은지님", "혜원님", "하경님")
