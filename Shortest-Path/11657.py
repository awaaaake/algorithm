import sys

input = sys.stdin.readline
INF = int(1e9)

#����� ������ ������ ���� �Է�
N, M =map(int, input().split())
#��� ������ ���� ������ ��� ����Ʈ
edges = []
#�ִ� �Ÿ� ���̺��� ��� �������� �ʱ�ȭ
distance = [INF] * (N+1)

#��� ������ ���� �Է�
for i in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C)) #���������� Ʃ�� ���·� �߰�

def bellman_ford(start):
    #���۳�忡���ؼ� �ʱ�ȭ
    distance[start]=0
    #��ü N-1���� ���带 �ݺ�
    for i in range(N):
        #�� �ݺ����� ��� ������ Ȯ���Ѵ�.
        for j in range(M):
            cur_node = edges[j][0] #�ϳ��� Ʃ�ó�����
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            # ���� ������ ���ļ� �ٸ� ���� �̵��ϴ� �Ÿ��� �� ª�� ���
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node]+edge_cost:
                #edges[j][1] = distance[cur_node] + edge_cost �Է����� �־��� ������ ���� �ٲٸ� �ȵ�..
                distance[next_node]=distance[cur_node]+edge_cost
                # N��° ���忡���� ���� ���ŵȴٸ� ���� ��ȯ�� ����
                if i == N-1:
                    return True
    return False

# ���� ���� �˰��� ����
negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    #1�� ��带 ������ �ٸ� ��� ���� �������� �ִ� �Ÿ��� ���
    for i in range(2, N+1):
        #������ �� ���� ���, -1���
        if distance[i]== INF:
            print("-1")
        else: #else�� ���ϸ� INF�� ��쿡���ؼ� -1�� ����ϰ�, INF�� ����ϴ°���
            print(distance[i])