#USING BREAK STATEMENT
for i in range(1, 10):
    if i ==5:
        break

    print(i)
for i in range(1,10):
    if i ==7:
        break 
    print(i)

for i in range(1,6):
    if i ==3:
        break 
    print(i)

l = [10, 20, 30, 40,50]

for i in l:
    if i == 30:
        print("number found")
        break
else:
    print("not found")
    
ch = input("Enter a string:")
#WAP TO CHECH WHHER THE GIVEN CHARACTER EXIST INA STRING
for i in ch:
    if i == 'A':
        print("character found")
        break
else:
    print("character not found")
#WAP TO CHECH THE NUMBER CONTINUOUSLY UNTIL THE USER ENTERS ZZERO
while True:
    n = int(input("enter a num"))
    if n==0:
        break
    print(n)
#WRITE A PROGRAM TO CHECH THE CORRECT USERNAMER UNTIL THE USER ENTERS THE CORRECT ONE
while True:
    n = input("Enter your username:")

    if n =='Loshini123':
        break
    print("ERROR, ENTER CORRECT USWERNAME!")
#GUESSING THE NUMBER GAME
while True:
    print("IT'S A GUESS THE NUMBER GAME!")
    n = int(input("GUESS THE NUMBER: "))

    if n == 18:
        print("YAY! YOU GOT IT!")
        break

    elif n > 18:
        print("NAH! It's smaller than this buddy")

    elif n < 18:
        print("Umm, try to increase it")
#CHECKING THE CORRECT OTP GIVEN TO THE MOBILE NO.
import random
ph = int(input("enter your number:"))
while True:
    otp = random.randint(1000,9999)
    print("AN OTP HAS SENT TO YOUR",ph,'the otp is',otp)
    n = int(input("Enter your otp:"))
    if otp ==n:
        print("LOGGED IN")
        break
    else:
        print("Enter correct otp!")
#WAP TO WERE YOU HAVE TO WAIT 5 SECS AFTER 5 MIS TRAILS OF THE PIN
import time

opin = 3456
count = 0

while True:

    if count < 5:
        pin = int(input('enter the pin:'))
        count += 1

        if pin == opin:
            print("PHONE IS UNLOCKED")
            break
        else:
            print("Enter pin again!")

    if count == 5:
        print("You entered many times buddy, that too all wrong")
        print("NOW WAIT")

        time.sleep(5)
        count = 0
        
#WAP TO CHECK THE PRIME NUMBER
n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print("It's not a prime number")
        break
else:
    print("It's a prime number")

# WAP to check a given  character index in a string 
ch = input("ENTER A STRING:")

s = 'N'

for i in range(len(ch)):
    if ch[i] == s:
        print("Initial index:", i)
        break
else:
    print("N is not found")

ch = input("Enter a string: ")

for i in ch:
    if ord(i) < 97 or ord(i) > 122:
        print("Not all are lowercase")
        break
else:
    print("ALL ARE LOWER CASE")