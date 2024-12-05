# [HSAT 2회 정기 코딩 인증평가 기출] 사물인식 최소 면적 산출 프로그램
import sys
input = sys.stdin.readline

surface = 987654321

def dfs(color_idx, x_max, x_min, y_max, y_min): # dfs를 통해 색상을 하나씩 처리하며 모든 조합 탐색
    global surface 

    if K < color_idx:
        surface = min(surface, abs((x_max-x_min) * (y_max-y_min)))
        return

    for i in range(len(color[color_idx])):
        x_new, y_new = color[color_idx][i]
        
        x_max_new, x_min_new = max(x_max, x_new), min(x_min, x_new)
        y_max_new, y_min_new = max(y_max, y_new), min(y_min, y_new)
        surface_new = abs((x_max_new-x_min_new) * (y_max_new-y_min_new)) # 현재의 점을 포함하는 직사각형 면적 계산
        
        if (surface_new < surface) or (color_idx == 1): # 백트래킹 (현재 점을 포함하는 직사각형이 기존 직사각형보다 작으면 해당 점 사용)
            dfs(color_idx+1, x_max_new, x_min_new, y_max_new, y_min_new)
        

# main
N,K = map(int, input().split())
color = [[] for _ in range(K+1)] # 각 색이 가지는 좌표들

for _ in range(N):
    x,y,k = map(int, input().split())
    color[k].append([x,y])
    
dfs(1, -1001, 1001, -1001, 1001) # max: -1001, min: 1001 -> 직사각형의 범위 업데이트 위해 반댓값으로 설정
print(surface)