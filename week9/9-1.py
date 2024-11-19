# [HSAT 5회 정기 코딩 인증평가 기출] 업무 처리
import sys
from collections import deque

completed_tasks = 0

def assign_tasks(r): # top-down으로 일처리 -> 일 할당받기
    global completed_tasks
    
    if 0 < len(team[0]): # top
        completed_tasks += team[0].popleft()
    
    for i in range(num-1):
        if r % 2 == 0: # 오른쪽 업무 (짝수)
            child = 2*i+2
        else: # 왼쪽 업무 (홀수)
            child = 2*i+1
            
        if 0 < len(team[child]):
            team[i].append(team[child].popleft())
            
# main
H, K, R = map(int, input().split())
num = 2**H
terminal = [deque(map(int, input().split())) for _ in range(num)] # 입력받은 말단 직원의 처음 업무

team = [deque() for _ in range(2*num-1)] # 팀 전체의 업무
for i in range(num): # 팀에 말단 직원의 업무 할당
    team[num+i-1] = terminal[i]

for r in range(R): # r: 0,1,...,R-1
    assign_tasks(r)
    
print(completed_tasks)