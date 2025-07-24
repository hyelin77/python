import re

def check():
    while True: #참이면 무한 반복
        password = input("패스워드를 입력하시오: ")
        if len(password) < 8:
            print("패스워드는 최소한 8글자이어야 합니다.")
        elif re.search('[0-9]', password) is None:
            #  elif not re.findall('[0-9]', password):
            print("패스워드는 적어도 하나의 숫자를 가져야 합니다.") 
        elif re.search('[A-Z]', password) is None: 
            print("패스워드는 적어도 대문자를 가져야 합니다.") 
        elif re.search('[`~!#$%^&*()_\-+=\[\]{};:"\\|,<>/?]', password) is None: 
            print("패스워드는 적어도 특수문자를 가져야 합니다.")     
        else:
            print("규정에 맞는 패스워드입니다.")
            break
        
check() #함수 호출

# 최소 한개의 소문자 + 최소 한개의 대문자 + 최소 한개의 숫자 + 최소 한개의 특수 문자최소 8자 + 최대 10자 + 최소 8자 + 최대 10자
# ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,10}$



# findall()은 정규식과 매칭되는 모든 문자열을 리스트로 반환한다.
# search()는 문자열 전체를 검색하여 정규식과 매칭되는지 검사하여 매칭되는 첫 번째 부분만 반환하고, 
#             그 이후는 더 이상 검색하지 않음.
