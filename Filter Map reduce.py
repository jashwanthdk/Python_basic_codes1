from functools import reduce
nums = [3,2,6,8,4,6,2,9]


evens = list(filter(lambda n:n%2==0,nums))

doubles = list(map(lambda n: n*2,evens))
print(doubles)
print(evens)

# evens = list(filter(is_even,nums))
#filter(function_name, iterable)

sum = reduce(lambda a,b: a + b,doubles)
print(sum)
# def is_even(n):
#     return n%2==0

