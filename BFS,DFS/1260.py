'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 
1 2 4 3
1 2 3 4
예제 입력 2 
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2 
3 1 2 5 4
3 1 4 2 5
예제 입력 3 
1000 1 1000
999 1000
예제 출력 3 
1000 999
1000 999
'''

from collections import deque

#n=정점개수, m=간선개수, v=탐색시작점
N, M, V = list(map(int, input().split()))

#인접영행열
matrix = [[0]*(N+1) for i in range(N+1)] #for i in range(N+1)에 들어가는 값이 행의 개수

#방문한곳을 체크기록할 리스트
visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)

#입력받는 값에 대해 영행렬에 1 삽입(인접리스트 생성)
for i in range(M):
    a, b=map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(V):
    visited_dfs[V]=1
    print(V, end=' ')
    #재귀
    for i in range(1, N+1):#i를 1부터 시작해서 작은수부터 방문하게됨
        if(visited_dfs[i]==0 and matrix[V][i]==1):#V와 인접한 노드이면서, 방문하지 않았다면 그 노드에대해서 다시 DFS
            dfs(i)

def bfs(V):
    #방문해야할 곳을 순서대로 넣을 큐
    queue=deque([V])
    visited_bfs[V]=1

    #큐안에 데이터가없을때까지 반복
    while queue:
        V=queue.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if(visited_bfs[i]==0 and matrix[V][i]==1):
                queue.append(i)
                visited_bfs[i]=1

dfs(V)
print()
bfs(V)


