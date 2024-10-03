# [21년 재직자 대회 예선] 거리 합 구하기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for i in range(N+1)]
subTreeSize = [0 for _ in range(N+1)]
distFromNode = [0 for _ in range(N+1)]

def dfs1(current, parent):
    subTreeSize[current] = 1
    for i in range(len(tree[current])):
        child, weight = tree[current][i]
        
        if child != parent:
            dfs1(child, current)
            distFromNode[current] += distFromNode[child] + weight*subTreeSize[child]
            subTreeSize[current] += subTreeSize[child]

def dfs2(current, parent):
    for i in range(len(tree[current])):
        child, weight = tree[current][i]
        
        if child != parent:
            distFromNode[child] = distFromNode[current] + weight*(N-2*subTreeSize[child])
            dfs2(child, current)

for _ in range(1, N):
    x, y, t = map(int, input().split())
    tree[x].append((y,t))
    tree[y].append((x,t))
    
dfs1(1,1)
dfs2(1,1)

for i in range(1, N+1):
    print(distFromNode[i])