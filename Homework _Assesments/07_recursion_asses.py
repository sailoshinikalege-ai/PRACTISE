'''
def fun(n):
    if n == 0:
        return 0
    return n + fun(n-1)

print(fun(4))

def fun(n):
    if n == 0:
        return 1
    return n * fun(n-1)

print(fun(4))

def print_num(n):
    if n == 0:
        return

    print_num(n - 1)
    print(n)

n = int(input("Enter N: "))
print_num(n)

def fun(n):
    if n ==0:
        return
    print(n)
    fun(n-1)
n = int(input("enter the num:"))
fun(n)

def even(n):
    if n == 0:
        return

    even(n - 1)

    if n % 2 == 0:
        print(n)

even(6)

def odd(n):
    if n ==0:
        return

    odd(n-1)

    if n%2 !=0:
        print(n)
n = int(input('enter the num'))
odd(n)

def sum(n):
    if n == 0:
        return 0

    return n + sum(n - 1)

n = int(input("Enter the num: "))
print("Sum =", sum(n))

def fac(n):
    if n==1:
        return 1
    return n * fac(n-1)
n = int(input('enter the num:'))
print(fac(n))

def power(a,n):
    if n ==0:
        return 1
    return a * power(a,n-1)
a = int(input('enter the num:'))
n =int(input('enter the power:'))
print(power(a,n))

def sum(n):
    if n ==0:
        return 0

    if n %2 ==0:
        return n + sum(n-1)
    else:
        return sum (n-1)
n = int(input('enter the num:'))
print(sum(n))

def sum(n):
    if n ==0:
        return 0

    if n %2 !=0:
        return n + sum(n-1)
    else:
        return sum (n-1)
n = int(input('enter the num:'))
print(sum(n))

def sum(n, i):
    if i == 11:
        return

    print( n *i )
    sum( n,i+1)

n = int(input("Enter the num: "))
sum( n,1)

#31. WAP to find the sum of numbers from 1 to N using a WHILE loop. Convert the same program into recursion.
#WHILE LOOP:
n = int(input('enter the num:'))
i =0
sum =0

while i <=n:
    sum = sum+i
    i = i+1
print(sum)

#INTO RECURSION:

def sum(n):
    if n ==0:
        return 0
    return n + sum(n-1)
n = int(input('enter the num:'))
print(sum(n)

#32. WAP to find the sum of numbers from 1 to N using a FOR loop. Convert the same program into recursion.
#FOR LOOP:
n = int(input('enter the num:'))
sum =0
for i in range (1, n+1):
  sum = sum+i
  i = i+1
print(sum)

#INTO RECURSION:

def sum(n):
    if n ==0:
        return 0
    return n + sum(n-1)
n = int(input('enter the num:'))
print(sum(n))

#33. WAP to find the sum of squares from 1 to N using a WHILE loop. Convert the same program into recursion.
#WHILE LOOP:
n = int(input('enter the num:'))
i=0
sq=1
while i<=n:
   sq= sq+i**2
   i = i+1
print(sq)

#INTO RECURSION:
def power(n):
    if n == 0:
        return 0

    return n**2 + power(n-1)
n = int(input('enter the num:'))
print(power(n))

#34. WAP to find the sum of squares from 1 to N using a FOR loop. Convert the same program into recursion.
#FOR LOOP:
n = int(input('enter the num:'))
sq =0
for i in range (1,n+1):
     sq = sq+ i**2
print(sq)

#INTO RECURSION:
def power(n):
    if n == 0:
        return 0

    return n**2 + power(n-1)
n = int(input('enter the num:'))
print(power(n))

#35. WAP to find the sum of cubes from 1 to N using a WHILE loop. Convert the same program into recursion.
#WHILE LOOP:
n = int(input('enter the num:'))
i = 0
cube =0
while i <=n:
    cube = cube+ i**3
    i = i+1
print(cube)

#RECURSION :

def cube(n):
    if n ==0:
        return 0
    return n**3 + cube(n-1)
n = int(input('enter the num:'))
print(cube(n))

#36. WAP to find the sum of cubes from 1 to N using a FOR loop. Convert the same program into recursion.
#FOR LOOP:

n = int(input('enter the num:'))
cube =0
for i in range(1,n+1):
    cube = cube+i**3
print(cube)

#RECURSION:
def cube(n):
    if n ==0:
        return 0
    return n**3 + cube(n-1)
n = int(input('enter the num:'))
print(cube(n))

#37. WAP to count the number of digits in a number using a WHILE loop. Convert the same program into recursion.
#WHILE LOOP:
n = int(input("enter the digit:"))

count =0

while n>0:
    digit = n % 10
    count = count+1
    n = n//10
print(count)

#RECURSION:

def count(n):
    if n == 0:
        return 0
    return 1 + count(n // 10)
n = int(input("Enter the num:"))
print(count(n))

#38. WAP to find the sum of digits of a number using a WHILE loop. Convert the same program into recursion.
#WHILE LOOP:

n = int(input('enter the digits:'))

sum =0

while n>0:
    digit = n %10
    sum = digit +sum
    n = n//10
print(sum)

#RECURSION:

def sum(n):
    if n==0:
        return 0
    return n%10 +sum(n//10)
n = int(input('enter the digit:'))
print(sum(n))

#39. WAP to find the product of digits of a number using a WHILE loop. Convert the same program into recursion.
#WHILE LOOP:

n = int(input('enter the digits:'))

mul =1

while n>0:
    digit = n %10
    mul = digit*mul
    n = n//10
print(mul)

#RECURSION:

def mul(n):
    if n==0:
        return 1
    return n%10 *mul(n//10)
n = int(input('enter the digit:'))
print(mul(n))

'''
#40. WAP to find the reverse of a number using a WHILE loop. Convert the same program into recursion.
#WHILE LOOP:

