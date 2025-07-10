print("안녕하세요?")
name=input("이름이 어떻게 되시나요? ")
print(f"만나서 반갑습니다. {name}씨")
print('이름의 길이는 다음과 같군요:'+str(len(name)))
age=int(input("나이가 어떻게 되시나요? "))
#input은 기본적으로 문자만 받음
print("내년이면 "+str(age+1)+"이 되시는군요.")
addr=input("주소가 어떻게 되시나요? ")
addr2=addr.split()
# split = 기본적으로 공백을 기준으로 문자열을 나눔
print(addr2[2]+"에 사시는군요.")