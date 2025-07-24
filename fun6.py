def ggd1():
    for i in range(2,10):
        print(i, "단")
        for j in range(1, 10):
            print(i, "*", j, "=", i*j)
        print()

def ggd2():
    for i in range(2,10):
        print(i, "단")
        for j in range(1, 10):
            print(i, "*", j, "=", i*j, end="  ")
        print()


con=True
while con : #True는 무한루프(1과 같은 뜻)
    num=int(input("메뉴를 입력하세요(1은 세로형 구구단, 2는 가로형 구구단, 0은 종료):  "))
    if num==1:
        print("1선택-세로형 구구단")
        ggd1()

    elif num==2:
        print("2선택-가로형 구구단")
        ggd2()
        
    elif num==0:
        print("종료합니다.")
        con=False

    else:
        print("선택 오류입니다. 다시 입력하세요.")

#함수 정의는 꼭대기에 할 필요는 없지만, 호출 전까지는 해야 함
