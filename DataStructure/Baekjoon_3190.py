#백준 3190번 뱀 자료구조 문제
#머리가 꺾은 뒤에, 몸은 꺾은 위치에 도달하기 전까지는 기존 이동을 유지해야 한다
#기존 방향의 이동을 유지하다가, 머리가 꺾은 지점에 도달해서야 꼬리도 꺾게 될 것이다다



from os import error
import sys
import copy
from collections import deque #deque 쓰기 위해

RIGHT = [1, 0]
LEFT = [-1, 0]
DOWN = [0, 1]
UP = [0, -1]

time = 0

N = int(input()) #보드의 크기
K = int(input()) #사과의 개수

apple_list = [] #사과의 위치를 저장할 리스트
corner_list = [] #뱀의 꺾인 지점을 저장할 리스트, 어느 지점에서, 어느 방향으로, 어느 시간에 회전을 시도하는지 차례로 기록되어 있음음

for i in range(K) :

    X, Y = map(int, input().split()) #사과의 위치
    apple_list.append([X - 1, Y - 1]) #사과의 위치를 리스트에 저장

L = int(input()) #뱀의 방향 변환 횟수

for i in range(L):

    X, C = input().split() #뱀의 방향 변환 정보

    corner_list.append([int(X), C]) #뱀의 꺾인 지점을 리스트에 저장

cur_head = [0, 0]
cur_direction = [1, 0] # 현재 이동 방향, + 면 우측 혹은 상단 - 면 좌측 혹은 하단단
tail_direction = [1, 0]



snake_list = [[0, 0]] #뱀의 몸통을 저장할 리스트
snake_list = deque(snake_list) #뱀의 몸통을 저장할 리스트를 deque로 변환

tail_turn_point = [] #꼬리가 꺾인 지점을 저장할 리스트
tail_turn_point = deque(tail_turn_point) #꼬리가 꺾인 지점을 저장할 리스트를 deque로 변환

#실 소요 시간 연산 로직    

while True :
    error = False
    time += 1

    #머리 먼저 이동
    cur_head[0] += cur_direction[0]
    cur_head[1] += cur_direction[1]

    snake_list.append(copy.deepcopy(cur_head)) #머리의 위치를 몸통 리스트에 추가

    #머리의 이동 방향 회전 처리
    for i in range(len(corner_list)) :

        if time != corner_list[i][0] :
            continue

    
        if corner_list[i][1] == 'L' :
            if cur_direction == RIGHT :
                cur_direction = copy.deepcopy(DOWN)
            elif cur_direction == LEFT :
                cur_direction = copy.deepcopy(UP)
            elif cur_direction == UP :
                cur_direction = copy.deepcopy(RIGHT)
            elif cur_direction == DOWN :
                cur_direction = copy.deepcopy(LEFT)

        if corner_list[i][1] == 'D' :
            if cur_direction == RIGHT :
                cur_direction = copy.deepcopy(UP)
            elif cur_direction == LEFT :
                cur_direction = copy.deepcopy(DOWN)
            elif cur_direction == UP :
                cur_direction = copy.deepcopy(LEFT)
            elif cur_direction == DOWN :
                cur_direction = copy.deepcopy(RIGHT)
        
        #꺾인 지점, 꺾어야 하는 방향 기입
        tail_turn_point.append([copy.deepcopy(cur_head), copy.deepcopy(cur_direction)])


    #머리가 보드 밖으로 나가면 게임 종료
    if cur_head[0] < 0 or cur_head[0] >= N or cur_head[1] < 0 or cur_head[1] >= N :
        error = True
        break

    #머리가 몸과 부딪혔는지 검증하는 로직직
    #꼬리에서 시작하여서, 현재 시간과 비교하여 꺾임 지점 포인트와 포인트의 사이(몸통이겠지)
    #사이 안에 머리가 위치하는지를 검증해야 함. 만약에 위치하면 게임 종료
    for i in range(len(snake_list)) :

        #만약 현재 머리의 위치가 뱀이 위치한 타일일 경우에 에러 처리
        if cur_head == snake_list[i] :
            error = True
            break


    #에러 검증 시에 게임 종료
    if(error):
        break

    #꺾인 지점의 시간이 현재 시간보다 작다면, 충돌 검증을 진행해야 함

    apple = False

    #사과와 머리의 충돌 판정, 충돌 시에 사과를 제거하고 꼬리는 이동을 시키지 말아야 함
    for i in range(len(apple_list)) :

        #현재 머리의 위치가 사과의 위치와 동일할 경우에, 사과를 제거하고 꼬리 이동을 하지 않아야 함
        if cur_head == apple_list[i] :
            apple_list.pop(i)
            apple = True
            break



    #사과가 없다면 꼬리 이동
    if apple == False :

        snake_list.popleft() #꼬리의 위치를 제거
    

print(time) #게임이 종료되는 시간 출력    






