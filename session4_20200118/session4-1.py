#class
class Movie:
    def __init__(self, tittle, actor, director, genre):
        self.tittle = tittle
        self.genre = genre
        self.actor = actor
        self.director = director

    def book(self):
        print(self.tittle, '예약되었습니다. ')
        print(self.tittle, self.actor, self.genre, self.director)

class Actionmovie(Movie):
    def __init__(self, tittle, actor, director, blood):
        super().__init__(tittle, actor, director, '액션')
        self.blood = blood

    def book(self):
        #super class 의 함수 사용할 때
        super().book()
        #super class에 오버로드 할 때
        print('액션영화', self.tittle, '예약되었습니다.')

male = Movie('말레피센트', '안젤리나 졸리', '디즈니', 'fantasy')
male.book()

born = Actionmovie('본시리즈', '맷 데이먼', '어찌구', 'yes')
born.book()