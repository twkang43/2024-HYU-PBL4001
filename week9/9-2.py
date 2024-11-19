# [HSAT 5회 정기 코딩 인증평가 기출] 성적 평가
import sys

def compute_rank(competition):
    rank = 1 # 순위
    overlap = 1 # 중복되는 해당 점수의 수
    sorted_score = sorted(scores[competition], reverse=True)
    
    ranks[competition][sorted_score[0]] = rank # 첫 점수 -> 무조건 1위
    for i in range(1,N): # 두번째부터 마지막까지
        if sorted_score[i-1] == sorted_score[i]: # 점수가 중복되는 경우
            overlap += 1
        else: # 점수가 중복되지 않는 경우
            rank += overlap
            overlap = 1
        
        ranks[competition][sorted_score[i]] = rank

# main
N = int(input())
scores = [list(map(int, input().split())) for _ in range(3)]
final_score = [sum(scores[i][j] for i in range(3)) for j in range(N)]
scores.append(final_score)

ranks = [dict() for _ in range(4)] # 점수에 대한 순위 기록

for i in range(4): # 점수에 대한 순위 계산
    compute_rank(i)
    
for i in range(4):
    for j in range(N): # 점수에 대한 순위를 참가자에 대한 순위로 변환
        print(ranks[i][scores[i][j]], end=' ')
    print()