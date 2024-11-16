# [HSAT 3회 정기 코딩 인증평가 기출] 교차로
import sys
from collections import deque

NUM_MAX = 1234567890

current_time = 0
roads = ['A','B','C','D']

queue = {'A': deque(),'B': deque(),'C': deque(),'D': deque()}
right = {'A': 'D','B': 'A','C': 'B','D': 'C'}

def simulate():
    global current_time
    
    while queue['A'] or queue['B'] or queue['C'] or queue['D']:
        oldest_car = {'A': 0,'B': 0,'C': 0,'D': 0}
        
        for r in roads:
            # 해당 도로에 차가 있는 경우
            if len(queue[r]):
                _, t = queue[r][0]
                oldest_car[r] = t
            # 해당 도로에 차가 없는 경우
            else:
                oldest_car[r] = NUM_MAX
        
        if all(t <= current_time for t in oldest_car.values()): # deadlock
            return
        
        # 기다리는 차가 없으면 현재 시간을 다가올 차량 시간으로 설정
        if all(current_time < t for t in oldest_car.values()):
            min_key = min(oldest_car, key=oldest_car.get)
            current_time = oldest_car[min_key]
            
        can_pass = {'A': False, 'B': False, 'C': False, 'D': False}
            
        for r in roads:
            # 현재 도로에 차량이 존재할 경우
            if oldest_car[r] <= current_time:
                # 오른쪽 도로에 차량이 존재하고, 해당 차량이 현재 시간보다 이전에 도착했다면 현재 도로 차량은 못 움직임
                if len(queue[right[r]]) and (oldest_car[right[r]] <= current_time):
                    can_pass[r] = False
                # 그 외 경우는 현재 도로 차량 움직일 수 있음
                else:
                    can_pass[r] = True
        
        for r in roads:
            if can_pass[r]:
                i, _ = queue[r].popleft()
                pass_time[i] = current_time
         
        current_time += 1
                
# main
N = int(input())
pass_time = [-1]*N

for i in range(N):
    t, w = input().split()
    t = int(t)
    queue[w].append((i, t)) # 각 도로에 대한 차량의 도착 시간 queue에 저장
    
    if i == 0:
        current_time = t
        
simulate()

for time in pass_time:
    print(time)