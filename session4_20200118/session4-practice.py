class Car:
    def __init__(self, 제조사, 모델, 색상):
        self.제조사 = 제조사
        self.모델 = 모델
        self.색상 = 색상
        self.기름양 = 1000

    def 전진(self):
        self.기름양 = self.기름양 - 50
        print(self.제조사, self.모델, self.색상, '차량 전진중입니다! 현재 기름양: ', self.기름양)

    def 후진(self):
        self.기름양 -= 30
        print(self.제조사, self.모델, self.색상, '차량 후진중입니다! 현재 기름양: ', self.기름양)

차1 = Car('현대', '아반떼', '흰색')
차1.전진()
차1.후진()

차2 = Car('BMW', '520D', '검은색')
차2.전진()
차2.후진()
차3 = Car('Audi', 'A7', '붉은색')
차3.전진()
차3.후진()

class Electriccar(Car):
    def __init__(self, 제조사, 모델, 색상):
        super().__init__(제조사, 모델, 색상)
        self.기름양 = 100

    def 전진(self):
        self.기름양 = self.기름양 - 10
        print(self.제조사, self.모델, self.색상, '차량 전진중입니다! 현재 충전량: ', self.기름양, '%')

    def 후진(self):
        self.기름양 = self.기름양 - 5
        print(self.제조사, self.모델, self.색상, '차량 전진중입니다! 현재 충전량: ', self.기름양, '%')


tessla = Electriccar('테슬라', '어띠구', 'red')
tessla.전진()
tessla.후진()


