#백준 13460번 구슬 탈출 2

#기본적으로는 그래프 탐색 문제 같은데, 좀 많이 꼬은 문제
#방문 배열을 단순히 처리하면 분명히 꼬일 것 같은데
#일단 최단 경로이니, BFS로 접근하는 편이 좋을거다
#로직 상으로는 이해가 잘 되지 않으나, 방문 배열을 2개의 구슬에 대해 모두 처리해야 한다?
#이유를 모르겠다만

from collections import deque
import sys
input = sys.stdin.readline

MAX_COUNT = 10 #최대 이동 횟수
RED = "R" #빨간 구슬
BLUE = "B" #파란 구슬
HOLE = "O" #구멍
WALL = "#" #벽


#생각해보니, 외곽은 무조건 벽이니까 굳이 입력으로 처리할 필요가 없지 않나?
N, M = map(int, input().split()) #보드의 크기
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)] #동서남북

graph = [["?"] * (M) for _ in range(N)] #보드 정보

#방문 배열을 4차원으로 해서, RED BLUE를 따로 처리하는 것이 아니라, RED & BLUE 쌍으로 해결해야 한다
# red_visited = [[False] * (M) for _ in range(N)] #빨간 구슬 방문 정보
# blue_visited = [[False] * (M) for _ in range(N)] #파란 구슬 방문 정보
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]#빨간, 파란 구슬 방문 정보
red_start = [0, 0] #빨간 구슬 시작 위치
blue_start = [0, 0] #파란 구슬 시작 위치
hole = [0, 0] #구멍 위치
answer = 0 #정답

#graph 입력 받기
for i in range(N):

    #한 줄 단위로 우선 입력
    line = input().strip()

    #그 다음은 왼쪽, 오른쪽 끝을 제외하고 입력 받기
    for j in range(M):

        #그래프에 입력
        graph[i][j] = line[j]
        
        #각 공, 구멍 시작 위치 저장
        if line[j] == RED:
            red_start = [i, j]
        
        if line[j] == BLUE:
            blue_start = [i, j]

        if line[j] == HOLE:
            hole = [i, j]

