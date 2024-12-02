# [21년 재직자 대회 예선] 비밀 메뉴
import sys
input = sys.stdin.readline

# main
M,N,K = map(int, input().split())
secret = list(map(int, input().split()))
buttons = list(map(int, input().split()))

answer = True
if(N < M):
    answer = False
else:
    for i in range(N-M+1): # 인덱스 초과 확인
        answer = True
        k = 0
        
        for j in range(i,i+M):
            if(buttons[j] != secret[k]):
                answer = False
                break
            k += 1
            
        if answer:
            break

print("secret" if answer else "normal")