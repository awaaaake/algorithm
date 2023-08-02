import sys
input = sys.stdin.readline

N=int(input())
data=[]
for i in range(N):
    data.append(tuple(map(int, input().split())))
#map 함수의 반환 값은 map객체 이기 때문에 해당 자료형을 list 혹은 tuple로 형 변환시켜주어야 합니다.

sorted_data = sorted(data, key=lambda x : (x[0], x[1]))
for X,Y in sorted_data:
    print(X,Y)
