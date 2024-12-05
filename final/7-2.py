# [HSAT 3회 정기 코딩 인증평가 기출] 플레이페어 암호
import sys

# LL -> LX LO
# XX -> XQ XY
# 마지막 글자 -> 마지막 글자 + X
# X (마지막) -> XX
# HELLOWORLD -> HE LX LO WO RL DX
# XXYYY -> XQ XY YX YX
def parse_message(message):
    parsed_message = []
    
    i = 0
    while i < len(message):
        if i == len(message)-1: # 마지막 한 문자가 남은 경우
            parsed_message.append([message[i],'X'])
            i += 1 # while문 종료 조건
        else:
            if message[i] == message[i+1]: # 연속된 두 문자가 같은 경우
                parsed_message.append([message[i], 'Q' if message[i] == 'X' else 'X'])
                i += 1
            else:
                parsed_message.append([message[i], message[i+1]])
                i += 2
    
    return parsed_message

def find_location(char):
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == char:
                return i,j

# 두 문자가 같은 행 -> 각 문자 아래로 한 칸 이동
# 두 문자가 같은 열 -> 각 문자 오른쪽으로 한 칸 이동
# 두 문자 다른 열 & 행 -> 칸의 열이 서로 교환된 위치에 적힌 글자로 암호화
def encrypt_message(parsed_message):
    encrypted_message = []
    
    for pair in parsed_message:
        first,second = pair
        
        first_x,first_y = find_location(first)
        second_x,second_y = find_location(second)
        
        new_first,new_second = '',''
        if first_x == second_x: # 두 문자가 같은 행
            new_first = key_matrix[first_x][(first_y+1)%5]
            new_second = key_matrix[second_x][(second_y+1)%5]
        elif first_y == second_y: # 두 문자가 같은 열
            new_first = key_matrix[(first_x+1)%5][first_y]
            new_second = key_matrix[(second_x+1)%5][second_y]
        else: # 두 문자 다른 열 & 행
            new_first = key_matrix[first_x][second_y]
            new_second = key_matrix[second_x][first_y]
            
        encrypted_message.append(new_first)
        encrypted_message.append(new_second)
        
    return encrypted_message
                
# main
message = input()
keys = list(set(input()))

key_matrix = [['' for _ in range(5)] for _ in range(5)]

for i in range(ord('A'), ord('Z')+1):
    char = chr(i)
    if (char not in keys) and (char != 'J'): # key로 주어진 알파벳을 제외한 알파벳들을 keys 뒤에 붙임
        keys.append(char)

for i in range(5):
    for j in range(5):
        key_matrix[i][j] = keys[5*i+j] # 5x5 key matrix 구성
        
parsed_message = parse_message(message)
encrypted_message = encrypt_message(parsed_message)

for char in encrypted_message:
    print(char, end='')
print()