# [HSAT 4회 정기 코딩 인증평가 기출] 슈퍼컴퓨터 클러스터
import sys
input = sys.stdin.readline

def check_budget(mid):
    total_cost = 0
    for i in range(N):
        if computer[i] < mid: # 예상 향상 성능보다 낮은 성능의 컴퓨터만 업그레이드
            total_cost += ((mid-computer[i])**2)
        
    return True if total_cost <= B else False

def binary_search(start, end):
    if start == end:
        return start
    
    mid = (start+end+1)//2 # 컴퓨터의 최소 성능
    
    if check_budget(mid): # 현재 설정한 컴퓨터의 최소 성능으로는 예산이 남음 -> 최소 성능 늘림
        return binary_search(mid, end)
    else: # 현재 설정한 컴퓨터의 최소 성능으로는 예산이 부족 -> 최소 성능 줄임
        return binary_search(start, mid-1)

# main
N,B = map(int, input().split())
computer = sorted(list(map(int, input().split())))

answer = binary_search(computer[0], computer[-1]+(10**9)) # B 내로 향상시킬 수 있는 최소 성능 계산
print(answer)