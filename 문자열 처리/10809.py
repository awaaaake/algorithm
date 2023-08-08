import sys
S=sys.stdin.readline().strip()

list=[-1]*26
for i in range(len(S)):
    if list[ord(S[i])-97]==-1: #처음등장하는 위치한번만 저장해야하므로
        list[ord(S[i])-97]=i
for i in list:
    print(i,end=' ')