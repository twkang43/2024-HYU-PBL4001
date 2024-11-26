# [HSAT 7회 정기 코딩 인증평가 기출] 순서대로 방문하기
import sys

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y,index): # (x,y): 현재 좌표, index: 도달해야 하는 다음 포인트의 인덱스
    global answer
    move_index = False
    
    if (x == spot[index][0]) and (y == spot[index][1]): # 해당 순서의 목표 지점에 도달한 경우
        if index == m-1: # 최종 위치에 마지막으로 도착했을 경우
            answer += 1
            return
        else:
            move_index = True
            index += 1
    
    visited[x][y] = 1
    
    for i in range(4): # (x,y)에서 시작하여 도달 가능한 경로 재귀적으로 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (-1 < nx < n) and (-1 < ny < n) and (not visited[nx][ny]):
            dfs(nx,ny,index)
    
    visited[x][y] = 0 # visited 원상복구
    if move_index: # 방문해야 하는 지점 복구
        index -= 1
    return
    
# main
n,m = map(int, input().split())
visited = []
spot = [] # 방문해야 할 지점

for _ in range(n):
    visited.append(list(map(int, input().split())))
for _ in range(m):
    x,y = list(map(int, input().split()))
    spot.append([x-1,y-1])
    
answer = 0
dfs(spot[0][0],spot[0][1],0)
print(answer)