'''
������ȣ���̱� -> �������� ���� ���� ����
�ð� ����	�޸� ����	����	����	���� ���	���� ����
1 ��	128 MB	155312	68257	43234	41.812%
����
<�׸� 1>�� ���� ���簢�� ����� ������ �ִ�. 1�� ���� �ִ� ����, 0�� ���� ���� ���� ��Ÿ����. ö���� �� ������ ������ ����� ���� ������ ������ �����ϰ�, ������ ��ȣ�� ���̷� �Ѵ�. 
���⼭ ����Ǿ��ٴ� ���� � ���� �¿�, Ȥ�� �Ʒ����� �ٸ� ���� �ִ� ��츦 ���Ѵ�. 
�밢���� ���� �ִ� ���� ����� ���� �ƴϴ�. <�׸� 2>�� <�׸� 1>�� �������� ��ȣ�� ���� ���̴�. 
������ �Է��Ͽ� �������� ����ϰ�, �� ������ ���ϴ� ���� ���� ������������ �����Ͽ� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է�
ù ��° �ٿ��� ������ ũ�� N(���簢���̹Ƿ� ���ο� ������ ũ��� ������ 5��N��25)�� �Էµǰ�, �� ���� N�ٿ��� ���� N���� �ڷ�(0Ȥ�� 1)�� �Էµȴ�.

���
ù ��° �ٿ��� �� �������� ����Ͻÿ�. �׸��� �� ������ ���� ���� ������������ �����Ͽ� �� �ٿ� �ϳ��� ����Ͻÿ�.

���� �Է� 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
���� ��� 1 
3
7
8
9
'''

N=int(input())
matrix=[]
num=[]
complex_count=0 #�������� ����

for i in range(N):
    row=list(map(int, input()))
    matrix.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j):
    matrix[i][j]=0 #1�� 0���� �ٲپ �湮ǥ�ø� ��(�湮 �迭�� ���� ������ ����)

    for k in range(4):
        ni=i+dx[k]
        nj=j+dy[k]

        #������ ����� �ٸ���������
        if(ni<0 or ni>=N or nj<0 or nj>=N):
            continue
        if(matrix[ni][nj]==1): #���̰�, ���� �湮���� ���� ���̶��
            global count 
            count+=1
            dfs(ni, nj)

    return count


for i in range(N):
        for j in range(N):
            if matrix[i][j]==1:
                complex_count+=1
                count=1 #ī��Ʈ �ʱ�ȭ �ϴ� ��
                num.append(dfs(i, j))#���� ���⼭ �ٷ� print(dfs(i,j))�� �߾��µ�, �׷��� �ϸ� complex_count���� �׻� ���� ����� �Ǵϱ� num��� ����Ʈ�� ���� �����صΰ� �������� �����

print(complex_count)
num.sort()#�������� ����
for i in num:
     print(i)


'''
bfs�� �������� ���� ���ϴ� �ڵ�
from collections import deque

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    matrix[i][j] = 0  # �湮 ǥ��

    count = 1  # ���� ��� �� ���� �� �ʱ�ȭ

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if matrix[nx][ny] == 1:  # �湮���� ���� ���� ���
                queue.append((nx, ny))
                matrix[nx][ny] = 0  # �湮 ǥ��
                count += 1  # ���� �� ����

    return count


N = int(input())
matrix = []

for _ in range(N):
    row = list(map(int, input()))
    matrix.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

complex_count = 0  # ���� ����� ����
num = []  # �� ���� ��� �� ���� ���� ������ ����Ʈ

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            complex_count += 1
            num.append(bfs(i, j))

print(complex_count)
num.sort()  # �������� ����

for i in num:
    print(i)
'''