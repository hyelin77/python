def hello():
    print("안녕하세요")

hello()
print('-'*20)

def hello():
    value="안녕하세요"
    return value

result=hello()
print(result)
print('-'*20)

def hello(h):
    print(h)

value="안녕하세요"
hello(value)
print('-'*20)

def hello(h):
    return_value= h + "반갑습니다"
    return  return_value

value="안녕하세요"
resulte=hello(value)
print(result)
print('-'*20)