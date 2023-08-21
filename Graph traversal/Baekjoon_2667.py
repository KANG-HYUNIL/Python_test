#백준 2667 단지 번호 붙이기

import sys
sys.setrecursionlimit(10**6)

#지도의 크기 N 받기
n = int(input())

#각 단지의 수, 집, 단지의 개수를 담을 변수 선언
answer = []

Map = []

count = 0

#집 받기
for i in range(n) :

    Map.append(list(map(int, input())))


#각각 우, 좌, 상, 하 의 이동을 표현함
Dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

#각각 정의된 단지의 집 수를 담을 변수, 한번의 단지가 끝난 후 초기화시켜주어야 한다.
global mid_answer
mid_answer = 0


#재귀를 이용한 DFS 풀이방법 채택, 한 집에서 갈 수 있는 모든 방향 탐색
#매개변수로 x, y의 좌표값을 넣어준다
def DFS(x, y):

    global mid_answer

    #좌표 (x, y)에 집이 있는지 없는지 확인    
    if Map[y][x] == 1:
        mid_answer += 1
        
        Map[y][x] = 0
    
        #좌표 (x, y) 집의 상, 하, 좌, 우 확인하기
        for i in Dir:
            Dir_x, Dir_y = i[0], i[1]

            #다음 이동의 x, y 좌표 정의
            next_x = x + Dir_x
            next_y = y + Dir_y

            #x, y 가 적정 idx 범위(0 ~ n - 1)을 벗어나지 않게 관리해주기
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:

                pass

            #범위 적정 시, 그쪽으로 재귀하기
            else:               
                
                DFS(next_x, next_y)

        return True
    
    #Map[y][x] 가 1이 아닐 경우, 혹은 주변에 집이 없을 경우 False
    return False



#같은 단지를 확인 못하는 경우를 피하기 위해, 따로 확인을 거쳐야한다?
for x in range(n):
    for y in range(n):


        if DFS(x, y) == True:
            

            answer.append(mid_answer)
            count += 1
            mid_answer = 0








print(count)
answer.sort()

print(*answer, sep="\n")



