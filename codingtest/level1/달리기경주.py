def solution(players, callings):
    dic={}
    for i, player in enumerate(players): #선수: 등수
        dic[player] = i
    for who in callings:
        index=dic[who]
        dic[who] -=1
        dic[players[index-1]] +=1
        players[index-1], players[index] = players[index], players[index-1]
    return players