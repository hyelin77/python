# dan=int(input("원하는 단은: "))

# for i in range(1,10,1)：
#     print(dan,"*",i,"=",dan*i, end="   ")

#1부터 100까지의 합
# sum=0
# for i in range(1,101,1):
#     sum=sum+i
# print(f"합계는 {sum}")

a=int(input("원하는 수는: "))
sum=0
cnt=0
for i in range(1,a+1,1):
    if i%2==0:
        sum=sum+i
        cnt=cnt+1
print(f"개수는 {cnt}")
print(f"합계는 {sum}")
