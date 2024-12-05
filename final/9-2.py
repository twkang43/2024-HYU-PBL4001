# [HSAT 5회 정기 코딩 인증평가 기출] 성적 평가
import sys
input = sys.stdin.readline

def compute_rank(test):
    rank = 1 # 순위
    overlap = 1 # 중복되는 해당 점수의 수
    sorted_score = sorted(scores[test], reverse=True)
    
    ranks[test][sorted_score[0]] = rank # 첫 점수 -> 무조건 1위
    for i in range(1,N):
        if sorted_score[i] == sorted_score[i-1]: # 점수가 중복되는 경우
            overlap += 1
        else: # 점수가 중복되지 않는 경우
            rank += overlap
            overlap = 1
        
        ranks[test][sorted_score[i]] = rank

# main
N = int(input())
scores = [list(map(int, input().split())) for _ in range(3)]
final_score = [sum(scores[i][j] for j in range(N)) for i in range(3)]
scores.append(final_score)

ranks = [dict() for _ in range(4)] # 각 시험에 대한 순위 기록

for i in range(4):
    compute_rank(i)
    
for i in range(4):
    for j in range(N):
        participant = scores[i][j]
        print(ranks[i][participant], end=' ')
    print()