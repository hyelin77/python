def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    #n=5
    #5*fact(4)
    #4*fact(3)
    #3*fact(2)
    #2*fact(1)
    
n=int(input("정수를 입력하세요: "))
f=fact(n)
print(n, "!은", f, "이다.")
