#백준 문자열 폭발 9935번


# 단순히 in 연산자와 replace 써도 될거 같기는 한데
# 문자열 길이가 100만이라 좀 곤란하려나?
# 시간 복잡도는 O(n*m) 이고

import sys



Str_Input = sys.stdin.readline().rstrip() # 문자열
Str_Boom = sys.stdin.readline().rstrip() # 폭발 문자열

FRULA = "FRULA" # 폭발 문자열이 없을 때 출력할 문자열

answer = "" # 정답
stack = []

for s in range(len(Str_Input)):
    # answer += str(Str_Input[s]) # 문자열을 하나씩 더해준다.

    # if len(answer) >= len(Str_Boom): # 정답 문자열의 길이가 폭발 문자열보다 길어지면

    #     if answer[-len(Str_Boom):] == Str_Boom:
    #         answer = answer[:-len(Str_Boom)]  

    stack.append(Str_Input[s]) # 스택에 문자 추가

    if len(stack) >= len(Str_Boom): # 스택의 길이가 폭발 문자열보다 길어지면
        if "".join(stack[-len(Str_Boom):]) == Str_Boom:
            for _ in range(len(Str_Boom)):
                stack.pop()

answer = "".join(stack) # 스택을 문자열로 변환

if answer == "":
    print(FRULA) # 정답이 없으면 FRULA 출력\
else:
    print(answer)