
#🟢 Slicing – Practice Questions
#Given s = "PYTHON", print the first 3 characters.
print("QUESTION :Given s = PYTHON, print the first 3 characters.")
s = "PYTHON"
print ( s[:3:])

#Given s = "COMPUTER", print the last 4 characters.
print("QUESTION:Given s = COMPUTER, print the last 4 characters.")
S='COMPUTER'
print (S [-4:])

#Given a = "PROGRAM", print the characters from index 2 to 5.
print("Question:Given a = PROGRAM, print the characters from index 2 to 5.")
a ='PROGRAM'
print(a[2:6:])

#Given v = "NOTEBOOK", print the string in reverse.
print("QUESTION:Given v = NOTEBOOK, print the string in reverse.")
v ='NOTEBOOK'
print(v[::-1])

#Given k = "CHOCOLATE", print every second character.
print("QUESTION:Given k = CHOCOLATE, print every second character.")
k = 'CHOCOLATE'
print(k[::2])

#Given l = "PYTHON", print the characters at odd indexes.
print("QUESTION:Given l = PYTHON, print the characters at odd indexes.")
l = 'PYTHON'
print(l[1::2])

#Given p = "PROGRAMMING", print the characters at even indexes.
print("QUESTION:Given p = PROGRAMMING, print the characters at even indexes.")
p ='PROGRAMMING'
print(p [::2])

#Given x = "COMPUTER", print the last 3 characters in reverse.
print("QUESTION:Given x = COMPUTER, print the last 3 characters in reverse.")
x ='COMPUTER'
print(x[:-4:-1])
#Given y = "NOTEBOOK", print everything except the last 2 characters.
print("QUESTION:Given y = NOTEBOOK, print everything except the last 2 characters.")
y ='NOTEBOOK'
print(y[:-2])

#Given z = "PYTHONPROGRAM", print characters from index 3 to index 9.
print("QUESTION:Given z = PYTHONPROGRAM, print characters from index 3 to index 9.")
z='PYTHONPROGRAM'
print(z[3:10:])


#🟡 Control Statements – Practice Questions
#Write a program to check whether a number is positive, negative, or zero.
x = int(input("Enter x:"))
if x <0:
    print("NEGATIVE")
elif x==0:
    print("ZERO")
elif x>=0:
    print("POSITIVE")
else:
    print("MAYBE COMPLEX")
    
#Write a program to check whether a number is even or odd.
y = int(input("Enter a num:"))
if y%2 ==0:
    print("EVEN")
else:
    print("ODD")
    
#Write a program to find the greatest among 3 numbers.
a= int(input("ENTER A:"))
b= int(input("ENTER B:"))
c= int(input("ENTER C:"))

if a >b and a >c:
    print(a, " is greatest num")
elif b>a and b>c:
    print(b," is greatest num")
else:
    print(c,"is greatest num")
    
#Write a program to find the smallest among 3 numbers.
A= int(input("ENTER A:"))
B= int(input("ENTER B:"))
C= int(input("ENTER C:"))

if A <B and A <C:
    print(A, " is smallest num")
elif B>A and B>C:
    print(B," is greatest num")
else:
    print(C,"is greatest num")
  
#Write a program to check whether a person is eligible to vote.
age = int(input('ENTER YOUR AGE: '))
if age >= 18:
    print("YOU ARE ELIGIBLE")
else:
    print("NOT ELIGIBLE")
    
#Write a program to check whether a number is divisible by both 5 and 10.
div = int(input("ENTER A NUM:"))
if div % 5== 0 and div% 10==0:
    print("DIVISIBLE BY BOTH 5 AND 10")
else:
    print("NOT DIVISIBLE")
    
#Write a program to check whether a character is a vowel or consonant.
ch = input("ENTER A CHARACTER:")
if ch in 'aeiouAEIOU':
    print("VOWELS")
else:
    print("CONSONANT")
    
#Write a program to check whether a number is a single-digit, two-digit, or three-digit number.
num = int(input("Enter a number:"))
if num >=0 and num <= 9:
    print("SINGLE DIGIT")
elif num >=10 and num <=99 :
    print("DOUBLE DIGIT")
elif num>=100 and num<=999:
    print("THREE DIGIT")
else:
    print("NONE")
    
#Write a program to check whether a given year is a leap year.
year = int(input("Enter the year:"))
if year % 4 ==0:
    print("LEAP YEAR")
else:
    print("NOT a leap year")
#🔴 Slicing + Control Statements
    
#Take a string as input and check whether its first and last characters are the same.
v = input("ENTER A STRING:")

if v [0] == v[-1]:
   print("FIRST AND LAST CHARACTER ARE SAME")
else:
    print("NOT SAME")
    
#Take a string as input and check whether it is a palindrome using slicing.
palindrome = input("ENTER A STRING:")

if palindrome [::1] == palindrome [::-1]:
    print("Its an palindrome string")
else:
    print("Not an palindrome")
#Take a string as input. If its length is at least 5, print its first 5 characters; otherwise print "Too short".
ch = input("Enter a string:")
if len(ch ) >= 5:
    print(ch [:5])
else:
    print("TOO SHORT")
    
#Take a string as input and check whether its first 3 characters are "www".
x = input("Enter a string:")
if x [:3] == 'www':
     print("ITS CORRECT URL")
else:
    print("INCORRECT")
    
#Take a username as input. If its length is between 5 and 10 characters, print "Valid"; otherwise print "Invalid".
user = input("Enter your username:")
if len (user) >= 5 and len (user) <=10:
    print("VALID")
else:
    print("NOT VALID")
    
#Take a word as input and print its first half using slicing. If its length is less than 4, print "Too short".
word = input("Enter a word: ")

if len(word) < 4:
    print("Too short")
else:
    print(word[:len(word)//2])

#Take a string as input and check whether the last 3 characters are "ing".
t = input ("A STRING:")
if t [-3:] == 'ing':
    print("CORRECT", t [-3:])
else:
    print("INCORRECT",t [-3:])
    
#Take a string as input. If its length is greater than 6, print the first 3 and last 3 characters.
g = input("Enter a string:")
if len(g) >6:
    print(g [:3] , g [-3:])
else:
    print("Wrong lenght")
#Take a word as input and check whether the first character is a vowel.
che= input("Enter a string:")
if che[0] in 'AEIOUaeiou':
    print("first character is a vowel.")
else:
    print("NOT A VOWEL")
    
#Take a string as input and check whether the string remains the same when reversed.''
rev= input("Enter a string")
if rev == rev[::-1]:
    print("REVERSE IS SAME")
else:
    print("NOT SAME IN REVERSE")
