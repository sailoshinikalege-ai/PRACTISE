
i = 1

while i <= 10:
    print(i)
    i = i + 2

    
i = 5

while i >= 5 and i <= 25:
    print(i)
    i = i + 5



i= int(input("enter a num"))
s =0
while s<=10:
    print(i ,'*' ,s, '=',i*s)
    s =s+1


num = int(input("Enter a number: "))

rev = 0

while num > 0:
    digit = num % 10
    rev = rev *10 +digit
    num =num//10

print(rev)


num = int(input('Enter a num'))

sum = 0

while num>0:
    digit = num%10
    sum = sum +digit
    num = num//10
print(sum)

n = int(input("Enter the num: "))
i = 1

while i <= n:
    if i % 5 == 0:
        print(i)
    i = i + 1
