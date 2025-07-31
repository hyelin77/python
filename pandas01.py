import pandas as pd

series1=pd.Series([2,4,6,8,10])
print(series1)

num=[1,2,3,4,5]
score_java=pd.Series([98,76,60,85,80], index=num)
score_python=pd.Series([88,92,100,55,70], index=num)

print(score_java)
print(score_python)

total=score_java+score_python
print("덧셈 결과는")
print(total)

print("index 기준 내림차순 정렬")
print(total.sort_index(ascending=False))
print("# 값 기준 오름차순 정렬")
print(total.sort_values(ascending=True))
print("값 기준 내림차순 정렬")
print(total.sort_values(ascending=False))

t1=total.sort_values(ascending=True)
t1.to_csv('./res01.csv')