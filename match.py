# num=int(input("1~3 숫자 입력: "))
# match num:
#     case 1:
#         print("1 입력")
#     case 2:
#         print("2 입력")
#     case 3:
#         print("3 입력")
#     case _:
#         print('1~3 이외의 숫자')

# num1=int(input("짝수 입력: "))
# num2=int(input("홀수 입력: "))
# match num1%2, num2%2:
#     case 0, 1:
#         print("num1은 짝수, num2는 홀수")
#     case 0, _:
#         print("num1은 짝수")
#     case _, 1:
#         print("num2는 홀수")
#     case _:
#         print("둘 다 오류")


num=int(input("수 입력: "))
match num%3, num%5:
    case 0, 0:
        print("3과 5의 배수")
    case 0, _:
        print("3의 배수")
    case _, 0:
        print("5의 배수")
    case _:
        print("둘 다 오류")
