# num=int(input("정수를 입력하시오."))

# if num>0:
#     print("양수입니다.")
# elif num==0:
#     print("0입니다.")
# else:
#     print("음수입니다.")

score=int(input("점수를 입력하시오."))

if score>=81 and score<=100:
    print("학점은 A입니다.")
elif score>=61 and score<=80:
    print("학점은 B입니다.")
elif score>=41 and score<=60:
    print("학점은 C입니다.")
elif score>=21 and score<=40:
    print("학점은 D입니다.")
elif score>=0 and score<=20:
    print("학점은 E입니다.")