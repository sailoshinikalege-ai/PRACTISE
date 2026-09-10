
i =2
sum = 0

while i <=50:
    if i %2 ==0:
     sum = sum + i
    i  =i+1
print(sum)


ch = input("STRING:")
i = 0

while i < len(ch):
    print(ch[i])
    i = i + 1

num = int(input("Enter the num:"))
rev = 0

while num>0:
    digit = num%10
    rev = rev*10 + digit
    num = num//10

print(rev,"is the reverse of the number")

n = int(input("enter the num:"))
i = 0
sum =0
while i<=n:
    sum = sum +i
    i = i+1
print(sum,"is the sum of the numbers from 1 to",n)

n = int(input("enter a num"))
i =0

while n>0:
    digit = n%10
    i = i+1
    n = n//10

print(i,"is the number of digits in the number")

num = int(input("Enter the num: "))

i = 1
fac = 1

while i <= num:
    fac = fac * i
    i = i + 1

print(fac,"is the factorial of the number")


num = int(input("enter a num:"))
i = 2
count =0

while i<num:
    if num%i==0:
       count = count+1
    i = i+1

if count ==0:
    print("prime num")
else:
    print("not a prime num")

n = int(input("Enter how many terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a)
    
    c = a + b
    a = b
    b = c
    
    i = i + 1


num = int(input("enter the num"))

i =0
mul=1

while num>0:
    digit = num%10
    if digit %2==0:
          mul = mul*digit
    num = num//10
    i = i+1
print(mul,"is the product of even digits in the number")
  

t = eval(input("enter a tuple"))
i =1
mul=1
while i <len(t):
    if isinstance(t[i], float):
        mul =mul * t[i]
    i = i+1
print(mul,"is the product of float values in the tuple")
    
