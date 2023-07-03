'''
1, 2, 3 더하기 다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	512 MB	102522	67437	46175	64.172%
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

예제 입력 1 
3
4
7
10
예제 출력 1 
7
44
274
'''

'''
n=1부터 차례대로 f(n)을 계산해보면 
f(n)=f(n-1)+f(n-2)+f(n-3)이라는 점화식이 구해진다.
'''
n_list=[]
topdown_memo=[0]*11
#기저 상태 도달 시, 1,2,4로 초기화
topdown_memo[1]=1
topdown_memo[2]=2
topdown_memo[3]=4

for i in range(4,11):
    topdown_memo[i]= sum(topdown_memo[i-3:i])#topdown_memo[i-1]+topdown_memo[i-2]+topdown_memo[i-3]

T=int(input())
for i in range(T):
    n_list.append(int(input()))

for n in n_list:
    print(topdown_memo[n])