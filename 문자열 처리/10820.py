import sys
input = sys.stdin.readline

while (True):
    data = input().rstrip('\n')

    if not data:
        break

    lower , upper, num, blank = 0, 0, 0, 0
    for i in data:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():  # 숫자 확인 수정
            num += 1
        elif i.isspace():
            blank += 1
    print(lower, upper, num, blank)
