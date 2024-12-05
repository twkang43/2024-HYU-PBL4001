# [HSAT 7회 정기 코딩 인증평가 기출] 자동차 테스트
import sys
import bisect
input = sys.stdin.readline

# main
n,q = map(int, input().split())
car = sorted(list(map(int, input().split())))
set_car = set(car)

for _ in range(q):
    m = int(input())
    
    if m not in set_car: # 탐색: O(1) (hash table 사용하기 때문)
        print(0)
    else:
        index = bisect.bisect_left(car,m) # car 내에서 m보다 작은 원소의 개수 저장
        print(index*(n-index-1)) # 경우의 수 = (자신보다 연비가 낮은 차량의 수) x (자신보다 연비가 높은 차량의 수) 