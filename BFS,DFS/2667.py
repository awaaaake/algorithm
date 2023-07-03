'''
단지번호붙이기 -> 연결요소의 개수 유사 문제
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	155312	68257	43234	41.812%
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
예제 출력 1 
3
7
8
9
'''

N=int(input())
matrix=[]
num=[]
complex_count=0 #연결요소의 개수

for i in range(N):
    row=list(map(int, input()))
    matrix.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j):
    matrix[i][j]=0 #1을 0으로 바꾸어서 방문표시를 함(방문 배열을 따로 만들지 않음)

    for k in range(4):
        ni=i+dx[k]
        nj=j+dy[k]

        #범위를 벗어나면 다른방향으로
        if(ni<0 or ni>=N or nj<0 or nj>=N):
            continue
        if(matrix[ni][nj]==1): #집이고, 아직 방문하지 않은 집이라면
            global count 
            count+=1
            dfs(ni, nj)

    return count


for i in range(N):
        for j in range(N):
            if matrix[i][j]==1:
                complex_count+=1
                count=1 #카운트 초기화 하는 곳
                num.append(dfs(i, j))#원래 여기서 바로 print(dfs(i,j))를 했었는데, 그렇게 하면 complex_count보다 항상 먼저 출력이 되니까 num라는 리스트에 따로 저장해두고 마지막에 출력함

print(complex_count)
num.sort()#오름차순 정렬
for i in num:
     print(i)


'''
bfs로 연결요소의 개수 구하는 코드
from collections import deque

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    matrix[i][j] = 0  # 방문 표시

    count = 1  # 연결 요소 내 집의 수 초기화

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if matrix[nx][ny] == 1:  # 방문하지 않은 집인 경우
                queue.append((nx, ny))
                matrix[nx][ny] = 0  # 방문 표시
                count += 1  # 집의 수 증가

    return count


N = int(input())
matrix = []

for _ in range(N):
    row = list(map(int, input()))
    matrix.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

complex_count = 0  # 연결 요소의 개수
num = []  # 각 연결 요소 내 집의 수를 저장할 리스트

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            complex_count += 1
            num.append(bfs(i, j))

print(complex_count)
num.sort()  # 오름차순 정렬

for i in num:
    print(i)
'''