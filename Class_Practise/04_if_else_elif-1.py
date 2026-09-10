'''num = abs(int(input("Enter the number: ")))
if num < 10:
   print("1 digit number")
elif num < 100:
    print("2 digit number")
elif num < 1000:
    print("3 digit number")
else: print("More digits") 

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
d=int(input("Enter d:"))

if a>b and a>c and a>d:
    print("A is greater ")
elif b>a and b>c and b>d:
    print("B is greater ")
elif c>a and c>b and c>d:
    print("C is greater ")
else:
    print("SD is greater")

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
d=int(input("Enter d:"))

if a <b and a<c and a<d:
    print("A is smaller")
elif  b<a and b<c and b<d:
    print("B is smaller")
elif c<a and c<b and c<d:
    print("C is smaller")
else:
    print("D is smaller")
    

x = int(input("Enter a num:"))

if x % 3==0 and x%5==0:
    print("FIZZBUZZ")
    
elif x%5 == 0:
 print("BUZZ")

elif x % 3==0:
  print("FIZZBUZZ")

marks = float (input("Enter your marks:"))
if marks >= 90:
     print("A grade")
elif marks >=80 and marks<90:
    print("B grade")
elif marks >=60 and marks<80:
    print("C grade")
elif marks >=45 and marks<60:
    print("D grade")
else:
    print("F grade")


x = int(input("Enter 1st digit: "))
y = int(input("Enter 2nd digit: "))
z = int(input("Enter 3rd digit: "))

if x > y:
    if x > z:
        print("1st is greater")
    else:
        print("3rd is greater")
else:
    if y > z:
        print("2nd is greater")
    else:
        print("3rd is greater")

        '''

print("WELCOME TO INSTAGRAM")

name = input("Enter your username: ")
psw = input("Enter your password: ")

if name == 'loshini@123':
    if psw == '12345':
        print("You are logged in")
    else:
        print("Wrong password")
else:
    print("Wrong username")



