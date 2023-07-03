import sys

input = sys.stdin.readline
INF = int(1e9)

#노드의 개수와 간선의 개수 입력
N, M =map(int, input().split())
#모든 간선에 대한 정보를 담는 리스트
edges = []
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N+1)

#모든 간선의 정보 입력
for i in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C)) #간선정보를 튜플 형태로 추가

def bellman_ford(start):
    #시작노드에대해서 초기화
    distance[start]=0
    #전체 N-1번의 라운드를 반복
    for i in range(N):
        #매 반복마다 모든 간선을 확인한다.
        for j in range(M):
            cur_node = edges[j][0] #하나의 튜플내에서
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node]+edge_cost:
                #edges[j][1] = distance[cur_node] + edge_cost 입력으로 주어진 정보의 값은 바꾸면 안됨..
                distance[next_node]=distance[cur_node]+edge_cost
                # N번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == N-1:
                    return True
    return False

# 벨만 포드 알고리즘 수행
negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    #1번 노드를 제외한 다른 모든 노드로 가기위한 최단 거리를 출력
    for i in range(2, N+1):
        #도달할 수 없는 경우, -1출력
        if distance[i]== INF:
            print("-1")
        else: #else를 안하면 INF인 경우에대해서 -1도 출력하고, INF도 출력하는것임
            print(distance[i])