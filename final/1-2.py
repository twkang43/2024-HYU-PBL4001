# [21년 재직자 대회 예선] 전광판
import sys
input = sys.stdin.readline

"""
. 0 .
1   2
| 3 |
4   5
. 6 .
"""
light = []
light.append([1,1,1,0,1,1,1]) # 0
light.append([0,0,1,0,0,1,0]) # 1
light.append([1,0,1,1,1,0,1]) # 2
light.append([1,0,1,1,0,1,1]) # 3
light.append([0,1,1,1,0,1,0]) # 4
light.append([1,1,0,1,0,1,1]) # 5
light.append([1,1,0,1,1,1,1]) # 6
light.append([1,1,1,0,0,1,0]) # 7
light.append([1,1,1,1,1,1,1]) # 8
light.append([1,1,1,1,0,1,1]) # 9
on_off_transition = [6,2,5,5,4,5,6,4,7,6]

# main
T = int(input())
for _ in range(T):
    A,B = map(str, input().split())
    answer = 0
    
    if(len(A) != len(B)): # A와 B의 길이가 다른 경우
        if(len(B) < len(A)): # A가 B보다 더 긴 경우
            residual = len(A)-len(B)
            for i in range(residual):
                answer += on_off_transition[int(A[i])-0]
            A = A[residual:]
            
        else: # B가 A보다 더 긴 경우
            residual = len(B)-len(A)
            for i in range(residual):
                answer += on_off_transition[int(B[i])-0]
            B = B[residual:]
            
    for i in range(len(A)):
        if(A[i] != B[i]): # 숫자가 다른 경우
            for j in range(7): # light의 각 전구의 변화 추적
                if(light[int(A[i])][j] != light[int(B[i])][j]):
                    answer += 1
                    
    print(answer)