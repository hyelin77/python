# num=int(input("정수를 입력하시오."))

# if num%2==0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")

year=int(input("연도를 입력하시오."))

if year%4==0 and year%100!=0 or year%400==0:
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 윤년이 아닙니다.")