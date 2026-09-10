'''
1. * * *
'''
n =3
for i in range(1,n+1):
    print ('*',end='')
'''

2.* * *
  * * *
  * * *
'''
n = 3
for i in range(1,n+1):
    for j in range (1,n+1):
        print ('*',end='')
    print()
'''

3.
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end='')
    print()

'''
4.

*
* *
* * *
* * * *
* * * * *
'''
n = 6
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>j:
            print('*',end ='')
    print()
'''

5.

*
  *
    *
      *
        *

'''

n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        if i == j:
            print('*', end='')
        else:
            print('  ', end='')
    print()


''' 
6.
n = 5
@
* @
* * @
* * * @
* * * * @
'''
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        if i>j :
            print('*', end=' ')
        else:
            print('@', end=' ')
    print()


'''
7.

# # # # $
# # # $ &
# # $ & &
# $ & & &
$ & & & &
'''
n = int(input("enter a num:"))

for i in range (1,n+1):
    for j in range (1,n+1):
        if i +j == n+1:
            print('$', end=' ')
        elif i+j>n+1:
            print('&', end=' ')
        elif i+j<n+1:
            print('#', end=' ')
        else:
            print(' ')
    print()
                


'''

8.

* * * * *
*       *
*       *
*       *
* * * * *
'''
n = 5

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''

9.

1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
'''

n =5
for i in range (1,n+1):
    for j in range (1,n+1):
        if i ==j :
            print('1', end=' ')
        else:
            print('0',end =' ')
    print()

'''
10.

*       *
  *   *
    *
  *   *
*       *
'''
n = int (input('Enter a num:'))

for i in range (1, n+1):
    for j in range(1,n+1):
        if i==j:
            print('*', end=' ')
        elif i+j == n+1:
            print('*', end=' ')
        else :
            print(' ', end=' ')
    print()

'''
11.

    *
    *
    *
* * * * *
    *
    *
    *
'''
for i in range (1,8):
    for j in range (1,6):
        if j ==3 or i == 4:
            print('*', end =' ')
        else :
            print(' ', end=' ')
    print()
