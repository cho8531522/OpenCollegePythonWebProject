#전화번호부 만들기
def deleteaddressbook():
    command2 = input('삭제될 사람의 이름을 입력하세요. ')
    a = str(command2)
    if a in addressbook.keys():
        del addressbook[a]
        print('삭제되었습니다.')
    else:
        print('삭제할 번호가 없습니다.')

def queryaddressbook():
    if len(addressbook) == 0:
        print('등록된 번호가 없습니다. ')
    else:
        for i in addressbook.items():
            print('이름: ' ,  , '번호: ' , addressbook[1])

def addaddressbook():
    command2 = input('이름, 번호를 입력하세요.')
    a = command2.split()
    addressbook[a[0]] = a[1]
    print('추가되었습니다.')

addressbook = {}
while True:
    command = input('등록된 전화번호를 조회하려면 조회, 전화번호를 추가하려면 추가, 삭제하려면 삭제를 입력하세요. 끝내려면 끝을 입력하세요. ')

    def endaddressbook():
        print('프로그램이 종료됩니다. ')

    if command == '조회':
        queryaddressbook()

    elif command == '추가':
        addaddressbook()

    elif command == '삭제':
        deleteaddressbook()

    elif command == '끝':
        endaddressbook()
        break
    else:
        print('명령어가 잘못되었습니다.')