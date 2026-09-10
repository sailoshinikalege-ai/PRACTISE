'''
class Students:
    name ='puja'
    age =22
s1=Students()
print(s1.name)
print(s1.age)


#User-defined class

class creation:
    a=10
    b =20
demo = creation
print(creation.a,creation.b) #ACESSING WITH CLASS
print(demo.a,demo.b)         #ACESSING WITH OBJECT
'''
class Bank:
    bname='BOI'
    loc ='Hyderabad'
    manager='vinay'

cus1=Bank()
cus2=Bank()

print(Bank.bname,Bank.loc,Bank.manager)
print(cus1.bname,cus1.loc,cus1.manager)

#Modifying class var.

Bank.loc='Bangalore'
print(Bank.bname,Bank.loc,Bank.manager)
print(cus1.bname,cus1.loc,cus1.manager)

#CHANGING VALUES WITH OBJECT
cus1.manager='Nikky'
print(Bank.bname,Bank.loc,Bank.manager)
print(cus1.bname,cus1.loc,cus1.manager)
print(cus2.bname,cus2.loc,cus2.manager)
cus2.bname='SBI'
print(Bank.bname,Bank.loc,Bank.manager)
print(cus1.bname,cus1.loc,cus1.manager)
print(cus2.bname,cus2.loc,cus2.manager)