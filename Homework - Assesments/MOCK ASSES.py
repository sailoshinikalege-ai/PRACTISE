'''
#109. Write a program to input your name and age and display both.
name = input('Enter your name:')
age = int(input('enter your age:'))
print(name,age)

#110. Write a program to input two numbers and display their sum.
a = int(input('enter a:'))
b = int(input('enter b:'))
print('sum=',a+b)

#111. Write a program to input two numbers and display:
#- Sum
#- Difference
#- Product
#- Division
# Floor Division
#- Remainder
a = int(input('enter a:'))
b = int(input('enter b:'))
print('sum=',a+b)
print('difference:',a-b)
print('product:',a*b)
print('divison:',a/b)
print('floor division:',a//b)

#112. Write a program to input the radius of a circle and calculate its area.
r = int(input('Enter the radius'))
area = 2* 3.14 *r
print('Area of circle:',area)

#113. Write a program to input a number using eval() and print its square.
sq = eval(input('enter the num:'))
print(sq**2)

#114. Write a program to input three numbers and display their average.
a = int(input('enter a:'))
b = int(input('enter b:'))
c = int(input('enter c:'))

print ((a+b+c)/2)

#115. Write a program to input marks of five subjects and calculate totaland percentage.
math = int(input('enter marks of maths:'))
phy = int(input('enter marks of physics:'))
bio = int(input('enter marsks of bilogy:'))
chem = int(input('enter marks of chemistry:'))
eng = int(input('enter marks of english:'))

total = math+chem+phy+eng+bio
per = (total/500)*100

print('Total :',total)
print('Percentage:',per)

#116. Write a program using print() with sep="-" to display:
#2026
#09
#09
print(2026, 9, 9, sep="-")


#117. Write a program using print() with end=" " to print:
#Hello World
print('Hello World',end = " ")


#SECTION 2 — CONDITIONAL STATEMENTS

#118. Write a program to check whether a number is positive, negative, or zero.
num = int(input('Enter the number:'))

if num>0:
    print('positive')
elif num<0:
    print('negative')
elif num ==0:
    print('zero')

'''
#119. Write a program to check whether a number is even or odd.
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#120. Write a program to check whether a person is eligible to vote.
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


#121. Write a program to find the largest of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)

#122. Write a program to find the largest of three numbers using if-elif-else.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

#123. Write a program to find the smallest of three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest:", a)
elif b <= a and b <= c:
    print("Smallest:", b)
else:
    print("Smallest:", c)

#124. Write a program to check whether a year is a leap year.
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

#125. Write a program to check whether a number is divisible by both 5 and 11.
n = int(input("Enter number: "))

if n % 5 == 0 and n % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both")

#126. Write a program to input marks and display:

#90-100  → A
#75-89   → B
#60-74   → C
#40-59   → D
#Below 40 → Fail

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

#127. Write a program using nested if to check:

#Age below 18 → Minor
#18-59       → Adult
#60 or above → Senior Citizen

age = int(input("Enter age: "))

if age < 18:
    print("Minor")
else:
    if age < 60:
        print("Adult")
    else:
        print("Senior Citizen")



#SECTION 3 — FOR LOOP & RANGE()

#128. Write a program to print numbers from 1 to 10.

for i in range(1, 11):
    print(i)

#129. Write a program to print numbers from 10 to 1.
for i in range(10, 0, -1):
    print(i)

#130. Write a program to print even numbers from 1 to 50.
for i in range(2, 51, 2):
    print(i)

#131. Write a program to print odd numbers from 1 to 50.
for i in range(1, 51, 2):
    print(i)

#132. Write a program to print multiples of 5 from 5 to 50.
for i in range(5, 51, 5):
    print(i)

#133. Write a program to print the multiplication table of a given number.
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)

#134. Write a program to find the sum of numbers from 1 to n.
n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)

#135. Write a program to find the sum of all even numbers from 1 to n.
n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1, 2):
    total = total + i

print("Sum:", total)

#136. Write a program to find the sum of all odd numbers from 1 to n.
n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1, 2):
    total = total + i

print("Sum:", total)

#137. Write a program to print numbers from n to 1 using range().
n = int(input("Enter n: "))

for i in range(n, 0, -1):
    print(i)


#SECTION 4 — WHILE LOOP

#138. Write a program to print numbers from 1 to 10 using while loop.
i = 1

while i <= 10:
    print(i)
    i = i + 1

#139. Write a program to print numbers from 10 to 1 using while loop.
i = 10

while i >= 1:
    print(i)
    i = i - 1

#140. Write a program to find the sum of numbers from 1 to n using while loop.
n = int(input("Enter n: "))

i = 1
total = 0

while i <= n:
    total = total + i
    i = i + 1

print(total)

#141. Write a program to count the number of digits in a number.
n = int(input("Enter number: "))

count = 0

while n > 0:
    n = n // 10
    count = count + 1

print("Number of digits:", count)

#142. Write a program to find the sum of digits of a number.
n = int(input("Enter number: "))

