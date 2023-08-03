import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
data = []

for i in range(N):
    data.append(int(input()))

# �� ������ �󵵸� �����ϴ� ��ųʸ�
count_dict = defaultdict(int)

for num in data:
    count_dict[num] += 1

print(count_dict.items())
result=sorted(count_dict.items(), key=lambda x:(x[1],-x[0]))
print(result[-1][0])
