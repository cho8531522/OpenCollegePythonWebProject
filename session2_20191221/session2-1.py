#딕셔너리에서 ket, value만 빼서 list 만들기
a = {'이근호' : 19, "임은지" : 17, "김하경" : 15}

a_key = list(a.keys())

print(a_key)

a_values = list(a.values())
print(a_values)

#딕셔너리 전체 리스트로 만들기
a_item = list(a.items())
print(a_item)
