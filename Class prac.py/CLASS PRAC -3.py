'''
num = int(input("enter the num:"))
if num%2 ==0:
    print("even")
else:
   print("odd")
'''
'''
ch = eval(input("Enter:"))
if type (ch) == float:
     print("Its float")
else:
    print("NOT FLOAT")

'''
'''
ch = input("Enter a character:")
if ch in ('a','e','i','o','u'):
   print("VOWEL")
else:
   print("No")
'''
'''
ch = input("enter :")
if ch == ch[::-1]:
    print("palindrome")
else:
        print("no")
'''
'''l= eval (input("Enter a list:"))
if len (l)%2 !=0:
    print("Has a middle value")
else:
    print("NO")'''
'''
val = int(input("enter your age:"))
if val>=18:
    print("Eligible")
else:
    ("NO")

a= int(input("enter a :"))
b= int(input("enter b :"))

if a>b:
     print("A is greater")
else:
    print("B is greater")

a= int(input("enter a :"))
b= int(input("enter b :"))

if a>b:
    print("A is greater than B")
elif a<b:
    print("B is greater than A")
else:
    print("Both are equal")


x = (int(input("enter x :")))
y = (int(input("enter y:")))

if x >=0 and y>=0:
    print("Its quadrant 1")
elif x<0 and y>=0:
        print("its qudrant 2")
elif x<0 and y<0:
        print("its qudrant 3")
else:
            print("Its quadrant 4:")

ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z':
    print("It's an uppercase")
elif ch >= 'a' and ch <= 'z':
    print("It's a lowercase")
elif ch >= '0' and ch <= '9':
    print("It's a digit")
else:
    print("Special character")


num = abs(int(input("Enter the number: ")))

if num < 10:
    print("1 digit number")
elif num < 100:
    print("2 digit number")
elif num < 1000:
    print("3 digit number")
else:
    print("More digits")
    '''
