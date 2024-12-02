# [21년 재직자 대회 예선] 비밀 메뉴 2
import sys
input = sys.stdin.readline

# main
N,M,K = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

LCS = [[0 for _ in range(M+1)] for _ in range(N+1)] # DP table, 비밀메뉴의 길이
answer = 0

for i in range(1,N+1):
    for j in range(1,M+1):
        if first[i-1] == second[j-1]: # first와 second의 각 현재 원소가 같다면, 이전 비밀메뉴 길이에서 길이 1 증가
            LCS[i][j] = LCS[i-1][j-1] + 1
            answer = max(answer, LCS[i][j])

print(answer)