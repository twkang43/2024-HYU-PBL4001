# [HSAT 1회 정기 코딩 인증평가 기출] 로봇이 지나간 경로
import sys

direction_char = ['^', '>', 'v', '<']
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def find_direction(x,y): # 0: up, 1: right, 2: down, 3: left
    count = 0
    direction = -1
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        
        if (0 <= nx < H) and (0 <= ny < W) and (map[nx][ny] == '#'):
            count += 1
            direction = i
            
    return direction if count == 1 else -1

def find_starting_point():
    for i in range(H):
        for j in range(W):
            if map[i][j] == '#':
                direction = find_direction(i,j)
                
                if -1 < direction:
                    return i,j,direction
                
def traverse(x,y,direction): # (x,y): 현재 좌표, direction: 현재 방향
    route = []
    map[x][y] = '.' # 경로 흔적 제거
    current_direction = direction
    new_direction = direction
    
    while True:
        while current_direction == new_direction:
            route.append('A')
            
            for _ in range(2): # 2칸 이동
                x += dx[new_direction]
                y += dy[new_direction]
                map[x][y] = '.'
                
            current_direction = new_direction
            new_direction = find_direction(x,y)
            
        if new_direction == -1:
            return route
        elif (new_direction-current_direction) % 4 == 1: # right - 현재 direction에 대해 R/L 상대적 판단
            route.append('R')
        elif (new_direction-current_direction) % 4 == 3: # left
            route.append('L')
        
        current_direction = new_direction
    
# main
H,W = map(int, input().split())
map = []
for _ in range(H):
    map.append(list(input()))
    
x,y,direction = find_starting_point() # map에서 시작 지점과 방향 탐색
route = traverse(x,y,direction) # 경로 탐색

print(f"{x+1} {y+1}")
print(direction_char[direction])
for i in range(len(route)):
    print(route[i], end='')
print()