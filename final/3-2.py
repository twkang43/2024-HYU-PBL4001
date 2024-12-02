# [21년 재직자 대회 예선] 거리 합 구하기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs1(current, parent): # 서브트리 크기 및 거리 계산
    sub_tree_size[current] = 1 # leaf node == 1
    
    for i in range(len(tree[current])):
        child,t = tree[current][i]
        
        if child != parent: # 부모 노드를 제외한 자식 노드 탐색
            dfs1(child, current)
            distance_from_node[current] += (distance_from_node[child] + t*sub_tree_size[child])
            sub_tree_size[current] += sub_tree_size[child]
    
def dfs2(current, parent):
    for i in range(len(tree[current])):
        child,t = tree[current][i]
        
        if child != parent: # 증가 : N-sub_tree_size[child], 감소 : sub_tree_size[child]
            distance_from_node[child] = (distance_from_node[current] + t*(N - 2*sub_tree_size[child])) # 해당 노드에서 
            dfs2(child, current)

# main
N = int(input())
tree = [[] for _ in range(N+1)]
sub_tree_size = [0 for _ in range(N+1)] # 각 서브트리의 노드 개수
distance_from_node = [0 for _ in range(N+1)] # 각 노드에서 다른 모든 노드까지의 거리 합

for _ in range(N-1):
    x,y,t = map(int, input().split())
    tree[x].append([y,t])
    tree[y].append([x,t])

dfs1(1,1) # 1번 노드에 대해 우선 dfs 수행
dfs2(1,1) # 루트 노드의 거리 정보를 바탕으로 모든 노드의 거리 합 계산

for i in range(1,N+1):
    print(distance_from_node[i])