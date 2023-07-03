# ����-���� �˰��� �ڵ� (
# Python)Permalink
import sys
input = sys.stdin.readline

INF = int(1e9) # ���Ѵ� ��

# ���, ������ ���� �Է�
v, e = map(int, input().split())
# ��� ������ ���� ������ ��� ����Ʈ
edges = []

# �ִܰŸ� ���̺��� ���Ѵ�� �ʱ�ȭ
distance = [INF] * (v + 1)

# ��� ������ ���� �Է�
for _ in range(e):
    sv, ev, cost = map(int, input().split())
    edges.append((sv, ev, cost))

# ����-���� �˰���
def bellmanFord(start):
    # ���� ��忡 ���ؼ� �ʱ�ȭ
    distance[start] = 0
    # v�� edge relaxation�� �ݺ�.
    # v - 1�� Ž���ϰ� ������ �ѹ��� Negative cycle ���� Ȯ��
    for i in range(v):
        # �� �ݺ����� ��� ������ Ȯ���ϸ� ����
        for j in range(e):
            curNode, nextNode, edgeCost = edges[j]
            # ���� ������ ���ļ� �ٸ� ���� �̵��ϴ� �Ÿ��� �� ª�� ���
            if distance[curNode] != INF and distance[curNode] + edgeCost < distance[nextNode]:
                distance[nextNode] = distance[curNode] + edgeCost
                # v��° �ݺ����� ���ŵǴ� ���� ������ Negative cycle ����
                if i == v - 1:
                    return False

    # ����-���� ��������
    return True

if bellmanFord(1):
    # 1�� ��带 ������ �ٸ� ��� ���� ���� ���� �ִܰŸ��� ���
    for i in range(2, v + 1):
        # ������ �� ���� ���
        if distance[i] == INF:
            print("������ �� ����.")
        else:
            print(distance[i])
else:
    print("Negative Cycle Exist")
# �ð����⵵Permalink
# ���� ��带 ������ ��� ���� (
# V - 1), �׸��� negative cycle�� Ȯ���ϱ� ���� �ѹ� �� �ݺ��ϱ� ������ �� V�� �ݺ��� ���ؼ� �ش� ������ ����� ��� ����(
# E)�� Ž���Ѵ�."