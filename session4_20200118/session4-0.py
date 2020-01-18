#class 만들기
class Human:
    #object를 만드는 함수 (= constructor)
    def __init__(self, name, age, address, blood):
        self.name = name
        self.age = age
        self.address = address
        self.blood = blood

    #class 안에 있는 함수는 method로 부름.
    def ageDouble(self):
        self.age = self.age * 2

    def introduce(self):
        print('제 이름은', self.name, '입니다. 나이는', self.age, '이고 ', self.blood, '형입니다. ')

하경 = Human("김하경", 19, '금천구', 'B')
하경.introduce()
하경.ageDouble()
하경.introduce()

용섭 = Human("이용섭", 20, '영등포', 'A')
용섭.introduce()
용섭.ageDouble()
용섭.introduce()