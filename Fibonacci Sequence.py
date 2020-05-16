a = 1
b = 1

num = int(input("Enter the number of numbers to be displayed :"))
print("1 1",end = " ")
for i in range(num - 2):
    c = a + b
    print(c,end=" ")
    a = b
    b = c
