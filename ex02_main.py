from ex02_fun import *

run=True
while run:
    num=int(input("메뉴를 선택하세요(0종료) 메뉴번호:  "))
    if num==1:
        v_gugudan()

    elif num==2:
        h_gugudan()

    elif num==0:
        print("종료")
        run=False
    else:
        print("선택 오류. 다시 선택하세요.")