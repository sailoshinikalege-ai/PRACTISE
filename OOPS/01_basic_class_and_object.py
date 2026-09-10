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

#GENERIC STATE

class University:
    uni_name='OSMANIA UNIVERSITY'
    loc='Hyderbad'
    timings='9:00 to 3:30'
    cource='BCA'

st1=University( )
print(University.uni_name,University.loc,University.timings,University.cource)
print(st1.uni_name,st1.loc,st1.timings,st1.cource)

class University:
    uni_name='OSMANIA UNIVERSITY'
    loc='Hyderbad'
    timings='9:00 to 3:30'
    

st1=University( )
st1.name ='Loshini'
st1.course='BCA'
st1.gpa=9.8

st2=University()
st2.name='Varsha'
st2.course='BBA'
st2.gpa=9.7
print(University.uni_name,University.loc,University.timings)
print(st1.name,st1.course,st1.gpa)
print(st2.name,st2.course,st2.gpa)


#SPECIFIC STATE

class Company:
    cname='TCS' 
    loc='Hyderabad'
    ceo='abc'
emp1=Company()
emp1.name='Nikky'
emp1.id=1008
emp1.role='Data Scientist'

emp2=Company()
emp2.name='Lakky'
emp2.id=1009
emp2.role='Software developer'

print(Company.cname,Company.loc,Company.ceo)
print(emp1.name,emp1.id,emp1.role)
print(emp2.name,emp2.id,emp2.role)

#Difference btw func and method
def add():
    print('hi')
add()

class Demo:
    def show(Self):
        print('hii')
d.Demo()
d.show()

'''
#CONSTRUCTOR

class Demo():
    def __intit__(self):
      print('constructor executed')

print(Demo)


class Student():
   def __init__(self,name,age,std):
      self.name=name
      self.age=age
      self.std=std
s1=Student('Nikky',22,'BCA')
print(s1.name,s1.age,s1.std)
print(id(s1))

class Marks():
   def __init__(self,phy,math,eng,chem):
      self.phy=phy
      self.math=math
      self.eng=eng
      self.chem =chem
s1=Marks(98,96,95,99)
print(s1.phy,s1.math,s1.chem,s1.eng)      

