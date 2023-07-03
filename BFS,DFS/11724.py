'''
연결요소의 개수구하기
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1 
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1 
2
예제 입력 2 
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
예제 출력 2 
1
'''
import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph=[[] for i in range(N+1)] #[[], [], [], []] 각 노드의 인접 리스트 생성

visited_dfs =[0]*(N+1)
count=0

for i in range(M):
    u, v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    visited_dfs[start]=1
    for node in graph[start]:
        if not visited_dfs[node]:
            dfs(node)

for i in range(1, N+1): #graph로 하지 않는다. 각 노드의 리스트는 for i in grahp[node]로하지만, 각 노드로 접근할때는 그냥 range로
    if not visited_dfs[i]: #만약 i번째 노드를 방문하지 않았다면
        if not graph[i]: #해당 정점이 연결된 그래프도 없다면
            count+=1 #그 노드자체로 하나의 연결요소이므로
            visited_dfs[i]
        else: #연결된 그래프가 있다면
            dfs(i)
            count+=1

print(count)     

'''
bfs로 구현한 코드
from collections import deque

def bfs(start):
    queue = deque([start])
    visited_bfs[start] = 1

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited_bfs[neighbor]:
                queue.append(neighbor)
                visited_bfs[neighbor] = 1

# 이전 코드에서 bfs로 연결요소의 개수를 구하는 부분을 추가합니다.
visited_bfs = [0] * (N+1)
count_bfs = 0

for i in range(1, N+1):
    if not visited_bfs[i]:
        if not graph[i]:
            count_bfs += 1
            visited_bfs[i] = 1
        else:
            bfs(i)
            count_bfs += 1

print(count_bfs)

'''


