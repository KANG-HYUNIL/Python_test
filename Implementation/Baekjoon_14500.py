#백준 14500번 테트로미노

#문제 해결 로직을 도저히 떠올리지 못해, 여러 질문 게시판의 글을 참고해서 풀기 시작했다.
#맵의 범위가 25만? 가까이 되서, 단순 브루트 포스로 못 풀거라 생각했는데, 이게 된다고 하네.
#머리가 좀 띵.
#그래프론적으로 접근해서, dfs나 bfs로도 풀 수 있다고 하는데.

#처음에 노가다로 기본 도형에서 회전 및 뒤집기 경우의 수 모두 구하려고 했는데,
#시간 초과 당연히 나왔고
#다른 게시물 글 참고하다가, 천재같은 단순화 보고 베끼기.

import sys

input =  sys.stdin.readline

#기초 5가지 모양
poly = [
    [(0, 0), (0, 1), (0, 2), (0, 3)], # ㅡ
    [(0, 0), (0, 1), (0, 2), (1, 1)], # ㅜ
    [(0, 0), (1, 0), (0, 1), (1, 1)], # ㅁ
    [(0, 0), (1, 0), (2, 0), (2, 1)], # ㄴ
    [(0, 0), (1, 0), (1, 1), (2, 1)] # 늑 모양
]   

# 도형 회전시키기
def rotate(xy1, xy2, xy3, xy4, rotateNum):
    #xy1, xy2, xy3, xy4 = (x1, y1), (x2, y2), (x3, y3), (x4, y4)    

    #회전은 시계 방향을 기점으로 한다.

    #값 읽기
    x1, y1 = xy1[0], xy1[1]
    x2, y2 = xy2[0], xy2[1] 
    x3, y3 = xy3[0], xy3[1]
    x4, y4 = xy4[0], xy4[1]


    #0도 회전
    if rotateNum == 0:
        #회전 안함
        return [xy1, xy2, xy3, xy4]
    #90도 회전
    if rotateNum == 1:

        newX2, newY2 = x1 + (y2 - y1), y1 - (x2 - x1) 
        newX3, newY3 = x1 + (y3 - y1), y1 - (x3 - x1)
        newX4, newY4 = x1 + (y4 - y1), y1 - (x4 - x1)

        #회전 후 좌표들
        newXy1 = (x1, y1)
        newXy2 = (newX2, newY2)
        newXy3 = (newX3, newY3)
        newXy4 = (newX4, newY4)

        return [newXy1, newXy2, newXy3, newXy4]

    ##180도 회전
    if rotateNum == 2:

        newX2, newY2 = x1 - (x2 - x1), y1 - (y2 - y1)
        newX3, newY3 = x1 - (x3 - x1), y1 - (y3 - y1)
        newX4, newY4 = x1 - (x4 - x1), y1 - (y4 - y1)

        newXy1 = (x1, y1)
        newXy2 = (newX2, newY2)
        newXy3 = (newX3, newY3)
        newXy4 = (newX4, newY4)
        return [newXy1, newXy2, newXy3, newXy4]
    
    #270도 회전
    else:

        newX2, newY2 = x1 - (y2 - y1), y1 + (x2 - x1)
        newX3, newY3 = x1 - (y3 - y1), y1 + (x3 - x1)
        newX4, newY4 = x1 - (y4 - y1), y1 + (x4 - x1)
        
        #회전 후 좌표들
        newXy1 = (x1, y1)
        newXy2 = (newX2, newY2)
        newXy3 = (newX3, newY3)
        newXy4 = (newX4, newY4)

        return [newXy1, newXy2, newXy3, newXy4]



#도형 가로 선 뒤집기(0, 0) 지점을 기준으로 왼쪽으로 뒤집어버리기로 고정
def reverse(xy1, xy2, xy3, xy4):
    #xy1, xy2, xy3, xy4 = (x1, y1), (x2, y2), (x3, y3), (x4, y4)

    #값 읽기
    x1, y1 = xy1[0], xy1[1]
    x2, y2 = xy2[0], xy2[1] 
    x3, y3 = xy3[0], xy3[1]
    x4, y4 = xy4[0], xy4[1]

    #x1, y1을 기준으로 왼쪽으로 뒤집어버려야 한다 
    #다른 xy들의 좌표와 xy1의 위치 차이의 절댓값을 얻어서, 
    
    newX2 = x1 - (x2 - x1)
    newX3 = x1 - (x3 - x1)
    newX4 = x1 - (x4 - x1)

    newXy1 = (x1, y1)
    newXy2 = (newX2, y2)
    newXy3 = (newX3, y3)
    newXy4 = (newX4, y4)

    return [newXy1, newXy2, newXy3, newXy4]

#반시계 방향으로 90도 회전
def rotatePoly_90(poly):
    return [(-y, x) for (x, y) in poly]

#위로 뒤집기
def flip_h(poly):
    return [(x, -y) for (x, y) in poly]

#아래로 뒤집기
def flip_v(poly):
    return [(-x, y) for (x, y) in poly]

# 중복된거 빼기위해 정규화
def normalize(poly):
    min_x = min(x for x, y in poly)
    min_y = min(y for x, y in poly)
    return sorted((x - min_x, y - min_y) for x, y in poly)

#모든 가능한 도형의 경우의 수 포함하는 set 반환 메서드
def create_all_poly(): 
    all_poly = set() #set 생성

    #기초 도형들에 대해 도형 수 분석 시작
    for p in poly:
        #기본 도형을 복사해서 사용
        #이유는, 회전 및 뒤집기 후에 원본 도형을 변형시키면, 원본 도형이 변형되버리기 때문
        cur_poly = p[:]
        
        #회전 4번
        for i in range(4):
            rotated_poly = rotate(cur_poly[0], cur_poly[1], cur_poly[2], cur_poly[3], i) #회전
            all_poly.add(tuple(normalize(rotated_poly))) #정규화된 도형을 set에 추가

        #뒤집고
        reverse_poly = reverse(cur_poly[0], cur_poly[1], cur_poly[2], cur_poly[3]) #뒤집기

        #또 회전 4번
        for i in range(4):
            rotated_poly = rotate(reverse_poly[0], reverse_poly[1], reverse_poly[2], reverse_poly[3], i)
            all_poly.add(tuple(normalize(rotated_poly))) #정규화된 도형을 set에 추가

    return all_poly

N, M = map(int, input().split()) # 행, 열
board = [list(map(int, input().split())) for _ in range(N)] # 맵

answer = 0 

poly_set = create_all_poly() #도형들 저장할 set

for i in range(N):

    for j in range(M):

        #도형들 loop
        for p in poly_set:

            #도형의 각 칸(4개)가 이동 후 위치하는 좌표를 계산
            x1, y1 = p[0][0] + i, p[0][1] + j
            x2, y2 = p[1][0] + i, p[1][1] + j
            x3, y3 = p[2][0] + i, p[2][1] + j
            x4, y4 = p[3][0] + i, p[3][1] + j

            

            #좌표가 범위 안에 있는지 확인
            if (0 <= x1 < N and 0 <= y1 < M) and (0 <= x2 < N and 0 <= y2 < M) and (0 <= x3 < N and 0 <= y3 < M) and (0 <= x4 < N and 0 <= y4 < M):
                temp = board[x1][y1] + board[x2][y2] + board[x3][y3] + board[x4][y4] #현재 도형이 차지한 공간의 숫자 합산
                answer = max(answer, temp) #기존 값과 비교해 최댓값 갱신

print(answer)
