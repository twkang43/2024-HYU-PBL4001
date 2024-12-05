# [HSAT 2회 정기 코딩 인증평가 기출] Garage game
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(rnd, adjacent_count, x, y, visited, l, r, b, t, neighbor):
    adjacent_count += 1
    color = garage[rnd][x][y]
    neighbor.append([x,y]) # 지워야 할 차량의 좌표값
    visited[x][y] = True
    
    l,r = min(l,x), max(r,x) # 직사각형 면적 계산 위한 left, right 값 업데이트
    b,t = min(b,y), max(t,y) # 직사각형 면적 계산 위한 bottom, top 값 업데이트
    
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if (0 <= nx < N) and (0 <= ny < N) and (garage[rnd][nx][ny] == color) and (not visited[nx][ny]):
            adjacent_count,l,r,b,t,neighbor = dfs(rnd,adjacent_count,nx,ny,visited,l,r,b,t,neighbor)
            
    return adjacent_count,l,r,b,t,neighbor

def remove(rnd, neighbor): # 사라질 차량을 제거
    garage[rnd+1] = [item[:] for item in garage[rnd]] # garage[rnd]에 대한 deep copy 
    for cell in neighbor:
        x,y = cell
        garage[rnd+1][x][y] = 0 # (x,y)는 색이 없도록 설정

def refill(rnd): # 차량이 제거된 후 남은 차량을 아래로 떨어뜨림
    for x in range(N):
        tmp = []
        for y in range(len(garage[rnd+1][x])):
            v = garage[rnd+1][x][y]
            if v != 0:
                tmp.append(v)
                
        garage[rnd+1][x] = tmp
        
def calculate_neighbor(rnd): # dfs를 돌지 않고 각 좌표 근처에 같은 색의 차량이 있는지 확인
    has_neighbor = [[False for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if (x < N-1) and (garage[rnd][x][y] == garage[rnd][x+1][y]): # (x,y)와 (x+1,y)의 색이 같은 경우
                has_neighbor[x][y] = has_neighbor[x+1][y] = True
            if (y < N-1) and (garage[rnd][x][y] == garage[rnd][x][y+1]): # (x,y)와 (x,y+1)의 색이 같은 경우
                has_neighbor[x][y] = has_neighbor[x][y+1] = True
    return has_neighbor

def simulate(rnd, score_sum): # rnd: 현재 라운드 순서, score_sum: 현재까지 얻은 점수의 합
    global largest
    visited = [[False for _ in range(N)] for _ in range(N)]
    has_neighbor = calculate_neighbor(rnd)
    
    for x in range(N):
        for y in range(N):
            if visited[x][y]: # 이미 방문했으면 넘어감 -> 효율적
                continue
            
            l = r = x
            b = t = y
            adjacent_count = 0 # (x,y)와 인접한 점 중 색이 같은 점의 수
            
            
            if (rnd == 2) and (has_neighbor[x][y] == False): # 마지막 단계에서 (x,y) 근처에 같은 색의 차가 없는 경우
                adjacent_count,area = 1,1
                visited[x][y] = True
            else:
                neighbor = []
                adjacent_count,l,r,b,t,neighbor = dfs(rnd,adjacent_count,x,y,visited,l,r,b,t,neighbor)
                area = (r-l+1) * (t-b+1) # 해당 차고를 포함하는 가장 작은 직사각형 면적 계산
                
            new_score_sum = score_sum + area + adjacent_count
            
            if rnd == 2: # 현재 라운드가 마지막 라운드라면 largest 업데이트
                if largest < new_score_sum:
                    largest = new_score_sum
            else:
                remove(rnd,neighbor) # 사라져야 하는 자동차를 삭제
                refill(rnd) 
                simulate(rnd+1, new_score_sum)

# main
N = int(input())
garage = [[[] for _ in range(N)] for _ in range(3)] # 게임 라운드 x (NxN)

for _ in range(3*N):
    tmp = list(map(int, input().split()))
    for i in range(N):
        garage[0][i].append(tmp[i])
        
for i in range(N): # stack 형태가 되게 reverse
    garage[0][i].reverse()

largest = 0 # 게임을 3차례 했을때 얻을 수 있는 가장 큰 값
simulate(0,0)
print(largest)