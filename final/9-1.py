# [HSAT 5회 정기 코딩 인증평가 기출] 업무 처리
import sys
from collections import deque
input = sys.stdin.readline

completed_tasks = 0

def assign_tasks(time):
    global completed_tasks
    
    if 0 < len(team[0]): # 부서장이 업무 처리 -> 완료
        completed_tasks += team[0].popleft()
    
    for i in range(2**H-1): # top-down
        if time%2 == 0: # 짝수 번째 날짜
            child = 2*i+2
        else: # 홀수 번째 날짜
            child = 2*i+1
        
        if 0 < len(team[child]):
            team[i].append(team[child].popleft())

# main
H,K,R = map(int, input().split())
team = [deque() for _ in range((2**(H+1))-1)] # 팀의 현재 처리중인 업무 수
terminal = [deque(map(int, input().split())) for _ in range(2**H)] # 말단 사원 각각의 현재 업무 수

for i in range(2**H): # 팀에 말단 사원의 업무 할당
    team[(2**H)+i-1] = terminal[i]
    
for r in range(R):
    assign_tasks(r)
    
print(completed_tasks)