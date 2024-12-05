# [HSAT 4회 정기 코딩 인증평가 기출] 통근버스 출발 순서 검증하기
import sys
input = sys.stdin.readline

# main
N = int(input())
array = [[0 for _ in range(N+1)] for _ in range(N+1)]
stack = list(map(int, input().split()))

cnt = 0
# array[j][i]: i보다 오른쪽에 있는 stack 값 중 j보다 작은 수들의 개수
for i in range(N-1,0,-1):
    for j in range(1,N+1):
        if stack[i] < j: # stack[i]가 j보다 작다면, 다음 위치의 값은 현재 위치에서 1 증가
            array[j][i-1] = array[j][i] + 1
        else: # 그렇지 않다면, 현재 값 유지
            array[j][i-1] = array[j][i]
            
for i in range(N-2):
    for j in range(i+1,N-1):
        if stack[i] < stack[j]:
            cnt += array[stack[i]][j] # j 이후의 값들 중 stack[i]보다 작은 값의 개수를 더함
            
print(cnt)