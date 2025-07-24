def get_input():
    return 2,3

x, y=get_input()
print(x, y)

def calculate (radius):
    area=3.14*radius**2 # **는 거듭제곱
    perimeter=2.0*3.14*radius
    return area, perimeter

x,y=calculate(10)
print(x, y)
