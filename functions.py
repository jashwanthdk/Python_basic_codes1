def greet():
    print('Hello')
    print('World')

greet()

def add(x,y):
    add = x + y
    print(add)
add(3,4)

def sub(x,y):
    return x-y
sub1=sub(3,4)
print(sub1)

def add_sub(x,y):
    c = x + y
    d = x - y
    return c,d

result1,result2 = add_sub(3,4)
print(result1, result2)

