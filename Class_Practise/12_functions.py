'''
def pali(l):
    out=[]
    for i in l:
        if type (i) == str:
            if i == i[::-1]:
                out. append(i)
    print(out)
pali ([10, 'ab', 76])

#WAP TO FIND THE GREATES NUM AMONG THE 3 

def gr(a, b, c):
    if a > b and a > c:
        print("A is greatest")
    elif b > a and b > c:
        print("B is greatest")
    else:
        print("C is greatest")


gr(10, 20, 30)

#WAP TO CONCATINATE TWO LISTS COLLECTION WITHOUT USING + OPERATOR

def con(m, n):
    out = []

    for i in m:
        out.append(i)

    for i in n:
        out.append(i)

    print(out)

con([1, 2, 3], [4, 5, 6])

#WAP  TO FIND THE SUM OF ALL THE INTEGERE PRESENT IN A GIVEN SE4T.
def l():
    s = eval(input("enter the set:"))
    total =0
    for i in s :
        if type(i) == int:
            total = total +i
            return total
print(sum())

#WAP TO FIND THE FACTORIAL OF A NUMBER
def fac():
    n = int(input("Enter the number:"))
    i = 1
    mul = 1

    while n > 0:
        mul = mul * n
        n = n - 1

    return mul

print(fac())

#  WAP TO FIND THE SUM OF DIGITS

def sum():
    n = int(input("Enter the number:"))
    
    digi = 0

    while n > 0:
        digit = n % 10
        digi = digit + digi
        n = n // 10

    return digi

print(sum())

#WAP TO FIND GRETEST AMONG THREE

def gr():
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = int(input("Enter c:"))
    if a > b and a> c:
        print("A is the grestes")
    elif b >c and b >a:
        print("B is the greates")
    else:
        print("C is the gretest")

    return (a,b,c)
print(gr())

#WAP TO CHECK WHETHER THE NUMBER IS POSITIVE , NEGATIVE OR ZERO

def check():
    a = int(input("enter a num:"))

    if a > 0 :
        print('POSITIVE')
    elif a<0:
        print('NEGATIVE')
    else:
        print('ZERO')

    return a
print(check())

#WAP TO PRINT THE INTIAL INDEX OF A CHARCARTER IN A GIVEN STRING
# STRING : PROGRAMMING
#CHARCATER : M

def i(ch):
    for x in range(len(ch)):
        if ch[x] == 'M':
            print("Initial index of M is:", x)
            break

ch = input("Enter a string:")
i(ch)
'''
#WAP TO MAP TWO LIST COLLECTIONS IN THYE FORM OF DICTIONARY
#L1=['A', 'B', 'C']
#L2 =[10,20,30]


#WAP TO EXTRACT ALL THE NEGATIVE NUMBERS FROM A LIST

def ex(a):
    out = []

    for i in a:
        if i < 0:
            out.append(i)

    return out

a = eval(input("Enter a list:"))
print(ex(a))

#WAP TO COUNT THE DIGITS

def count (a):
    i = 0
    count = 0

    while a >0:
        digit = a %10
        count=count +i
        a = a //10

        count = count +1
def arm(m):
    original = m
    total = 0

    while m > 0:
        digit = m % 10
        cube = digit * digit * digit
        total = total + cube
        m = m // 10

    if total == original:
        return "Armstrong number"
    else:
        return "Not an Armstrong number"


m = int(input("Enter a number: "))
print(arm(m))

        


