import sys
from collections import defaultdict

S=sys.stdin.readline().strip()
dict=defaultdict(int)
for char in S:
    dict[char]+=1

for value in range(ord('a'), ord('z')+1):
    print(dict[chr(value)], end=' ')