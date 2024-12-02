# 21년 재직자 대회 예선] 이미지 프로세싱
import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j,c): # bfs 통해 한 query에 대해 색상 변경 수행
    value = image[i][j]
    image[i][j] = c
    
    queue = deque()
    queue.append([i,j])
    
    while len(queue):
        x,y = queue[0][0], queue[0][1]
        queue.popleft()
        
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if(0 <= nx < H) and (0 <= ny < W) and (image[nx][ny] == value):
                image[nx][ny] = c
                queue.append([nx,ny])

# main
H,W = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(H)]

Q = int(input())
for _ in range(Q):
    i,j,c = map(int, input().split())
    bfs(i-1,j-1,c)

for x in range(H):
    for y in range(W):
        print(f"{image[x][y]} ", end="")
    print()