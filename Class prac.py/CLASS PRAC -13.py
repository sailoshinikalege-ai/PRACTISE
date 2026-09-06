
#GLOBAL VARIABLE

a = 10   #VARIABLE CREATED OUTSIDE FUNC KNOWN AS GLOBAL VARIABLE
b = 20   
def sam():
    print(a,b)
    print(a+b)
sam ()

#MODIFYING GLOBAL VARAIBLE

a = 10 # ITS A GLOBAL VARAIABLE
def sam():
    a = 100   # IT DOESNT MODIFY CAUSE ITS LOCAL VARIABLE
sam()
print(a)

# USING GLOBAL KEYWORD

a = 10
b = 200

def sam():
    global a,b
    print(a,b)
    a = 100
    b = 250

    print(a+b)
print('BEFORE MODIFICATION:', a,b)
sam ()
print('AFTER MODIFICATION:',a,b)

