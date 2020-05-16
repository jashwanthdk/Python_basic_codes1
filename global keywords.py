a = 20
b = 9
print(id(a))

def something():
    global a
    a = 15
    x = globals()['a']
    print(id(x))
    print("inside",x)

something()


print("outside",a)
#outside the func global variable
#inside the func local variable
