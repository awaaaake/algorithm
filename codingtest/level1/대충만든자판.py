keymap = ["AGZ", "BSSS"]
targets = ["ASA","BGZ"]
def solution(keymap, targets):
    answer = []
    dic = {}
    for key in keymap:
        for i, char in enumerate(key):
            if char not in dic:
                dic[char] = i+1
            else: 
                dic[char]=min(i+1, dic[char])

    for target in targets:
        result = 0
        for char in target:
            if char in dic: #딕셔너리에 특정 키가 존재하는지는 if dic[char] : 대신 if char in dic:
                result+=(dic[char])
            else: 
                result=(-1) #목표 문자열을 작성할 수 없는 경우 = 문자열 중 하나의 문자라도 존재하지 않는경우
                break
        answer.append(result)
    return answer


print(solution(keymap, targets))