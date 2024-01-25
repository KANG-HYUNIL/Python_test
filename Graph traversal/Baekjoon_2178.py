#2178번 미로 찾기 (백준)
#BFS로 풀도록 노력해보자!

from collections import deque




#시작지점은 1,1 즉 0, 0 이다
#N X M 받기
n, m = list(map(int, input().split(sep=" ")))

#BFS를 위한 deque, 답을 담을 answer 변수 선언
deq = deque()

 

answer = [0] #이동 횟수를 담을 배열

#우, 좌, 상, 하 의 이동 표현
Dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

Map = [] #미로 정보를 담을 배열

#미로 정보 받기
for i in range(n) :
    Map.append(list(map(int, list(input()))))

#idx에 맞게 목표 좌표 변경
Target_n = n - 1
Target_m = m - 1



#목표 지점 도착 여부를 확인하는 변수
global Check 
Check = False


def BFS(x, y):

    global Check

    #방문 여부 표시 및 방문 횟수 증가
    Map[y][x] = 0
    answer[0] += 1

    #deque에 좌표 집어넣기
    deq.append([x, y])

    
    while True:

        sub_ary = []

        #BFS 접근, deque에 좌표가 남아있을 동안 실행
        while len(deq) != 0 :

            #가장 왼쪽 좌표 빼내기
            pop_x, pop_y = deq.popleft()


            #빼낸 좌표에서 상, 하, 좌, 우 탐색하기
            for i in Dir:
                Dir_x, Dir_y = i[0], i[1]

                next_x = pop_x + Dir_x
                next_y = pop_y + Dir_y

                #목표 지점 도착 시
                if next_x == Target_m and next_y == Target_n:
                    Check = True
                    break

                #Map 범위를 벗어나는 경우
                if next_x < 0 or next_x > Target_m or next_y < 0 or next_y > Target_n:
                    pass
                
                #지나갈 수 없거나, 이미 지나간 곳일 경우
                elif Map[next_y][next_x] == 0:
                    pass

                #갈 수 있는 경우
                else:
                    sub_ary.append([next_x, next_y]) #sub_ary에 다음 이동 좌표 삽입
                    Map[next_y][next_x] = 0 #그 좌표 지점은 방문표시 해놓기
            

            #목표 지점에 도착했다면, break
            if Check == True:   
                break

        answer[0] += 1

        if Check == True:   
                break
            
        

        for point in sub_ary:
            deq.append(point)

 
 

BFS(0, 0)

print(answer[0])


