wallpaper=["..........", ".....#....", "......##..", "...##.....", "....#....."]
def solution(wallpaper):
    min_x, min_y = len(wallpaper), len(wallpaper[0])
    max_x, max_y = 0, 0

    for i in range(len(wallpaper)): #드래그 시작 위치
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if i < min_x:
                    min_x=i
                if i >= max_x:
                    max_x=i
                if j < min_y:
                    min_y=j
                if j >= max_y:
                    max_y=j
    return [min_x,min_y,max_x+1,max_y+1]

print(solution(wallpaper))      