def update(x):
    print(id(x))
    x[1] = 25
    print("x = ",x)

x = [10,20,30]
print(id(x))
update(x)
print("x = ",x)

#we dont use pass by value or pass by reference in python