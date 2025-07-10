num=input("주민등록번호: ")

num = num.split("-")[1]
print("추출문자열: ", num)

if num[0]=="1" or num[0]=="3":
    print("남자입니다.")
elif num[0]=="2" or num[0]=="4":
    print("여자입니다.")