name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

def solution(name, yearning, photo):
    result = []
    dic={}
    for i, who in enumerate(name):
        dic[who] = yearning[i]
    for object in photo:
        score = 0
        for who in object:
            if who in name:
                score += dic[who] 
        result.append(score)
    return result

print(solution(name, yearning, photo))

# def solution(name, yearing, photo):
#     dictionary = dict(zip(name, yearning))
#     scores = []
#     for pt in photo:
#         score = 0
#         for p in pt:
#             if p in dictionary:
#                 score += dictionary[p]
#             scores.append(score)
#     return scores