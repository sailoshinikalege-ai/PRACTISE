
#21. Write a program to pack three numbers into one variable and print it.
def pack(*a):
    print (a)
pack(10,20,30)

#22. Write a program to unpack three values into three variables.

def unpack(c1,c2,c3):
    print(c1,c2,c3)
unpack(*(20,20,40))

#23. Write a program to pack multiple values and find their sum after unpacking.
def sum(*a):
  x, y, z = a
  print(x + y + z)
sum (*(10,20,30))


# 24. Write a program using starred unpacking to store
# the first value separately and remaining values in a list.

def value(v1, *v2):
    print(v1)
    print(v2)

value(*(10, 20, 30, 40))


# 25. Write a program using starred unpacking to store the last value separately.

def value(*a):
    *x, y = a
    print(x)
    print(y)

value(10, 20, 30, 40)

# 26. Write a program to unpack the characters of a three-letter string into three variables.

ch = "CAT"

a, b, c = ch

print(a)
print(b)
print(c)


# 27. Write a program to swap two variables using unpacking.

a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

# 28. Write a program to unpack a tuple containing five values.

a = (10, 20, 30, 40, 50)

a1, a2, a3, a4, a5 = a

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)

# 29. Write a program to separate the first and last elements using unpacking.

a = (10, 20, 30, 40, 50)

first, *middle, last = a

print("First =", first)
print("Last =", last)


# 30. Write a program to unpack a list and print each value separately.

a = [10, 20, 30, 40]

a1, a2, a3, a4 = a

print(a1)
print(a2)
print(a3)
print(a4)
