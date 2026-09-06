#PACKING AND UNPACKING


#PACKING
'''
def pack(*a):           # '*' used for packing into tuple
    print(type(a))
    print(a)
pack(1,2,3,4,5,6)

def pack(*a):           # '*' used for packing into tuple
    print(type(a))
    print(a)
pack(1.0,2.5,3.2,4.3,5.4,6.7)

def pack(*a):           # '*' used for packing into tuple
    print(type(a))
    print(a)
pack(6+9j , 6+8j)

def pack(*a):           # '*' used for packing into tuple
    print(type(a))
    print(a)
pack(True, False)

#WAP TO FIND THE STRING VALUES FROM A TUPLE USING PACKING

def pack(*a):
    for i in a:
        if type(i) == str:
            print(i)
pack(10.0, 'he;;o', 'nikky',89)

#WAP TO PRINT ALL THE VALUES FROM A TUPLE USING PACKING

def pac(*a):
    for i in a :
        print(i)

pac(10, 'heyy', 10.6, 'True', True)


def pack(**b):
    print(type(b))
    print(b)

pack (a=1, b=2)

# WAP TO PRINT ALL THE KEYS PRESENT INSIDE A DICTIONARY USING DOUBLE PACKING

def pac(**a):
    for i in a:
        print(i)

pac(a=1, b=3, cat=45)

# WAP TO PRINT ALL THE VALUES PRESENT INSIDE A DICTIONARY USING DOUBLE PACKING

def pac(**a):
    for i in a.values():
        print(i)

pac(a=1, b=3, cat=45)

# WAP TO PRINT ALL THE VALUES AND KEYS PRESENT INSIDE A DICTIONARY USING DOUBLE PACKING

def pack(**a):
    for k, v in a.items():
        print(k, v)

pack(a=1, b=3, cat=45)


#COMBINATION OF SINGLE & DOUBLING PACKING

def pack(*a ,**b):
    print(type(a))
    print(a)
    print(type(b))
    print(b)
#pack (12,90, a=5 ,b=7)
#pack (78,56,89)
#pack (a=5, b=7)
pack()
'''
#UNPACKING

def pack(c1,c2,c3):
    print(c1,c2,c3)
pack(*'abc')
pack(*[10,20,30])
pack(*(8,5,4))
pack(*{'a':6, 'b':9, 'c':10}.values())  # FOR VALUES
pack(*{'a':6, 'b':9, 'c':10}.items())   #FOR BOTH KEYS AND VALUES