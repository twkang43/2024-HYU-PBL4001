# [HSAT 인증평가 1회] 차세대 지능형 교통시스템

directions = [[],
              [0,1,2], # 1
              [0,1,3], # 2 
              [0,2,3], # 3
              [1,2,3], # 4
              [0,1], # 5
              [0,3], # 6
              [2,3], # 7
              [1,2], # 8
              [1,2], # 9
              [0,1], # 10
              [0,2], # 11
              [2,3], # 12
              ]

visit_cross = []
signals = []

N, T = map(int, input().split())

for i in range(N):
    signal = []
    for j in range(N):
        signal.append(list(map(int, input().split())))
    signals.append(signal)
    
q = []
q.append([0,0,1])
