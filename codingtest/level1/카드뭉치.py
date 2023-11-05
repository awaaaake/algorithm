def solution(cards1, cards2, goal):
    last1=-1 #card1뭉치에서 마지막으로 뽑은 단어의 인덱스
    last2=-1 #card2뭉치에서 마지막으로 뽑은 단어의 인덱스
    for word in goal:
        if(word in cards1):
            if (last1 +1 == cards1.index(word)):
                last1=cards1.index(word)
            else:
                return "No"
        elif(word in cards2):
            if (last2 +1 ==  cards2.index(word)):
                last2=cards2.index(word)
            else:
                return "No"
        else:
            return "No"
    return "Yes"


def solution(cards1, cards2, goal):
    for word in goal:
        if cards1 and (word == cards1[0]): 
            #맨 앞에있는 단어부터 사용하면, 그게 곧 "순서"와 "사용했던 단어는 다시 사용할수 없다"는 조건을 모두 만족
            del cards1[0] # 또는 cards1.pop(0)
        elif cards2 and (word == cards2[0]):
            del cards2[0]
        else:
            return 'No'
    return 'Yes'
