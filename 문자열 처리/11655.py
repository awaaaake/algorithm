import sys
input= sys.stdin.readline

data=input().rstrip('\n')
for i in data:
    if i.isupper():
        if (ord(i)+13) >90: #90±îÁö´Â ±¦ÂúÀ½
            print(chr(ord(i)-13), end='')
        else:
            print(chr(ord(i)+13), end='')
    elif i.islower():
        if (ord(i)+13) >122: #122±îÁö´Â ±¦ÂúÀ½
            print(chr(ord(i)-13), end='')
        else:
            print(chr(ord(i)+13), end='')
    else: 
        print(i,end='')