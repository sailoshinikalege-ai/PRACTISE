
#41. Write a function to accept two numbers and return their sum.

def add():
    a = int(input('ENTER A:'))
    b = int(input('ENTER B:'))

    sum = a + b

    return sum

print(add())

#Write a function to accept a number and check whether it is even or odd.

def check():
    num = int(input("Enter a num:"))

    if num % 2 ==0 :
        print('EVEN')
    else:
        print('ODD')
check()

# Write a function to accept a string and count the number of vowels.

def vowels():
    ch = input('Enter a string:')
    count =0
    for i in ch :
        if i in 'AEIOUaeiou':
            count = count+1
    print(count)
vowels()

#Write a function to accept a list and find the largest value using an inbuilt function.

def find():
    l = eval(input("Enter a list:"))
    
    return max(l)

print(find())

#45. Write a function using DEFAULT ARGUMENTS to calculate the total bill.
#Given:
#Item Price = 500
#Quantity = 2
#Discount = 50

def bill(price=500, quantity=2, discount=50):
    total = (price * quantity) - discount
    return total

print(bill())

#46. Write a function using KEYWORD ARGUMENTS to accept and display the following employee details:
#	Name
#	Salary
#	City
#	Department

def profile(Name,Salary,City,Department):
    print('Name:',Name)
    print('Salary:',Salary)
    print('City:',City)
    print('Department:',Department)
profile('Nikky', 50000,'Hyderabad','DataScientist')

#47. Write a function using *args to accept any number of numbers and return their sum.

def add_numbers(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(add_numbers(10, 20, 30, 40))


#49. PACKING + UNPACKING USING FUNCTION
'''
Write a function that accepts any number of student marks using *args.
The function should:
1.	Pack all marks inside args.
2.	Print the packed values.
3.	Find the total marks.
4.	Find the highest mark.
5.	Find the average.
'''

def marks(*args):
    total = 0

    print("Packed values:", args)

    for i in args:
        total = total + i

    highest = max(args)
    average = total / len(args)

    print("Total:", total)
    print("Highest:", highest)
    print("Average:", average)


marks(80, 90, 75, 85, 95)
'''
50. UNPACKING USING FUNCTION
Create a list containing employee details:
employee = ["Rahul", 25000, "Delhi"]
Create a function:
display_employee(name, salary, city)
Then unpack the list while calling the function.
Expected concept:
display_employee(*employee)
'''
employee = ["Rahul", 25000, "Delhi"]

def display_employee(name, salary, city):
    print("Name:", name)
    print("Salary:", salary)
    print("City:", city)

display_employee(*employee)

#51
def bill():

    proname = input("Enter the product name:")
    price = int(input("Enter the price:"))
    quan = int(input("Enter the quantity:"))
    dis = int(input("Enter the discount:"))

    total = price * quan
    finalamt = total - dis

    print("TOTAL:", total)
    print("FINAL BILL:", finalamt)

bill()

#52
def emp(NAME,BASIC_SALARY,BONUS,DEDUC):
    Net_Salary = BASIC_SALARY + BONUS - DEDUC
    print('Your net salary is:',Net_Salary)
emp('NIKKY',50000,10000,5000)

#53
def marks(*args):
    total = 0

    print("Packed values:", args)

    for i in args:
        total = total + i

    highest = max(args)
    average = total / len(args)
    lowest = min(args)

    print("Total:", total)
    print("Highest:", highest)
    print("Average:", average)
    print('Lowest:',lowest)


marks(78,85,90,67,88)

#54
def order(item_name, price, quan, deli_charge=30):

    Food_Total = price * quan

    Final_Bill = Food_Total + deli_charge

    print("Item:", item_name)
    print("Food Total:", Food_Total)
    print("Delivery Charge:", deli_charge)
    print("Final Bill:", Final_Bill)


order("Pizza", 300, 2)

#55

def login(user,psw='NIKKY123'):
    if user == 'nikky@123' and psw=='NIKKY123':
        print('login successful')
    else:
        print('Invalid Username or Password')

login('nikky@123')


#56
#Using keyword arguments
def trans(acc, bal, amt, tranty):

    if tranty == "deposit":
        bal = bal + amt
        print("Final balance:", bal)

    elif tranty == "withdraw":
        bal = bal - amt
        print("Final balance:", bal)


trans(acc=101, bal=5000, amt=1000, tranty="deposit")

#57
def cart(*prices):
    total =0
    count =0
    avg=0
    for i in prices:
        total = total+i
        count = count +1
        avg = total /len(prices)
    print('Total price:',total)
    print('Count:',count)
    print('Average:',avg)
cart(500, 1200, 300, 800, 150)

#58
def student_details(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)


student_details(name="Anjali", age=22, course="MCA", city="Kolkata")

#59
employee = ("Rahul", 25000, "Python", "Bangalore")

def employee_details(name, salary, department, city):

    print("Name:", name)
    print("Salary:", salary)
    print("Department:", department)
    print("City:", city)


employee_details(*employee)


#60

def order_details(customer_name, product, price, quantity):

    total = price * quantity

    print("Customer Name:", customer_name)
    print("Product:", product)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Amount:", total)


order = ("Anjali", "Laptop", 50000, 2)

order_details(*order)

#61. Create a function using *args to find the largest number withoutusing max().

'''
62. Create a function using *args to find the sum of only even
numbers.


63. Create a function using **kwargs to count the total number of
key-value pairs.


64. Create a function using **kwargs to print only the values.


65. Create a program demonstrating BOTH:

1. Packing using *args
2. Unpacking using *

Use a function in both cases.


66. Create a program demonstrating BOTH:

1. Packing using **kwargs
2. Unpacking using **

Use a function in both cases.

'''








