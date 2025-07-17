total=0
answer='yes'
while answer=='yes':
    num=int(input("숫자를 입력하세요: "))
    total=total+num
    answer=input("계속하실까요?(yes/no): ")
print("합계는: ", total)
