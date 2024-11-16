# [HSAT 인증평가 2회] Garage Game -> 다시 풀어보기,, 답 안맞음
largest = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

N = int(input())
v = [[[] for _ in range(N)] for _ in range(3)]

def dfs(round, cnt, coordinate, visit, adjacent, neighbor):
    x, y = coordinate
    left, right, bottom, top = adjacent
    
    cnt += 1
    color = v[round][x][y]
    neighbor.append([x,y])
    visit[x][y] = True
    
    left = min(left, x)
    right = max(right, x)
    bottom = min(bottom, y)
    top = max(top, y)
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (0 <= nx and nx <= N-1) and (0 <= ny and ny <= N-1) and (v[round][nx][ny] == color) and (visit[nx][ny] == False):
            cnt, adjacent, neighbor = dfs(round, cnt, (nx, ny), visit, (left, right, bottom, top), neighbor)
            left, right, bottom, top = adjacent
            
    return cnt, (left, right, bottom, top), neighbor

def remove(round, neighbor):
    global v
    
    v[round+1] = [element[:] for element in v[round]] # 2차원 배열 복사
    for item in neighbor:
        x, y = item[0], item[1]
        v[round+1][x][y] = 0

def refill(round):
    global v
    
    for i in range(N):
        tmp = []
        for j in range(len(v[round+1][i])):
            value = v[round+1][i][j]
            if value != 0:
                tmp.append(value)
        v[round+1][i] = tmp
        
def calculate_neighbor(round):
    neighbor_exist = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if (i < N-1) and (v[round][i][j] == v[round][i+1][j]):
                neighbor_exist[i][j] = neighbor_exist[i+1][j] = 1
            if (j < N-1) and (v[round][i][j] == v[round][i][j+1]):
                neighbor_exist[i][j] = neighbor_exist[i][j+1] = 1
                
    return neighbor_exist

def simulate(round, score_sum):
    global largest
    visit = [[False for _ in range(N)] for _ in range(N)]
    neighbor_exist = calculate_neighbor(round)
    
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                continue
            
            left = right = i
            bottom = top = j
            cnt = 0
            
            if (round == 2) and (neighbor_exist[i][j] == 0):
                cnt = 1
                area = 1
                visit[i][j] = True
            else:
                neighbor = []
                cnt, adjacent, neighbor = dfs(round, cnt, (i,j), visit, (left, right, bottom, top), neighbor)
                left, right, bottom, top = adjacent
                area = (right-left+1) * (top-bottom-1)
                
            new_score_sum = score_sum + cnt + area
            
            if round == 2:
                if largest < new_score_sum:
                    largest = new_score_sum
            else:
                remove(round, neighbor)
                refill(round)
                
                simulate(round+1, new_score_sum)

# main
for _ in range(3*N):
    tmp = list(map(int, input().split()))
    for i in range(N):
        v[0][i].append(tmp[i])
            
for i in range(N):
    v[0][i].reverse()
        
simulate(0,0)
print(largest)