# [21년 재직자 대회] 코딩 테스트 세트 

def test(mid):
    slist = [0] * N
    slist[0] = clist[0]
    
    for i in range(N-1):
        if mid <= slist[i]:
            slist[i+1] = clist[i+1] + dlist[i]
        elif mid <= slist[i] + dlist[i]:
            slist[i+1] = clist[i+1] + (slist[i] + dlist[i] - mid)
        else:
            return False
        
    return True if mid <= slist[N-1] else False

def binary_search(start, end):
    if start == end:
        return start
    
    mid = (start+end+1) // 2
    if(test(mid)):
        return binary_search(mid, end)
    else:
        return binary_search(start, mid-1)

N, T = map(int, input().split())
for i in range(T):
    clist = []
    dlist = []
    
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if j%2 == 0:
            clist.append(tmp[j])
        else:
            dlist.append(tmp[j])
            
    print(binary_search(0, 2*(10**12)))