'''
문제
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.



어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

예제 입력 1 
7
6
1 2
2 3
1 5
5 2
5 6
4 7
예제 출력 1 
4
'''

from collections import deque
'''
split을 쓰고 int형으로 바꿀거면 map이 필요하고, 아니면 그냥 바로
int(input())하면됨
'''
N=int(input())
M=int(input())

array=[[0]*(N+1) for i in range(N+1)]

#방문한곳을 체크할 리스트 이렇게하면 어떤 리스트가 만들어지지?/??
visited_bfs = [0]*(N+1) #[0,0,0,0,0]

for i in range(M):
    x, y=map(int, input().split())
    array[x][y]=array[y][x]=1

def bfs():
    #방문해야할 곳을 순서대로 넣을 큐
    queue=deque([1])
    visited_bfs[1]=1
    count=0
    #큐안에 데이터가없을때까지 반복
    while(queue):
        V=queue.popleft()
        for i in range(N+1):
            if(array[V][i]==1 and visited_bfs[i]==0):
                queue.append(i)
                visited_bfs[i]=1
                count+=1

    return count

print(bfs())