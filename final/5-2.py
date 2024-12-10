# [HSAT 1회 정기 코딩 인증평가 기출] 안전운전을 도와줄 차세대 지능형 교통시스템
import sys
from collections import deque
input = sys.stdin.readline

# 0 : north, 1 : east, 2 : south, 3 : west
directions = [[],
              [1,2,0], # 1 (E, S, N)
              [0,1,3], # 2 (N, E, W)
              [3,0,2], # 3 (W, N, S)
              [2,3,1], # 4 (S, W, E)
              [1,0],   # 5 (E, N)
              [0,3],   # 6 (N, W)
              [3,2],   # 7 (W, S)
              [2,1],   # 8 (S, E)
              [1,2],   # 9 (E, S)
              [0,1],   # 10 (N, E)
              [3,0],   # 11 (W, N)
              [2,3],   # 12 (S, W)
              ]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs():
    current_time = 0
    
    while queue:
        if current_time == T:
            break
        
        queue_size = len(queue)
        while queue_size:
            y,x,direction = queue.popleft() # 현재 위치와 방향을 꺼냄
            queue_size -= 1
            
            if direction != directions[signals[y-1][x-1][current_time%4]][0]: # 현재 방향이 신호의 첫번째 방향이 아니면 이동 불가
                continue
            
            for i in directions[signals[y-1][x-1][current_time%4]]:
                nx,ny = x+dx[i],y+dy[i]
                
                if (nx < 1 or N < nx) or (ny < 1 or N < ny) or visited[ny][nx][current_time%4][i]: # 같은 시간에 대해 교차로 중복 방문 방지
                    continue
                
                visited[ny][nx][current_time%4][i] = True
                queue.append([ny,nx,i])
                answer.add((ny,nx))
                
        current_time += 1

# main
N,T = map(int, input().split())

signals = []
# (N+1) x (N+1) x 현재시간 x 현재방향
visited = [[[[False for _ in range(4)] for _ in range(4)] for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    signal = []
    for j in range(N):
        signal.append(list(map(int, input().split()))) # 각 교차로 신호 순서
    signals.append(signal)
    
queue = deque()
queue.append([1,1,0]) # 교차로 (1,1)에서 north 방향 (0) 진입
visited[1][1][0][0] = True

answer = set() # 교차로: 중복 카운트 X -> set
answer.add((1,1))
bfs() # BFS 통해 차량이 이동 가능한 경로 탐색

print(len(answer))