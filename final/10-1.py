# [HSAT 6회 정기 코딩 인증평가 기출] 염기서열 커버
import sys

def merge(sequence1, sequence2):
    if (sequence1 == []) or (sequence2 == []): # 초염기서열이 하나라도 존재하지 않는 경우 -> 합칠 수 없기에 빈 배열 return
        return []
    
    merged_sequence = []
    for i in range(M):
        if sequence1[i] == '.': # 첫번째 염기서열의 DNA가 와일드카드인 경우 -> 두번째 염기서열의 초염기서열 그대로 사용
            merged_sequence.append(sequence2[i])
        elif sequence2[i] == '.': # 두번째 염기서열의 DNA가 와일드카드인 경우 -> 첫번째 염기서열의 초염기서열 그대로 사용
            merged_sequence.append(sequence1[i])
        elif sequence1[i] == sequence2[i]: # 두 염기서열의 DNA가 같은 경우 -> 공통으로 가지는 DNA로 초염기서열에 추가
            merged_sequence.append(sequence1[i])
        else: # 두 염기서열의 DNA가 일치하지 않는 경우 -> 합칠 수 없기에 빈 배열 return
            return []
    
    return merged_sequence

def generate_super_sequence(binary_index):
    location = 0
    
    tmp_index = binary_index
    while tmp_index%2 == 0: # ex. N=5, 01011 -> {01010 / 00001}
        tmp_index = tmp_index//2
        location += 1
    
    # 이미 계산된 작은 super_sequence에 새로 활성화된 sequence를 더함 
    super_sequence[binary_index] = merge(sequence[location], super_sequence[binary_index-(2**location)])
    
def get_answer(binary_index):
    if answer[binary_index] < N+1: # 이미 index의 초염기서열 개수를 구한 경우
        return answer[binary_index]
    
    bit1 = [] # 활성화된 염기서열의 위치, ex. 101101 -> bit1 = [5,3,2,0]
    number1 = number2 = 0
    tmp_index = binary_index
    
    for i in range(N): # 뒤에서부터 활성화된 염기서열들의 위치를 저장
        if tmp_index%2 == 1:
            bit1.append(i)
            number2 += 2**i # number1 + number2 == binary_index
        tmp_index = tmp_index//2
        
    digit = [0]*len(bit1) # 아래의 for loop에서 1씩 incremental, binary_index를 구성하는 모든 조합 체크 ex) 01101 -> (00001,01100), (00101,01000), (01101, 00000)
    for i in range(1, 2**(len(bit1)-1)): # 활성화된 비트들의 모든 부분집합 조합을 탐색, number1에서 나온 수가 number2에 나올 수 있음 -> 절반만 수행
        for j in range(len(bit1)): # 비트마스크를 두 부분집합으로 분할
            if digit[j] == 1: # bit1의 [j] 비트를 선택 해제
                digit[j] = 0
                tmp = 2**bit1[j]
                number1 -= tmp
                number2 += tmp
            else: # bit1의 [j]번째 비트를 새로 선택
                digit[j] = 1
                tmp = 2**bit1[j]
                number1 += tmp
                number2 -= tmp
                break # 덧셈 종료
        tmp = get_answer(number1) + get_answer(number2) # DP (memoization)
        
        if tmp < answer[binary_index]: # 최솟값 찾기
            answer[binary_index] = tmp

# main
N,M = map(int, input().split())
sequence = [list(input()) for _ in range(N)]

super_sequence = [None]*(2**N) # 각 염기서열의 조합을 커버하는 초염기서열의 집합 (N개의 DNA들에 대한 부분집합의 개수 = 2^N)
super_sequence[0] = ['.']*M # 어떠한 DNA도 필수로 지정되지 않은 경우

for i in range(1,2**N): # ex. i = 01010(2) -> 3,1번째 염기서열을 커버하는 초염기서열
    generate_super_sequence(i)

answer = [N+1]*(2**N) # 초염기서열 개수의 최댓값: N+1 -> 해당 값으로 초기화
answer[0] = 0

for i in range(1,2**N):
    if super_sequence[i] != []: # 해당 집합의 염기서열을 모두 커버할 수 있는 하나의 초염기서열이 있는 경우
        answer[i] = 1
    else:
        get_answer(i)
        
print(answer[2**N-1]) # 모든 bit가 1인 경우가 정답