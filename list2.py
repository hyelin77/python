movie_rank=["극한직업","아바타","범죄도시"]

movie_rank.append("배트맨")
print(movie_rank)

movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

del movie_rank[3] #del은 삭제
print(movie_rank)

print(len(movie_rank))

nums=[1,2,3,4,5]
average=sum(nums)/len(nums) #len은 list의 갯수를 구하는 함수
print(average)