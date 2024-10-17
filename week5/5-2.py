# [HSAT 인증평가 1회] 차세대 지능형 교통시스템
from collections import deque

# 0 : north, 1 : east, 2 : south, 3 : west
directions = [[],
              [1,2,0], # 1 (E, S, N)
              [0,1,3], # 2 (N, E, W)
              [3,0,2], # 3 (W, N, S)
              [2,3,1], # 4 (S, W, E)
              [1,2],   # 5 (E, S)
              [0,3],   # 6 (N, W)
              [3,2],   # 7 (W, S)
              [2,1],   # 8 (S, E)
              [1,2],   # 9 (E, S)
              [0,1],   # 10 (N, E)
              [3,0],   # 11 (W, N)
              [2,3],   # 12 (S, W)
              ]
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

N, T = map(int, input().split())

signals = []
# (N+1) x (N+1) x current_time x current_direction
visit = [[[[False for _ in range(4)] for _ in range(4)] for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    signal = []
    for j in range(N):
        signal.append(list(map(int, input().split())))
    signals.append(signal)
    
q = deque()
q.append([1,1,0])
visit[1][1][0][0] = 1

current_time = 0
answer = set()
answer.add((1,1))

while q:
    if current_time == T:
        break
    
    q_size = len(q)
    while q_size:
        y, x, direction = q.popleft()
        q_size -= 1
        
        if direction != directions[signals[y-1][x-1][current_time%4]][0]:
            continue
        
        for i in directions[signals[y-1][x-1][current_time%4]]:
            ny = y + dy[i]
            nx = x + dx[i]
            
            if (ny < 1 or nx < 1) or (N < ny or N < nx) or visit[ny][nx][current_time%4][i]:
                continue
            
            visit[ny][nx][current_time%4][i] = True
            q.append([ny, nx, i])
            answer.add((ny, nx))
        
    current_time += 1

print(len(answer))