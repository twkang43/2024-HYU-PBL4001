# [HSAT 인증평가 1회] 로봇이 지나간 경로0

direction_char = ['^', '>', 'v', '<']
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

H, W = map(int, input().split())

grid = []
for i in range(H):
    grid.append(list(input().strip()))
    
def find_direction(x,y):
    cnt = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < H) and (0 <= ny < W) and (grid[nx][ny] == '#'):
            direction = i
            cnt += 1
    
    return (direction if cnt == 1 else -1)
    
def find_start_point(grid):
    for x in range(H):
        for y in range(W):
            if grid[x][y] == '#':
                direction = find_direction(x,y)
                
                if -1 < direction:
                    return x, y, direction
                
def traverse(x, y, direction):
    grid[x][y] = '.'
    prev_dir = direction
    new_dir = direction
    
    while True:
        while new_dir == prev_dir:
            print('A', end='')
            
            for _ in range(2):
                x += dx[new_dir]
                y += dy[new_dir]
                grid[x][y] = '.'
                
            prev_dir = new_dir
            new_dir = find_direction(x,y)
            
        if new_dir == -1:
            return
        elif (new_dir - prev_dir) % 4 == 1:
            print('R', end='')
        elif (new_dir - prev_dir) % 4 == 3:
            print('L', end='')
        prev_dir = new_dir
    
x, y, direction = find_start_point(grid)
print(f"{x+1} {y+1}")
print(direction_char[direction])
traverse(x, y, direction)