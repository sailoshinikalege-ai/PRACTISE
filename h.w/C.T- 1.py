#SECTION F — BASIC PYTHON PROGRAMS



#1. Simple Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


#2. Even or Odd
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


#3. Positive, Negative or Zero
n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


#4. Largest Between Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)


#5. Largest Among Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest:", a)
elif b > a and b > c:
    print("Largest:", b)
else:
    print("Largest:", c)


#6. Divisibility Check
n = int(input("Enter a number: "))

if n % 5 == 0 and n % 7 == 0:
    print("Divisible by both 5 and 7")
else:
    print("Not divisible by both 5 and 7")


#7. Age Calculator
birth = int(input("Enter birth year: "))
current = int(input("Enter current year: "))

age = current - birth

print("Age:", age)

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#8. Student Pass or Fail
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

#9. Grade Calculator
marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")


#10. Multiplication Table
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)


#11. Sum From 1 to N
n = int(input("Enter a number: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum:", sum)


#12. Factorial of a Number
n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial:", fact)

#13. Count Digits
n = int(input("Enter a number: "))
count = 0

while n > 0:
    digit = n % 10
    count = count + 1
    n = n // 10

print("Number of digits:", count)

#14. Sum of Digits
n = int(input("Enter a number: "))
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits:", sum)

#16. Palindrome Number
n = int(input("Enter a number: "))
original = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if original == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

#17. Armstrong Number
n = int(input("Enter a three digit number: "))
original = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit * digit * digit
    n = n // 10

if original == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

#18. Count Even and Odd Digits
n = int(input("Enter a number: "))
even = 0
odd = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    n = n // 10

print("Even digits:", even)
print("Odd digits:", odd)


#19. Product of Digits
n = int(input("Enter a number: "))
product = 1

while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10

print("Product:", product)

#20. Largest Digit
n = int(input("Enter a number: "))
largest = 0

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    n = n // 10

print("Largest digit:", largest)

#21. Smallest Digit
n = int(input("Enter a number: "))
smallest = 9

while n > 0:
    digit = n % 10

    if digit < smallest:
        smallest = digit

    n = n // 10

print("Smallest digit:", smallest)

#22. Count a Particular Digit
n = int(input("Enter a number: "))
d = int(input("Enter the digit to count: "))
count = 0

while n > 0:
    digit = n % 10

    if digit == d:
        count = count + 1

    n = n // 10

print("Occurrences:", count)

#23. Sum of Even Digits
n = int(input("Enter a number: "))
sum = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        sum = sum + digit

    n = n // 10

print("Sum of even digits:", sum)

#24. Sum of Odd Digits
n = int(input("Enter a number: "))
sum = 0

while n > 0:
    digit = n % 10

    if digit % 2 != 0:
        sum = sum + digit

    n = n // 10

print("Sum of odd digits:", sum)


#25. Perfect Number
n = int(input("Enter a number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

#26. Prime Number
n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")


#27. Print Prime Numbers from 1 to 100
for n in range(2, 101):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        print(n)

#28. Fibonacci Series
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#29. Power of a Number
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

power = 1

for i in range(exponent):
    power = power * base

print("Power:", power)

#30. Sum of Even Numbers from 1 to 100
sum = 0

for i in range(2, 101, 2):
    sum = sum + i

print("Sum:", sum)

#31. Sum of Odd Numbers from 1 to 100
sum = 0

for i in range(1, 101, 2):
    sum = sum + i

print("Sum:", sum)

#32. Print Numbers in Reverse Order
n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    print(i)

#33. Multiples of a Number
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n * i)

#34. Numbers Divisible by Both 3 and 5
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#35. Skip Multiples of 3
for i in range(1, 51):

    if i % 3 == 0:
        continue

    print(i)

#36. Stop at 25
for i in range(1, 101):

    if i == 25:
        break

    print(i)

#37. First Number Divisible by Both 7 and 11
n = 1

while n <= 100:

    if n % 7 == 0 and n % 11 == 0:
        print(n)
        break

    n = n + 1

#38. Sum Until User Enters Zero
sum = 0

while True:
    n = int(input("Enter a number: "))

    if n == 0:
        break

    sum = sum + n

print("Final sum:", sum)

#39. Number Guessing Program
secret = 25

while True:
    guess = int(input("Guess the number: "))

    if guess > secret:
        print("Too High")

    elif guess < secret:
        print("Too Low")

    else:
        print("Correct Guess")
        break

#40. Count Numbers Divisible by 7
count = 0

for i in range(1, 201):

    if i % 7 == 0:
        count = count + 1

print("Count:", count)


#SECTION G — STRING, LIST, TUPLE, SET & DICTIONARY


#1. String Operations
name = input("Enter your name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title:", name.title())
print("Length:", len(name))
#2. Reverse a String
s = input("Enter a string: ")

print("Reverse:", s[::-1])
#3. Palindrome String
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
#4. Count Vowels
s = input("Enter a string: ")
count = 0

for i in s:
    if i in "aeiouAEIOU":
        count = count + 1

print("Number of vowels:", count)
#5. Find a Character
s = input("Enter a string: ")
ch = input("Enter a character: ")

if ch in s:
    print("Character is present")
else:
    print("Character is not present")
#6. List Number Analysis
l = [10, 20, 30, 40, 50]

print("Maximum:", max(l))
print("Minimum:", min(l))
print("Sum:", sum(l))
print("Length:", len(l))

#7. List Operations
l = [10, 30, 20, 40]

l.append(50)
print("After append:", l)

l.remove(20)
print("After remove:", l)

l.sort()
print("After sort:", l)

l.reverse()
print("After reverse:", l)

#8. Tuple Occurrence
t = (10, 20, 10, 30, 10, 40)

n = int(input("Enter value: "))

print("Occurrences:", t.count(n))

#9. Tuple Index
t = (10, 20, 30, 40, 50)

n = int(input("Enter value: "))

print("Index:", t.index(n))

#10. Set Operations
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))
print("Difference:", s1.difference(s2))
print("Symmetric Difference:", s1.symmetric_difference(s2))

#11. Remove From Set
s = {10, 20, 30, 40}

n = int(input("Enter value to remove: "))

s.discard(n)

print(s)

#12. Dictionary Operations
d = {
    "name": "Nikky",
    "age": 19,
    "course": "BCA"
}

# Add
d["city"] = "Hyderabad"

# Update
d["age"] = 20

# Remove
d.pop("city")

print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())


#SECTION H — COPY OPERATIONS
#1. General Copy / Assignment
l1 = [10, 20, 30]

l2 = l1

l2.append(40)

print("Original:", l1)
print("Copied:", l2)



#2. Shallow Copy
import copy

l1 = [[10, 20], [30, 40]]

l2 = copy.copy(l1)

l2[0].append(50)

print("Original:", l1)
print("Copied:", l2)


#3. Deep Copy
import copy

l1 = [[10, 20], [30, 40]]

l2 = copy.deepcopy(l1)

l2[0].append(50)

print("Original:", l1)
print("Copied:", l2)



