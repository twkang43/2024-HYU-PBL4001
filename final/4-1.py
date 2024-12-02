# [21년 재직자 대회 본선] 코딩 테스트 세트 
import sys
input = sys.stdin.readline

def test(mid):
    s_list = [0 for _ in range(N)]
    s_list[0] = c_list[0]
    
    for i in range(1,N):
        if mid <= s_list[i-1]: # 이전 단계에 충분히 문제가 많아 현재 단계의 문제에 애매한 문제를 몰아주는 경우
            s_list[i] = c_list[i] + d_list[i-1]
        elif mid <= s_list[i-1] + d_list[i-1]: # 이전 단계에 필요한 문제를 제하고 현재 단계에 주는 경우
            s_list[i] = c_list[i] + (d_list[i-1] - (mid - s_list[i-1]))
        else: # 이전 단계에 문제가 부족한 경우
            return False
        
    return True if mid <= s_list[N-1] else False

def binary_search(start, end):
    if start == end:
        return start
    
    mid = (start+end+1)//2
    if(test(mid)): # 큰 범위에 대해 bsearch
        return binary_search(mid,end)
    else: # 작은 범위에 대해 bsearch
        return binary_search(start,mid-1)

# main
N,T = map(int, input().split())
for _ in range(T):
    c_list, d_list = [], []
    
    l = list(map(int, input().split()))
    for i in range(2*N-1):
        if (i%2) == 0:
            c_list.append(l[i])
        else:
            d_list.append(l[i])
            
    answer = binary_search(0, 2*(10**12)) # 가능한 테스트 케이스의 최소값부터 최대값에 대해 binary serach
    print(answer)