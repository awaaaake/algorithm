import sys 
from collections import deque

N = int(sys.stdin.readline())
queue = deque([])

for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(queue) == 0:
            print(-1)
            continue
        if cmd[0] == 'pop':
            print(queue.popleft())
        elif cmd[0] == 'front':
            print(queue[0])
        elif cmd[0] == 'back':
            print(queue[-1])
