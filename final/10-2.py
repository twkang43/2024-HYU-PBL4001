# [HSAT 6회 정기 코딩 인증평가 기출] 출퇴근길
import sys
sys.setrecursionlimit(10**6) # recursion 제한 풀기
input = sys.stdin.readline

def dfs(current_node, current_adj, visit):
    if visit[current_node]:
        return
    
    visit[current_node] = True
    for node in current_adj[current_node]:
        dfs(node,current_adj,visit)

# main
n,m = map(int, input().split())

adj = [[] for _ in range(n+1)]
adj_reverse = [[] for _ in range(n+1)] # 방향이 바뀐 그래프
for _ in range(m):
    x,y = map(int, input().split())
    adj[x].append(y)
    adj_reverse[y].append(x)

S,T = map(int, input().split())

# 출근길: S -> i -> T가 이어져 있어야 함
from_s = [False]*(n+1) # 집에서 특정 지점 i까지 도달 가능 여부 확인
from_s[T] = True # from: 목적지에 도달하면 더 탐색하지 않도록 목적지 노드를 미리 방문 처리
dfs(S,adj,from_s) # S에서 T로 나가는 엣지들에 대한 dfs

to_t = [False]*(n+1) # 특정 지점 i에서 회사까지 도달 가능 여부 확인
dfs(T,adj_reverse,to_t) # T로 들어오는 엣지들에 대한 dfs

# 퇴근길: T -> i -> S가 이어져 있어야 함
from_t = [False]*(n+1) # 회사에서 특정 지점 i까지 도달 가능 여부 확인
from_t[S] = True
dfs(T,adj,from_t) # T에서 S로 나가는 엣지들에 대한 dfs

to_s = [False]*(n+1) # 특정 지점 i에서 집까지 도달 가능 여부 확인
dfs(S,adj_reverse,to_s) # S로 들어오는 엣지들에 대한 dfs

answer = 0
for i in range(1,n+1):
    if from_s[i] and from_t[i] and to_s[i] and to_t[i]: # 출퇴근길에서 모두 방문 가능한 길
        answer += 1

answer -= 2 # answer: S와 T도 방문 가능한 노드로 카운트 -> 해당 노드들은 빼주기
print(answer)