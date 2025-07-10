
# score=[0,0,0]
# score[0]=int(input("국어 점수를 입력하세요:"))
# score[1]=int(input("수학 점수를 입력하세요:"))
# score[2]=int(input("영어 점수를 입력하세요:"))

score=[]
score.append(int(input("국어 점수를 입력하세요:")))
score.append(int(input("수학 점수를 입력하세요:")))
score.append(int(input("영어 점수를 입력하세요:")))

# tot=score[0]+score[1]+score[2]
tot=sum(score)
avg=round(tot/3,2) #정수와 정수 -> 실수 나올수도 있음, round는 반올림 함수(앞이 나누는 수, 뒤가 소수점 자리수)

print("총점: ",tot,"평균: ",avg)