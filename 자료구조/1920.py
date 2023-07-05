'''
수 찾기
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	211102	64707	42888	29.980%
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

예제 입력 1 
5
4 1 5 2 3
5
1 3 7 9 5
예제 출력 1 
1
1
0
0
1
'''
import sys
#1 2 3을 입력으로 받고, data에 리스트 형태로 각 정수를 원소로 담기 위해서는 다음과 같은 코드를 작성
N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
sorted_nums = sorted(nums)
M = int(input())
data = list(map(int, sys.stdin.readline().split()))

def binary_search(target, list):
    start=0
    #mid=len(nums)//2 x 왜? 시작값이 0or 1이 아닐수 있기 때문
    end=len(list)-1
    
    while start <= end:
        mid=(start+end)//2 #값자체가 아닌 인덱스 번호로써 사용
        if target<list[mid]:
            end=mid-1
        elif target>list[mid]:
            start=mid+1
        else:
            return True
    return False

for target in data:
    if binary_search(target, sorted_nums):
        print(1)
    else:
        print(0)


'''
set을 이용한 코드
import sys
N = int(input())
nums = set(map(int, sys.stdin.readline().split()))
M = int(input())
data = list(map(int, sys.stdin.readline().split()))

for target in data:
    print(1) if target in nums else print(0)
'''