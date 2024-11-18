# [HSAT 4회 정기 코딩 인증평가 기출] 슈퍼컴퓨터 클러스터
import sys

def check_budget(mid):
    total_cost = 0
    
    for i in computer:
        if i < mid: # 예상 향상 성능보다 낮은 성능의 컴퓨터만 업그레이드
            total_cost += (mid - i) ** 2
        
    if total_cost <= B: # 업그레이드에 사용된 비용을 budget B와 비교
        return True
    else:
        return False

def binary_search(start, end): # start, end: 향상할 수 있는 성능
    if start == end:
        return start
    
    mid = (start + end + 1) // 2
    
    if check_budget(mid): # budget이 남는 경우
        return binary_search(mid, end)
    else: # budget이 남지 않는 경우
        return binary_search(start, mid-1)

# main
N, B = map(int, input().split())
computer = list(map(int, input().split()))
computer.sort()

# 큰 B의 범위 -> binary search를 통한 최적의 budget의 범위를 효율적으로 판단
# [최소 향상 성능, 최대 향상 성능] 사이 binary search를 통해 가장 tight한 최종 cost와 컴퓨터 중 최대 향상 성능 계산
answer = binary_search(computer[0], computer[-1] + 10**9)
print(answer)