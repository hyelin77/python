num=int(input("1~3 숫자 입력: "))
match num:
    case 1:
        print("1 입력")
    case 2:
        print("2 입력")
    case 3:
        print("3 입력")
    case _:
        print('1~3 이외의 숫자')