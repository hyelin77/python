# dan=int(input("원하는 단은: "))

# for i in range(1,10,1)：
#     print(dan,"*",i,"=",dan*i, end="   ")

#1부터 100까지의 합
# sum=0
# for i in range(1,101,1):
#     sum=sum+i
# print(f"합계는 {sum}")

# a=int(input("원하는 수는: "))
# sum=0
# cnt=0
# for i in range(1,a+1,1):
#     if i%2==0:
#         sum=sum+i
#         cnt=cnt+1
# print(f"개수는 {cnt}")
# print(f"합계는 {sum}")


# for i in range(1,6):
#     for j in range(0, i):
#         print("*", end="")
#     print()


# for i in range(1,6):
#     for j in range(6, i, -1):
#         print("*", end="")
#     print()

# fruit=['참외', '파인애플', '사과', '바나나', '골드키위', '배']
# cart=[]
# for k in fruit:
#     if len(k) >=3:
#         cart.append(k)
# print()

과자={
    "꼬깔콘":2000,
    "새우깡":3830,
    "포카칩":1180
}
for k, v in 과자.items():
    print(k,v)