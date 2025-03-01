#문제는 쉬운게 뻔한데, 만들기가 귀찮다
#개념과 구조를 안다고 다 AI써서 만드니 그런듯
#근데 정작 이것도 만드려하니 내 생각과 거의 똑같이 copilot이 해버려서 참 이게..


import sys #아 sys 안써서 입출력 초과는 아니지 좀좀

TestCase = int(sys.stdin.readline()) #테스트 케이스 수

stack = [] #스택을 만들어준다

ZeroNum = 0 #0을 출력할 때 사용할 변수
NegativeOne = -1 #-1을 출력할 때 사용할 변수

for i in range(TestCase):
    command = sys.stdin.readline().strip().split() #명령어를 입력받는다

    if command[0] == 'push': #push 명령어를 받았을 때
        stack.append(command[1]) #스택에 추가한다
        continue

    if command[0] == 'pop': #pop 명령어를 받았을 때
        if len(stack) == 0: #스택이 비어있을 때
            print(NegativeOne) #-1을 출력한다
        else: #스택이 비어있지 않을 때
            print(stack.pop()) #스택의 맨 위에 있는 값을 출력하고 제거한다
        continue

    if command[0] == 'size': #size 명령어를 받았을 때
        print(len(stack)) #스택의 길이를 출력한다
        continue

    if command[0] == 'empty': #empty 명령어를 받았을 때
        if len(stack) == 0: #스택이 비어있을 때
            print(1) #1을 출력한다
        else: #스택이 비어있지 않을 때
            print(ZeroNum) #0을 출력한다
        continue

    if command[0] == 'top': #top 명령어를 받았을 때
        if len(stack) == 0: #스택이 비어있을 때
            print(NegativeOne) #-1을 출력한다
        else: #스택이 비어있지 않을 때
            print(stack[-1]) #스택의 맨 위에 있는 값을 출력한다
        continue