total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum:", total)

#143. Write a program to reverse a number.
n = int(input("Enter number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse:", rev)

#144. Write a program to check whether a number is a palindrome.
n = int(input("Enter number: "))

original = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#145. Write a program to find the factorial of a number using while loop.
n = int(input("Enter number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial:", fact)

#146. Write a program to check whether a number is prime using a loop.
n = int(input("Enter number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")

#147. Write a program to print the Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

#
#SECTION 5 — NESTED LOOPS / PATTERNS
#
'''
148. Write a program to print:

*
**
***
****
*****

'''
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

'''
149. Write a program to print:

*****
****
***
**
*
'''
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

'''
150. Write a program to print:

1
12
123
1234
12345
'''
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

'''
151. Write a program to print:

1
22
333
4444
55555
'''

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()
'''
152. Write a program to print:

*****
*****
*****
*****
*****
'''
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

'''
'''

#SECTION 6 — INTERMEDIATE PROGRAMS


#153. Write a program to find the largest digit of a number.
n = int(input("Enter number: "))

largest = 0

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    n = n // 10

print("Largest digit:", largest)

#154. Write a program to find the smallest digit of a number.

n = int(input("Enter number: "))

smallest = 9

while n > 0:
    digit = n % 10

    if digit < smallest:
        smallest = digit

    n = n // 10

print("Smallest digit:", smallest)

#155. Write a program to count the number of even and odd digits in a number.
n = int(input("Enter number: "))

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

#156. Write a program to check whether a number is an Armstrong number.
n = int(input("Enter number: "))

original = n
count = 0

while n > 0:
    count = count + 1
    n = n // 10

n = original
total = 0

while n > 0:
    digit = n % 10
    total = total + digit ** count
    n = n // 10

if total == original:
    print("Armstrong")
else:
    print("Not Armstrong")

#157. Write a program to print Armstrong numbers between 1 and 1000.
for n in range(1, 1001):

    original = n
    count = 0
    temp = n

    while temp > 0:
        count = count + 1
        temp = temp // 10

    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** count
        temp = temp // 10

    if total == original:
        print(original)

#158. Write a program to check whether a number is a perfect number.
n = int(input("Enter number: "))

total = 0

for i in range(1, n):
    if n % i == 0:
        total = total + i

if total == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")

#159. Write a program to print perfect numbers between 1 and 1000.
for n in range(1, 1001):

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total = total + i

    if total == n:
        print(n)

#160. Write a program to find the GCD of two numbers using loops.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD:", gcd)

#161. Write a program to find the LCM of two numbers using loops.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    lcm = a
else:
    lcm = b

while True:
    if lcm % a == 0 and lcm % b == 0:
        break

    lcm = lcm + 1

print("LCM:", lcm)

#162. Write a program to print all prime numbers between 1 and 100.
for n in range(2, 101):

    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        print(n)

#163. Write a program to find the sum of the digits that are even in a given number.
n = int(input("Enter number: "))

total = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        total = total + digit

    n = n // 10

print("Sum:", total)

#164. Write a program to count how many digits of a number are divisibleby 3.
n = int(input("Enter number: "))

count = 0

while n > 0:
    digit = n % 10

    if digit % 3 == 0:
        count = count + 1

    n = n // 10

print("Count:", count)


#SECTION 7 — BREAK


#165. Write a program to print numbers from 1 to 20 and stop at 10using break.
for i in range(1, 21):

    if i == 11:
        break

    print(i)

#166. Write a program to repeatedly input numbers and stop when theuser enters 0.
while True:

    n = int(input("Enter number: "))

    if n == 0:
        break

    print(n)

#167. Write a program to search for a number in a list and stop whenthe number is found using break.
numbers = [10, 20, 30, 40, 50]

search = int(input("Enter number to search: "))

for i in numbers:

    if i == search:
        print("Number found")
        break

#168. Write a program to find the first number divisible by 7 between1 and 100 using break.
for i in range(1, 101):

    if i % 7 == 0:
        print(i)
        break


#SECTION 8 — CONTINUE

#169. Write a program to print numbers from 1 to 20 but skip even numbers using continue.
for i in range(1, 21):

    if i % 2 == 0:
        continue

    print(i)

#170. Write a program to print numbers from 1 to 20 but skip 5, 10, and 15 using continue.
for i in range(1, 21):

    if i == 5 or i == 10 or i == 15:
        continue

    print(i)

#171. Write a program to print only odd numbers from 1 to 50 using continue.
for i in range(1, 51):

    if i % 2 == 0:
        continue

    print(i)


#SECTION 9 — PASS


#172. Write a program using pass inside an if statement.
n = int(input("Enter number: "))

if n > 0:
    pass
else:
    print("Negative or zero")

#173. Write a program using pass inside a for loop.
for i in range(1, 6):

    if i == 3:
        pass

    print(i)

#174. Write a program using pass inside a while loop.
i = 1

while i <= 5:

    if i == 3:
        pass

    print(i)
    i = i + 1