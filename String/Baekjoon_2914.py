#백준 2941번 크로아티아 알파벳

# 맨날 알고리즘 풀다가 기초 문자열 처리에 된통 당해서, 문자열도 조금씩 해보자
# 아 이씨..
# 쉬운 문제부터, 문자열 문제들은 다 푸는 방법은 머릿속에 있어도, 
# 필요한 함수가 바로바로 안나오는게 곤란했으니.

import sys # 입출력 속도 향상


#접근 방법이 솔직히 감이 잘 안온다. 
# 크로아티아 알파벳 목록들을 다 미리 가지고 있어야 하나?

C_Alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 알파벳 목록

# 우선 입력을 받아야겠지.
N = sys.stdin.readline().rstrip() # 입력받은 문자열

STAR = '*' # 크로아티아 알파벳을 나타내는 별표 문자

N_len = len(N) # 입력받은 문자열의 길이

cur_pos = 0 # 현재 위치를 나타내는 변수

for i in range(N_len):

    # 현재 위치가 이미 문자열의 길이와 같아졌다면, 의미가 없음 break
    if cur_pos >= len(N):
        break

    cur_char = N[cur_pos] # 현재 문자

    # 현재 문자가 크로아티아 알파벳 목록에 있는지 확인
    for j in range(len(C_Alphabet)):

        # 포함 여부 확인, 안되어 있으면 다음 루프
        if not cur_char == C_Alphabet[j][0]:
            continue
        
        # 현재 문자가 크로아티아 알파벳 목록에 있는데, 비교해보니 길이가 안맞으면 다음 루프
        if not cur_pos + len(C_Alphabet[j]) <= len(N): # 현재 위치 + 크로아티아 알파벳의 길이가 문자열의 길이보다 작거나 같으면
            continue
        
        # 크로아티아 알파벳 목록에 있는 문자와 현재 문자가 같으면
        if N[cur_pos:cur_pos + len(C_Alphabet[j])] == C_Alphabet[j]:
            
            # 크로아티아 알파벳을 교체해주어야 겠지
            N = N[:cur_pos] + STAR + N[cur_pos + len(C_Alphabet[j]):]

    cur_pos += 1 # 현재 위치를 1 증가시켜준다.

print(len(N)) # 크로아티아 알파벳을 별표 문자로 바꾼 문자열의 길이를 출력한다.