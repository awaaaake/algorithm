park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]

def solution(park, routes):
    H = len(park)
    W = len(park[0])
    op = {"N" : (-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
   
    for i in range(len(park)): #시작위치 찾기
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x,y= i,j
                break

    #좌표이동
    for route in routes:
        dir, dist = route.split()
        dist=int(dist)
        
        dx, dy = x, y #현재위치
        for _ in range(dist):
            nx = x + op[dir][0]
            ny = y + op[dir][1]
            if 0<=nx<=H-1 and 0<=ny<=W-1 and (park[nx][ny]!="X"):
                x, y = nx, ny   
            else:
                x, y = dx, dy
                break
    return [x, y]

solution(park, routes)

