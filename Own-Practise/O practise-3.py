#ASSIGNMENT.

#WAP TO CONVERT ALL THE LOWERCASE CHARACTERS FROM A GIVEN STR INTO UPPERCASE.
ch = input("Enter your character:")
i = 0
upper = ""

while i < len(ch):
    if ord(ch[i]) >= 97 and ord(ch[i]) <= 122:
        upper = upper + chr(ord(ch[i]) - 32)
    else:
        upper = upper + ch[i]

    i = i + 1

print(upper)
#WAP TO CONVERT UPPERCASE CHARS TO LOWERCASE AND LOWERCASE  CHARS INTO  UPPERCASE IN A GIVEN STR.
#(SWAPCASE)

