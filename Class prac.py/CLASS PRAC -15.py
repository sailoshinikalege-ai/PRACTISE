#PASSING DEFAULT VALUES

def reg(name, phno,email,altphno = None , altmail =''):
    print('Name is:',name)
    print('Phone no is:',phno)
    print('Email  is:',email)
    print('Alternative number is:',altphno)
    print('Alternative email is:',altmail)
reg ('NIKKY',8186864545,'nikky@gmail.com')

    
   
#WAP TO FIND THE PRODUCT OF MIN 3 NUMBER AND MAX 5 NUMBER

def pro(a, b, c, d=1, e=1):
    return a * b * c * d * e

print(pro(1, 2, 3))
 
#WAP TO EXTRACT FLOAT NUMBERS FROM THE TUPLE COLLECTION

def fl(a):
    for i in a:
        if type(i) == float:
            print(i)

fl((9.6, 'hello', 70, 8.9))

def fl(a, b=0):
    for i in a:
        if type(i) == float:
            print(i)

fl((9.6, 'hello', 70, 8.9))

def fl (t,out=()):
    for i in t:
        if type (i)==float:
            out+=(i,)
    return out
print(fl((1.2,'hello',3.4)))

#POSITIONAL ARGS

def add(a,b):
    print(a+b)
add(3,2)

#WAP TO FIND THE COMMON ELEMENTS BETWEEN TWO LISTS

# POSITIONAL ARGUMENTS

def common(a, b):
    out = ()

    for i in a:
        for j in b:
            if i == j:
                out += (i,)

    return out

print(common((1,2,3,4,5,6), (1,3,5,7,9,0)))


#

def add(a,b,c,d,e,f=0,g=0):
    return a+b+c+d+e+f+g
print(add(1,2,3,4,5,6))

#WAP TO CALCULATE THE POWER OF A NUMBER WERE THE DEFUALT POWER IS 2


def power(a, b=2):
    return a ** b

print(power(5))

#WAP TO CALCULATE THE TOTAL SALARY OF AN EMPLOYEE WERE THE BONUS HAS A DEFUALT VALUE OF ATLEAST 5000

def emp(sal,bonus=5000):
    return sal +bonus
print(emp(20000))

#WAP TO TAKE NAME, SALARY, CITY OF AN EMPLOYY

def emp(name='name123',salary=1234,city ='city123'):
    print(name)
    print(salary)
    print(city)
emp(name ='NIKKY', salary = 55000,city ='BANGLOARE')

#WAP TO CALCULATE TOTAL MARKS OF A STUDENT
def total (maths=123, phy=123,chem=123):
    print('Your total marks are:',maths+phy+chem)
total (maths=45, phy=56,chem=59)

#WAP TO FIND THE PRODUCT OF N NUMBER
def pro(*a):
    mul =1
    for i in a:
        mul =mul*i
     
    return mul
print(pro(1,2,3,4,5))

#WAP TO ACCEPT ANY NUMBER OF NAMES AND PRINT THEM
def name(*b):
    print(b)
name('nikky','akshya','lily')

#WAP TO CREATE A FUNC THAT ACCEPTS ANY NUM OF KEYWORD ARGS AND PRINTS ALL THE KEYS AND VALUES

def val (**k):
       for key, value in k.items():
           print(key, ':', value)
