'''
for i in range(1,11):
    if i ==6:
        continue
    print(i)

#WAP TO PRINT NUMBERS FROM 1 TO 20 BY SKIPPING THE NUMBER 5.
for i in range(1,21):
    if i ==5:
        continue
    print(i)
   
#WAP TO PRINT NUMBERS FROM 1 TO 10 BY SKIPPING ALL EVEN NUMBERS USING CONTINUE
for i in range(0,11):
    if i % 2 != 0:
        continue
    print(i)

#WAP TO PRINT NUMBERS FROM 1 TO 20 BY SKIPPING THE NUMBERS DIVISIBLE BY 5 
for i in range (1,21):
    if i%5 ==0:
        continue
    print(i)
#WAP TO PRINT ALL CHARACTERS OF A STRING EXCEPT VOWELS

ch = input("enter a string:")

for i in ch:
    if i in 'AEIOUaeiou':
        continue
    print(i)

 #WAP TO EXCTRACT EVERY CHARACTER FROM A STRING EXCEPY 'a'
ch = input("enter a string:")

for i in ch:
    if i == 'a':
        continue
    print(i)

#WAP TO PRINT ALL NUMBERS FROM A GIVEN LIST EXCEPT EVEN NUMBERS
l = [10,15,20,25,35]
for i in l:
    if i % 2 == 0:
        continue
    print(i)

#WAP TO EXTRACT ALL THE INTEGERS FROM GIVE LIST
l =[10,'HII',20,6.4,89,'python']
for i in l:
    if type(i)!= int:
        continue
    print(i)


#WAP TO EXTRACT ALL THE SPECIAL CHARACTERS FROM A GIVES STRING.
ch = input("Enter a string:")

for i in ch:
    if ('A' <= i <= 'Z') or ('a' <= i <= 'z') or i in '0123456789':
        continue
print(i)
#WAP TO PRINT 1 TO 10 BY SKIPPING 3 AND 8 (WHILE LOOP)
i = 1

while i <= 10:
    if i == 3 or i == 8:
        i = i + 1
        continue

    print(i)
    i = i + 1
'''

