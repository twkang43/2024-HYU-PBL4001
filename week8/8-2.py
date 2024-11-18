# [HSAT 4회 정기 코딩 인증평가 기출] 통근버스 출발 순서 검증하기
import sys

cnt = 0

# main
N = int(input())
array = [[0 for _ in range(N+1)] for _ in range(N+1)] # [0,N] x [0,N]
a = list(map(int, input().split()))

# array[j][i]: i보다 오른쪽에 있는 a 값 중 j보다 작은 수들의 개수
for i in range(N-1, 0, -1):
    for j in range(1, N+1):
        if(a[i] < j):
            array[j][i-1] = array[j][i] + 1
        else:
            array[j][i-1] = array[j][i]
            
for i in range(N-2):
    for j in range(i+1, N-1):
        if(a[i] < a[j]):
            cnt += array[a[i]][j]

print(cnt)