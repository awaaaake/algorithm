T = int(input())

for i in range(T):
    stack = []
    a=input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:# ���ÿ� ��ȣ�� ������� NO -> ¦�� ���� �ʴ� ���
                print("NO")
                break
    else:# break������ ������ �ʰ� ����������� �����Ѵ�
            if not stack:# break������ �Ȳ���� ������ ����ִٸ� ��ȣ�� �� �´°Ŵ�.
                print("YES")
            else:# break�� �ɷȴ��� ���ÿ� ��ȣ�� ����ִٸ� NO�̴�.
                print("NO")