import sys
input = sys.stdin.readline
n, k = map(int, input().split())
stack=[i for i in range(1,n+1)]
list=[]

turn=k-1

for _ in range(n): #while True:도 가능
    list.append(stack.pop(turn))
    if not stack:
        break
    turn=(turn+k-1)%len(stack) #turn에있던 요소가 pop됐으므로, 인덱스가 한칸씩밀림->-1해주고, 스택의 크기가 계속바뀌므로, 스택크기로 나눈 나머지

print('<'+', '.join(str(i) for i in list)+'>')
