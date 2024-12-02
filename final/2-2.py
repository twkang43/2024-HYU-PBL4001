# [21년 재직자 대회 예선] 마이크로서버
import sys
input = sys.stdin.readline

# main
T = int(input())
for _ in range(T):
    N = int(input())
    m = sorted(list(map(int, input().split())))
    
    start, end = 0, N-1
    count = 0    
    
    while (start <= end) and (600 < m[end]): # memory가 600 이상이라면 서버 하나 독점
        count += 1
        end -= 1
    
    while (start <= end) and (m[start] == 300 and m[end] == 600): # memory가 300+600이 되는 경우
        count += 1
        start += 1
        end -= 1
        
    mem300_count = 0 # memory가 300인 서비스의 수
    while (start <= end) and (m[start] == 300):
        mem300_count += 1
        start += 1
        
    while start < end:
        if m[start] + m[end] <= 900:
            count += 1
            start += 1
            end -= 1
        elif 0 < mem300_count: # 300 + (mem < 600) -> 서버 하나 할당
            count += 1
            mem300_count -= 1
            end -= 1
        else: # (mem < 600)에 서버 하나 할당
            count += 1
            end -= 1
            
    if start == end:
        count += 1
        if 0 < mem300_count: # 남은 메모리와 300을 같이 할당
            mem300_count -= 1
            
    if 0 < mem300_count:
        count += ((mem300_count+2)//3)
    
    print(count)