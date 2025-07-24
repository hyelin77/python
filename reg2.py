import re #파이썬에서 정규 표현식을 사용할 때, 내장 모듈인 re를 사용함

pattern=r'^[\w]+@[\w]+\.[A-Za-z]{2,4}$'
#r > 문자 그대로
# ^ > 시작
#$>끝
#[] > 문자 범위
#\w > 문자나 숫자
# @ > 그 자체 @
# \. > 그자체 .(점)
#{2, 4} > 2~4개 반복

def checkEmail(emailAddress):
    if(re.fullmatch(pattern, emailAddress)):
        #re.fullmatch()는 문자열 전체가 주어진 정규 표현식과 일치하는지 확인
        print(f"{emailAddress}는 유효한 이메일 주소입니다.")
    else:
        print(f"{emailAddress}는 유효하지 않은 이메일 주소입니다.")

email=input("이메일을 입력하세요: ")
checkEmail(email) #함수 호출