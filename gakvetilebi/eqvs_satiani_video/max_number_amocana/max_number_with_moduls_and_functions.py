import func_max_number
from func_max_number import max_number

numbers = [1, 2, 40, 2321, 12, 340, 45]

print("################################ 0 ")
print(max(numbers))


print("################################ 1 ")
print(max_number(numbers))
print(type(max_number(numbers)))

print("################################ 2 ")
x = func_max_number.max_number(numbers)
print(x)
print(type(x))