n = int(input('enter the digits:'))

rev =0
while n>0:
    digit = n %10
    rev= rev *10 +digit 
    n = n//10
print(rev)

#RECURSION:

def rev(n, r):
    if n == 0:
        return r

    return rev(n // 10, r * 10 + n % 10)

#41. WAP to print the multiplication table of a number using recursion.

def table(n, i):
    if i == 11:
        return

    print(n, "*", i, "=", n*i)
    table(n, i+1)

n = int(input("Enter the num:"))
table(n, 1)


#42. WAP to print numbers from N to 1 using recursion.

def numbers(n):
    if n == 0:
        return

    print(n)
    numbers(n-1)

n = int(input("Enter the num:"))
numbers(n)


#43. WAP to print numbers from 1 to N using recursion.

def numbers(n, i):
    if i > n:
        return

    print(i)
    numbers(n, i+1)

n = int(input("Enter the num:"))
numbers(n, 1)


#44. WAP to count even numbers from 1 to N using recursion.

def even(n):
    if n == 0:
        return 0

    if n % 2 == 0:
        return 1 + even(n-1)

    return even(n-1)

n = int(input("Enter the num:"))
print(even(n))


#45. WAP to count odd numbers from 1 to N using recursion.

def odd(n):
    if n == 0:
        return 0

    if n % 2 != 0:
        return 1 + odd(n-1)

    return odd(n-1)

n = int(input("Enter the num:"))
print(odd(n))


#46. WAP to find the largest digit in a number using recursion.

def largest(n):
    if n == 0:
        return 0

    digit = n % 10
    large = largest(n//10)

    if digit > large:
        return digit

    return large

n = int(input("Enter the num:"))
print(largest(n))


#47. WAP to extract all lowercase characters from the given string using recursion.

def lower(s, i):
    if i == len(s):
        return ""

    if s[i].islower():
        return s[i] + lower(s, i+1)

    return lower(s, i+1)

s = input("Enter the string:")
print(lower(s, 0))


#48. WAP to print numbers from N to 1 using recursion.

def numbers(n):
    if n == 0:
        return

    print(n)
    numbers(n-1)

n = int(input("Enter the num:"))
numbers(n)


#49. WAP to find the sum of digits of a number using recursion.

def sum(n):
    if n == 0:
        return 0

    return n%10 + sum(n//10)

n = int(input("Enter the num:"))
print(sum(n))


#50. WAP to print the following output using recursion.
#32123

def pattern(n):
    if n == 0:
        return

    print(n, end="")
    pattern(n-1)
    print(n, end="")

pattern(3)


#51. WAP to print the following output using recursion.
#543212345

def pattern(n):
    if n == 0:
        return

    print(n, end="")
    pattern(n-1)
    print(n, end="")

pattern(5)


#52. WAP to find the sum of all the integers present in a given list using recursion.
#Condition: Consider only integer values.

l = [10, 12, 8+9j, [12, 4, 9.8], [1, 3, [6, 8+3j]]]

def sum_list(l, i):
    if i == len(l):
        return 0

    if type(l[i]) == int:
        return l[i] + sum_list(l, i+1)

    return sum_list(l, i+1)

print(sum_list(l, 0))


#53. WAP to generate the following output using recursion.

#Input:
#l = ['hai', 56, 7+8j, 45, 8.7, 'data']

#Output:
#['iahhai', 56, 7+8j, 45, 8.7, 'attddata']

l = ['hai', 56, 7+8j, 45, 8.7, 'data']

def reverse(s):
    if s == "":
        return ""

    return reverse(s[1:]) + s[0]

def modify(l, i):
    if i == len(l):
        return

    if type(l[i]) == str:
        l[i] = reverse(l[i]) + l[i]

    modify(l, i+1)

modify(l, 0)
print(l)


#54. WAP to check whether a number is palindrome or not using recursion.

def reverse(n, rev):
    if n == 0:
        return rev

    return reverse(n//10, rev*10 + n%10)

n = int(input("Enter the num:"))

if n == reverse(n, 0):
    print("Palindrome")
else:
    print("Not Palindrome")


#55. WAP to check whether a number is prime or not using recursion.

def prime(n, i):
    if i == 1:
        return True

    if n % i == 0:
        return False

    return prime(n, i-1)

n = int(input("Enter the num:"))

if n <= 1:
    print("Not Prime")
elif prime(n, n-1):
    print("Prime")
else:
    print("Not Prime")


#56. WAP to find the GCD/HCF of two numbers using recursion.

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a%b)

a = int(input("Enter the first num:"))
b = int(input("Enter the second num:"))

print(gcd(a, b))


#57. WAP to find the LCM of two numbers using recursion.

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a%b)

a = int(input("Enter the first num:"))
b = int(input("Enter the second num:"))

lcm = (a*b)//gcd(a,b)

print(lcm)


#58. WAP to find the nth Fibonacci number using recursion.

def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

n = int(input("Enter the num:"))
print(fib(n))


#59. WAP to print the first N Fibonacci numbers using recursion.

def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

def print_fib(n, i):
    if i == n:
        return

    print(fib(i), end=" ")
    print_fib(n, i+1)

n = int(input("Enter N:"))
print_fib(n, 0)


#60. WAP to find the largest digit in a number using recursion.

def largest(n):
    if n == 0:
        return 0

    digit = n%10
    large = largest(n//10)

    if digit > large:
        return digit

    return large

n = int(input("Enter the num:"))
print(largest(n))


#61. WAP to find the smallest digit in a number using recursion.

def smallest(n):
    if n < 10:
        return n

    digit = n%10
    small = smallest(n//10)

    if digit < small:
        return digit

    return small

n = int(input("Enter the num:"))
print(smallest(n))


#62. WAP to count the number of even digits present in a number using recursion.

def even(n):
    if n == 0:
        return 0

    digit = n%10

    if digit % 2 == 0:
        return 1 + even(n//10)

    return even(n//10)

n = int(input("Enter the num:"))
print(even(n))


#63. WAP to count the number of odd digits present in a number using recursion.

def odd(n):
    if n == 0:
        return 0

    digit = n%10

    if digit % 2 != 0:
        return 1 + odd(n//10)

    return odd(n//10)

n = int(input("Enter the num:"))
print(odd(n))

#