'''

12.

* * * * * * * * *
* *     *     * *
*   *   *   *   *
*     * * *     *
* * * * * * * * *
*     * * *     *
*   *   *   *   *
* *     *     * *
* * * * * * * * *
'''
n =9
for i in range (1,n+1):
    for j in range (1,n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print('*', end=' ')
        elif i+j ==n+1:
            print('*', end=' ')
        elif i==j:
            print('*', end=' ')
        elif i ==5 or j ==5:
            print('*', end=' ')
        else:
           print(' ', end=' ')

    print()
'''
13.

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

n = int(input('enter a num:'))

for i in range(1,n+1):
    num =1
    for j in range (1,n+1):
        print (num , end =' ') 
        num= num+1
    print()
    
'''
14.

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''

n = int(input("enter a num:"))
num =1
for i in range (1, n+1):
    
    for j in range (1,n+1):
        print(num, end='')
    print()
    num = num+1

'''

15.

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
n = int(input("enter a num:"))

for i in range (1, n+1):
    num =1
    for j in range (1,i+1):
        print(num, end=' ')
        num = num+1
    print( )

'''
16.

23
23 24
23 24 25
23 24 25 26
23 24 25 26 27
'''

n = int(input("Enter a num:"))

for i in range(1, n+1):
    num = 23

    for j in range(1, i+1):
        print(num, end=" ")
        num = num + 1

    print()
    '''


17.

5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''
n = int(input("Enter a num:"))

for i in range(1, n+1):
    num = n

    for j in range(1, i+1):
        print(num, end=" ")
        num = num -1

    print()
'''
18.

*   *
* * *
* * *
* * *
*   *
'''
n = 5

for i in range(1, n+1):
    for j in range(1, 4):
        if (i == 1 or i == 5) and j == 2:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

'''
19.

* * * * *
*       *
*       *
*       *
* * * * *
'''
n = int(input("Enter a num:"))

for i in range(1, n+1):
    for j in range (1,n+1):
        if i ==1 or i ==n or j ==1 or j ==n:
            print('*', end=' ')
        else:
            print(' ', end =' ')

    print( )
'''

20.

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
n = int(input("enter a num:"))

for i in range (1, n+1):
    for j in range (1,n+1):
        print('*', end=' ')
    print()
'''

21.

* * * * *
* *   * *
*   *   *
* *   * *
* * * * *
'''
n = int(input("enter a num:"))
for i in range (1, n+1):
    for j in range(1, n+1):
        if i ==j or i +j == n+1 or i ==1 or i==n or j == n or j ==1 :
            print('*', end=' ')
        else :
            print(' ', end =' ')
    print( )
'''
22.

*       *
  *   *
    *
  *   *
*       *

'''
n = int (input("enter a num:"))
for i in range (1, n+1):
    for j in range (1, n+1):
       if i ==j or i+j == n+1:
           print('*', end=' ')
       else:
           print (' ', end =' ')
    print( )
'''
23.

1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
'''
n = int (input("enter a num:"))
for i in range (1, n+1):
    for j in range (1, n+1):
       if i ==j or i+j == n+1:
           print('1', end=' ')
       else:
           print ('0', end =' ')
    print( )
'''
24.

* * * * *
  * * * *
    * * *
      * *
        *
'''
n = int(input('enter a num:'))
for i in range (1, n+1):
    for j in range (1, n+1):
        if i <= j:
            print('*', end=' ')
        else :
            print(' ', end = ' ')
    print( )

'''
25.

        *
      * *
    * * *
  * * * *
* * * * *
'''
n = int(input('enter a num:'))
for i in range (1, n+1):
    for j in range (1, n+1):
        if i+j >= n+1:
            print('*', end=' ')
        else :
            print(' ', end = ' ')
    print( )
'''
26.

* * * * *
* * * *
* * *
* *
*
'''
n = int(input('enter a num:'))
for i in range (1, n+1):
    for j in range (1, n+1):
        if i+j <= n+1:
            print('*', end=' ')
        else :
            print(' ', end = ' ')
    print( )

'''
27.

* * * * *
  * * * *
    * * *
      * *
        *
'''
n = int(input('enter a num:'))
for i in range (1, n+1):
    for j in range (1, n+1):
        if i<j:
            print('*', end=' ')
        else :
            print(' ', end = ' ')
    print( )
'''
28.

        *
      * *
    * * *
  * * *
* * * * *
'''
n = int(input('enter a num:'))
for i in range (1, n+1):
    for j in range (1, n+1):
        if i+j >= n+1:
            print('*', end=' ')
        else :
            print(' ', end = ' ')
    print( )
'''


29.

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

n =int(input('enter a num:'))
num =1

for i in range (1, n+1):
    for j in range (1,i+1):
        if i >=j:
          print (num , end =' ')
        else :
           print(' ', end =' ')
    num = num +1
    print( )
'''

30.

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''

n =int(input('enter a num:'))
num =1

for i in range (1, n+1):
    for j in range (1,i+1):
        if i >=j:
          print (num , end =' ')
        else :
           print(' ', end =' ')
        num = num +1
    print( )
'''
31.

5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
'''
n =int(input('enter a num:'))
num =n

for i in range (1, n+1):
    for j in range (1,i+1):
        if i >=j:
          print (num , end =' ')
        else :
           print(' ', end =' ')
    num = num -1
    print( )
'''

32.

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

'''
n = int(input('enter a num:'))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i >= j:
            print(i - j + 1, end=' ')
        else:
            print(' ', end=' ')

    print()
'''
33.

1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9

'''
n = int(input('enter a num:'))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(i + j - 1, end=' ')
    print()

'''
34.

5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''

n = int(input('enter a num:'))

for i in range(1, n+1):
    num =n
    for j in range(1, n+1):
        if i +j <=n+1:
         print (num , end= ' ')
        else:
           print(' ', end =' ')
        num = num-1
    print()
'''

35.

1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25

'''
n = int(input("enter a num:"))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(i*j, end=' ')
    print()
   
'''
36.

1 1 1 1 1
1 2 2 2 2
1 2 3 3 3
1 2 3 4 4
1 2 3 4 5

'''

n = int(input("enter a num:"))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
'''
37.

5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1

'''
n = int(input('enter a num:'))
num = n
for i in range (1, n+1):
    for j in range (1,n+1):
        print(num, end =' ')
    num = num-1
    print( )
'''
38.

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''
n = int(input('enter a num:'))

for i in range (1, n+1):
    for j in range (1,n+1):
        if i +j<= n+1:
         print(n-i-j+2, end =' ')
    
    print( )
'''
39.

1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
'''

n = int(input('enter a num:'))

for i in range (1, n+1):
    for j in range (1,n+1):
        if i +j<= n+1:
         print(i+j-1, end =' ')
    
    print( )
'''
40.

* * * * *
  * * * *
    * * *
      * *
        *
'''
n = int(input('enter a num:'))
for i in range (1, n+1):
    for j in range (1, n+1):
        if i <= j:
            print('*', end=' ')
        else :
            print(' ', end = ' ')
    print( )
'''

41.

* * * * *
*       *
*   *   *
*       *
* * * * *
'''
n = int(input('Enter a num:'))

for i in range (1, n+1):
    for j in range (1,n+1):

     if i== 1 or i ==n or j ==1 or j==n :
        print('*', end = ' ')
     elif i == (n+1)//2 and j == (n+1)//2:
            print('*', end=' ')
     else:
            print(' ', end=' ')

   
    print( )
'''

42.

*       *
  *     *
    *   *
      * *
        *

'''
n = int (input("enter a num:"))
for i in range (1, n+1):
    for j in range (1, n+1):
        if j ==n or i ==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print( )
'''
43.

*       *
* *     *
*   *   *
*     * *
*       *
'''
n = int (input("enter a num:"))
for i in range (1, n+1):
    for j in range (1, n+1):
        if j ==n or j ==1 or i ==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print( )
'''

44.

* * * * *
* * * * *
*   *   *
* * * * *
* * * * *
'''
n = int (input("enter a num:"))
for i in range (1, n+1):
    for j in range (1, n+1):
        if j ==n or j ==1 or i ==j or i ==1 or i ==n:
            print('*', end=' ')
        elif i ==2 or i==n-1:
            print('*', end =' ')
        else:
            print(' ', end=' ')
    print( )
'''

45.

* * * * *
*       *
*   *   *
*       *
* * * * *
'''

n = int (input("enter a num:"))
for i in range (1, n+1):
    for j in range (1, n+1):
        if j ==n or j ==1 or i ==1 or i ==n:
            print('*', end=' ')
        elif i == (n+1)//2 and j == (n+1)//2:
            print('*', end=' ')
        else:
            print(' ', end =' ')
    print( )
'''
46.

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
n = int(input('Enter the num:'))
for i in range (1, n+1):
    for j in range(1, n+1):
        print('*', end = ' ')
    print( )
'''

47.

WAP to print the PRIMARY DIAGONAL of a 5 × 5 matrix.
'''
n = 5
for i in range(1, n+1):
    for j in range (1,n+1):
        if i==j :
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print( )
'''
48.

WAP to print the SECONDARY DIAGONAL of a 5 × 5 matrix.
'''
n = 5
for i in range(1, n+1):
    for j in range (1,n+1):
        if i+j == n+1 :
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print( )
'''
49.

WAP to print the pattern above the PRIMARY DIAGONAL.
'''
n = 5
for i in range(1, n+1):
    for j in range (1,n+1):
        if i<j :
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print( )
'''
50.

WAP to print the pattern below the PRIMARY DIAGONAL.
'''
n = 5
for i in range(1, n+1):
    for j in range (1,n+1):
        if i>j :
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print( )
'''
51.

WAP to print the pattern above the SECONDARY DIAGONAL.
'''
n = 5
for i in range(1, n+1):
    for j in range (1,n+1):
        if i+j<= n+1 :
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print( )
'''

52.

WAP to print the pattern below the SECONDARY DIAGONAL.
'''
n = 5
for i in range(1, n+1):
    for j in range (1,n+1):
        if i+j>= n+1 :
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print( )
'''
53.

WAP to print both the PRIMARY and SECONDARY DIAGONALS.
'''
n = int(input('enter a num:'))
for i in range(1, n+1):
    for j in range (1,n+1):
        if i+j== n+1 or i ==j :
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print( )
'''
54.

WAP to print a hollow square pattern using nested loops.
'''
n = 5
for i in range(1, n+1):
    for j in range (1,n+1):
        if i==n or j==n or i==1 or j==1 :
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print( )

'''
55.

WAP to print a square pattern using * on the boundary
and spaces inside. 
'''
n = 5
for i in range(1, n+1):
    for j in range (1,n+1):
        if i==n or j==n or i==1 or j==1 :
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print( )
'''

56. WAP a program to print A.
'''
n =8
for i in range (n):
    for j in range (9):
        if (1<=4 and(j==4-i or j ==4+i)) or (i >=4 and (j==0 or j==8)) or (i ==4 and 0<j<8):
            print('*', end=" ")
        else:
            print(' ', end = ' ')

    print( )
'''
'''