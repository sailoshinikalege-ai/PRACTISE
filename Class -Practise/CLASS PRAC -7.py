''' 
l = eval(input("enter a list:"))

new = []

for i in l:
    if i not in new:
        new.append(i)

print(new)

d = eval(input("Enter a tuple: "))

new = {}

for i in d:
    if isinstance(i, str):
        new[i] = len(i)

print(new)

a = eval(input("enter a list:"))
new={}

for i in a :
    if isinstance(i, str):
     new [i] = i[0],i[-1]

print(new)

ch = input("enter a character:")

new ={}

for i in ch:
    if ord (i)>=65 and ord (i)<= 90:
        new [i] = chr(ord (i) +32)
    if ord (i)>=97 and ord (i)<= 112:
        new [i] = chr(ord (i) -32)
print (new)

l =[12,'program',7+3j,5.6,'break',9]
new={}

for i in l:
    if type(i)==str:
        vow=''
        for j in i:
            if j not in 'AEIOUaeiou':
             vow+=j
        new[i]= vow
print(new)

l = [12, 'program', 7+3j, 5.6, 'break', 9]
new = {}

for i in l:
    if type(i) == str:
        vow = ''
        for j in i:
            if ord(j) >= 65 and ord(j) <= 90:
                vow += chr(ord(j) + 32)
            if ord(j) >= 97 and ord(j) <= 122:
                vow += chr(ord(j) - 32)

        new[i] = vow

print(new)'''



l = [10,13,4,6]
new= []

for i in l:
    sum =0
    for j in l:
        if i != j:
            sum = sum +j
    new.append(sum)      
print(new)  
    
#l= [1000,700,100,300,900,200]
# n = 1000
# output = [1000,[700,100],[300,900,200]]


l =[1000,700,100,300,900,200]
temp =0

