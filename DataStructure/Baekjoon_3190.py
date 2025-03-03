#백준 3190번 뱀 자료구조 문제
#머리가 꺾은 뒤에, 몸은 꺾은 위치에 도달하기 전까지는 기존 이동을 유지해야 한다
#기존 방향의 이동을 유지하다가, 머리가 꺾은 지점에 도달해서야 꼬리도 꺾게 될 것이다다




import copy
from collections import deque #deque 쓰기 위해

#문제에서 첫 번째를 행으로 취급하고 있었다(y축)
RIGHT = [0, 1]
LEFT = [0, -1]
DOWN = [1, 0]
UP = [-1, 0]

time = 0

N = int(input()) #보드의 크기
K = int(input()) #사과의 개수

apple_list = [] #사과의 위치를 저장할 리스트
corner_list = [] #뱀의 꺾인 지점을 저장할 리스트, 어느 지점에서, 어느 방향으로, 어느 시간에 회전을 시도하는지 차례로 기록되어 있음음

for i in range(K) :

    X, Y = map(int, input().split()) #사과의 위치
    apple_list.append([X, Y]) #사과의 위치를 리스트에 저장

L = int(input()) #뱀의 방향 변환 횟수

for i in range(L):

    X, C = input().split() #뱀의 방향 변환 정보

    corner_list.append([int(X), C]) #뱀의 꺾인 지점을 리스트에 저장

cur_head = [1, 1]
cur_direction = copy.deepcopy(RIGHT) # 현재 이동 방향, + 면 우측 혹은 상단 - 면 좌측 혹은 하단단
tail_direction = copy.deepcopy(RIGHT)



snake_list = [[1, 1]] #뱀의 몸통을 저장할 리스트
snake_list = deque(snake_list) #뱀의 몸통을 저장할 리스트를 deque로 변환

corner_list = deque(corner_list) #꺾인 지점을 저장할 리스트를 deque로 변환

#실 소요 시간 연산 로직    


while True :
    error = False
    time += 1

    #머리 먼저 이동
    cur_head[0] += cur_direction[0]
    cur_head[1] += cur_direction[1]

    snake_list.append(copy.deepcopy(cur_head)) #머리의 위치를 몸통 리스트에 추가

    if (len(corner_list) != 0) :

        if corner_list[0][0] == time :

            if corner_list[0][1] == 'L' :
                if cur_direction == RIGHT :
                    cur_direction = copy.deepcopy(UP)
                elif cur_direction == LEFT :
                    cur_direction = copy.deepcopy(DOWN)
                elif cur_direction == UP :
                    cur_direction = copy.deepcopy(LEFT)
                elif cur_direction == DOWN :
                    cur_direction = copy.deepcopy(RIGHT)


            if corner_list[0][1] == 'D' :
                if cur_direction == RIGHT :
                    cur_direction = copy.deepcopy(DOWN)
                elif cur_direction == LEFT :
                    cur_direction = copy.deepcopy(UP)
                elif cur_direction == UP :
                    cur_direction = copy.deepcopy(RIGHT)
                elif cur_direction == DOWN :
                    cur_direction = copy.deepcopy(LEFT)
        
            corner_list.popleft()


    #머리가 보드 밖으로 나가면 게임 종료
    if cur_head[0] <= 0 or cur_head[0] > N or cur_head[1] <= 0 or cur_head[1] > N :
        error = True
        break

    #머리가 몸과 부딪혔는지 검증하는 로직직
    #꼬리에서 시작하여서, 현재 시간과 비교하여 꺾임 지점 포인트와 포인트의 사이(몸통이겠지)
    #사이 안에 머리가 위치하는지를 검증해야 함. 만약에 위치하면 게임 종료
    #주의점 : 먼저 몸의 길이를 증가시킨 후에, 충돌을 구분하는 에러 처리 후, 그 후에 사과를 판정해 몸길이를 조정함함
    for i in range(len(snake_list) - 1) :

        #만약 현재 머리의 위치가 뱀이 위치한 타일일 경우에 에러 처리
        if cur_head == snake_list[i] :
            error = True
            break


    #에러 검증 시에 게임 종료
    if(error):
        break

    apple = False

    #사과와 머리의 충돌 판정, 충돌 시에 사과를 제거하고 꼬리는 이동을 시키지 말아야 함
    for i in range(len(apple_list)) :

        #현재 머리의 위치가 사과의 위치와 동일할 경우에, 사과를 제거하고 꼬리 이동을 하지 않아야 함
        if cur_head[0] == apple_list[i][0] and cur_head[1] == apple_list[i][1] :
            apple_list.pop(i) #먹은 사과 제거
            apple = True #사과 먹음 표시
            break #한 번 먹었으면 또 먹을수는 없기에 break



    #사과가 없다면 꼬리 이동
    if apple == False :

        snake_list.popleft() #꼬리의 위치를 제거
    
    # print("time")
    # print(time)

    # print("snake list")
    # print(list(snake_list))

    # print("apple")
    # print(apple_list)

    # print("head direction")
    # print(cur_direction)

    # print("-----------------")

print(time) #게임이 종료되는 시간 출력    