#BFS로 탐색
def BFS():

    global answer

    #빨간, 파란 구슬의 위치를 저장할 deque
    #[0]: 행, [1]: 열
    red_deq = deque()
    blue_deq = deque()

    #시작 위치 저장
    red_deq.append(red_start)
    blue_deq.append(blue_start)

    #시작 위치 방문 처리
    # red_visited[red_start[0]][red_start[1]] = True
    # blue_visited[blue_start[0]][blue_start[1]] = True

    visited[red_start[0]][red_start[1]][blue_start[0]][blue_start[1]] = True

    while True:

        #이동
        answer += 1

        #최대 이동 횟수 초과 시 -1 설정 후 break
        if answer > MAX_COUNT:
            answer = -1
            break

        #RED, BLUE 구슬 위치 가능성들 임시 배열
        temp_red = []
        temp_blue = []

        find_hole = 0 #구멍에 빠졌는지 여부, 0 : ZERO, 1 : ONLY RED, 2 : ONLY BLUE, 3 : BOTH


        while red_deq:
            
            #구슬 위치 획득
            red_cur = red_deq.popleft()
            blue_cur = blue_deq.popleft()

            #방향 이동
            for direction in dir:

                find_hole = 0 #구멍에 빠졌는지 여부, 0 : ZERO, 1 : ONLY RED, 2 : ONLY BLUE, 3 : BOTH
                
                red_next = red_cur[:] #깊은 복사
                blue_next = blue_cur[:] #깊은 복사

                #RED 이동
                while True:
                    

                    #이동
                    red_next[0] += direction[0]
                    red_next[1] += direction[1]

                    #벽 만나면 이전 위치로 되돌리고 break
                    if graph[red_next[0]][red_next[1]] == WALL:
                        red_next[0] -= direction[0]
                        red_next[1] -= direction[1]
                        break
                    
                    #구멍 만나면 break
                    if red_next == hole:
                        find_hole += 1
                        break

                    #BLUE와 만나면 이전 위치로 되돌리고 break
                    if red_next == blue_next:
                        red_next[0] -= direction[0]
                        red_next[1] -= direction[1]
                        break

                     
                
                #BLUE 이동
                while True:

                    #이동
                    blue_next[0] += direction[0]
                    blue_next[1] += direction[1]

                    #벽 만나면 이전 위치로 되돌리고 break
                    if graph[blue_next[0]][blue_next[1]] == WALL:
                        blue_next[0] -= direction[0]
                        blue_next[1] -= direction[1]
                        break
                    
                    #구멍 만나면 break
                    if blue_next == hole:
                        find_hole += 2
                        break   

                    #RED와 만나면 이전 위치로 되돌리고 break
                    if red_next == blue_next:
                        blue_next[0] -= direction[0]
                        blue_next[1] -= direction[1]
                        break
                    
                     
                    
                #RED와 BLUE의 이동 순서 때문에, RED를 한 번 더 이동 로직 수행
                #본래 동시에 이동을 시도해야 하나, 그럼 머리 아프니까 그냥
                #RED 먼저 후 BLUE, 그 후에 BLUE 때문에 이전 RED 이동에 방해가 있었을 수 있으니 한 번 더 RED 이동
                while True:
                
                    #구멍 만나면 break
                    if red_next == hole:
                        break

                    #이동
                    red_next[0] += direction[0]
                    red_next[1] += direction[1]

                    #벽 만나면 이전 위치로 되돌리고 break
                    if graph[red_next[0]][red_next[1]] == WALL:
                        red_next[0] -= direction[0]
                        red_next[1] -= direction[1]
                        break
                    
                    #구멍 만나면 break
                    if red_next == hole:
                        find_hole += 1
                        break

                    #BLUE와 만나면 이전 위치로 되돌리고 break
                    if red_next == blue_next:
                        red_next[0] -= direction[0]
                        red_next[1] -= direction[1]
                        break

                     
                
                #BLUE, 혹은 BOTH 일 경우에,
                # 이 경우는 다음 후보지에 이 next 좌표를 넣을 필요가 없음
                if find_hole > 1 :
                    continue
                
                #RED만 성공 시에 break
                if find_hole == 1 :
                    break
                
                #아직 계속 이동을 시도해야 한다면
                else :
                    #방문 여부 확인, RED와 BLUE 모두 이미 도달한 적이 있는 곳이라면
                    # if red_visited[red_next[0]][red_next[1]] and blue_visited[blue_next[0]][blue_next[1]] :
                    #     continue

                    if visited[red_next[0]][red_next[1]][blue_next[0]][blue_next[1]] :
                        continue

                    # #둘 중 하나라도 가보지 않은 곳이라면 방문 처리 후,  
                    # red_visited[red_next[0]][red_next[1]] = True
                    # blue_visited[blue_next[0]][blue_next[1]] = True
                    visited[red_next[0]][red_next[1]][blue_next[0]][blue_next[1]] = True

                    #다음 후보지 좌표에 넣기
                    temp_red.append(red_next[:])
                    temp_blue.append(blue_next[:])

            # print(temp_red)
            # print(temp_blue)

                ## direction for loop    

            #RED만 성공 시에 break
            if find_hole == 1 :
                break

            ## red_deq while loop

        #RED만 성공 시에 break
        if find_hole == 1 :
            break
        
        #다음 이동 후보지들 deq에 추가
        for red in temp_red:
            red_deq.append(red)
            # red_visited[red[0]][red[1]] = True

        #다음 이동 후보지들 deq에 추가
        for blue in temp_blue:
            blue_deq.append(blue)
            # blue_visited[blue[0]][blue[1]] = True

        
        ## True while loop

BFS()

print(answer)