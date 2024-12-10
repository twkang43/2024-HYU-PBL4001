# [HSAT 4회 정기 코딩 인증평가 기출] 통근버스 출발 순서 검증하기
import sys
input = sys.stdin.readline

# main
N = int(input())
buses = list(map(int, input().split()))

more = [[0 for _ in range(N)] for _ in range(N)] # more[i][k]: i-k 구간에 buses[i]보다 큰 buses[k]의 수
total = 0

for i in range(N):
    for k in range(i+1,N): # i < j < k, 이후 k가 j의 역할을 하기 때문에 i+1부터 시작
        if buses[i] < buses[k]: # 이후 k가 j의 역할
            more[i][k] = more[i][k-1] + 1
        else: # buses[k] < buses[i]
            more[i][k] = more[i][k-1]
            total += more[i][k] # i-k 사이에 buses[i]보다 큰 값의 수를 total에 더함

print(total)