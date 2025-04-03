#백준 14891번 톱니바퀴

#문제가 좀 괴랄해보이나, 이해하면 복잡하지는 않다.
# 자, 차근차근 해보자

#전제 조건: 톱니바퀴는 4개가 존재. 8개 방향, 45도 각도 씩. +자와 X자 합친 꼴 보면 됨.
#톱니바퀴 4개는 왼쪽부터 1, 2, 3, 4번을 가지게 된다.
# 톱니바퀴는 시계/반시계 방향으로 회전 가능
# 톱니바퀴는 1-2-3-4 형태로 이어져있음
# 톱니바퀴 회전 시에, 연결된 곳이 동일 극성이라면 반대 방향으로 이동한다.
# 이는 연쇄적으로 일어날 수 있다.


import sys

input = sys.stdin.readline
from collections import deque

#톱니들 정보를 보관할 것들은 deque와 리스트를 활용해서, popleft와 pop 이용해 회전 느낌 이요
# 0번 인덱스부터 하여서 7번까지가 톱니를 의미하게
# 시계/반시계 회전 메서드 관리
# 회전은 연쇄적이나, 사실상 동시이기에 주의 필요

#톱니바퀴는 4개만 있음, 단순 입력 처리로 우선 해결ㅇㅇ
first = deque(list(map(int, list(input().strip())))) #톱니바퀴 1번
second = deque(list(map(int, list(input().strip())))) #톱니바퀴 2번
third = deque(list(map(int, list(input().strip())))) #톱니바퀴 3번
fourth = deque(list(map(int, list(input().strip()))))#톱니바퀴 4번

T = [first, second, third, fourth] #톱니바퀴 리스트로 관리

#N, S극 매직넘버 
N = 0
S = 1

#톱니바퀴 정보가 12시부터 시계 방향임
TOP = 0
RIGHT = 2 #2번 idx는 우측을 의미하게 됨
LEFT = 6 #6번 idx는 좌측을 의미하게 됨

CLOCKWISE = 1 #시계 방향 회전
COUNTER_CLOCKWISE = -1 #반시계 방향 회전

NO_EFFECT = 0
LEFT_EFFECT = -1 #왼쪽 톱니바퀴에 영향을 미침
RIGHT_EFFECT = 1 #오른쪽 톱니바퀴에 영향을 미침


# 톱니바퀴 회전 및 영향 처리 메서드드
def rotate(target, direction, effect):

    if target < 0 or target > 3: #톱니바퀴 인덱스 범위 초과 시에
        return
    
    left_target = target - 1 #왼쪽 톱니바퀴 인덱스
    right_target = target + 1 #오른쪽 톱니바퀴 인덱스
    
    if effect == NO_EFFECT: #톱니바퀴 회전 시에 영향이 없다면

        #왼쪽부터 보자
        if left_target >= 0:

            #왼쪽이면, 현재 톱니의 9시와 왼쪽 톱니의 3시를 비교해야 한다. 같다면
            if T[target][LEFT] != T[left_target][RIGHT]:
                rotate(left_target, direction * -1, LEFT_EFFECT) #왼쪽 톱니바퀴에 영향을 미친다.

        #그 후 오른쪽
        if right_target <= 3:

            #오른쪽이면, 현재 톱니의 3시와 왼쪽 톱니의 9시를 비교해야 한다. 같다면
            if T[target][RIGHT] != T[right_target][LEFT]:
                rotate(right_target, direction * -1, RIGHT_EFFECT) #오른쪽 톱니바퀴에 영향을 미친다.

    elif effect == LEFT_EFFECT: #왼쪽 톱니바퀴에 영향을 미친다면
        #왼쪽부터 보자
        if left_target >= 0:

            #왼쪽이면, 현재 톱니의 9시와 왼쪽 톱니의 3시를 비교해야 한다. 같다면
            if T[target][LEFT] != T[left_target][RIGHT]:
                rotate(left_target, direction * -1, LEFT_EFFECT) #왼쪽 톱니바퀴에 영향을 미친다.

    elif effect == RIGHT_EFFECT: #오른쪽 톱니바퀴에 영향을 미친다면
            #그 후 오른쪽
        if right_target <= 3:

            #오른쪽이면, 현재 톱니의 3시와 왼쪽 톱니의 9시를 비교해야 한다. 같다면
            if T[target][RIGHT] != T[right_target][LEFT]:
                rotate(right_target, direction * -1, RIGHT_EFFECT) #오른쪽 톱니바퀴에 영향을 미친다.
    
    #영향 처리 후, target 톱니 회전 처리
    if direction == CLOCKWISE:
        T[target].appendleft(T[target].pop())    

    elif direction == COUNTER_CLOCKWISE:
        T[target].append(T[target].popleft())
    
    pass


K = int(input()) #회전 횟수 입력 받기

for i in range(K):

    target, direction = map(int, input().split()) #회전할 톱니바퀴와 방향 입력 받기
    target -= 1 ##인덱스 맞추기 위해 -1 해주기
    #target 회전 및 연쇄작용 처리리

    rotate(target=target, direction=direction, effect=NO_EFFECT) #톱니바퀴 회전 및 영향 처리 메서드 호출

#점수 처리
answer = 0

for i in range(4):
    if T[i][TOP] == S: #톱니바퀴의 12시 방향이 S극이라면
        answer += (2 ** i) #점수 처리

print(answer)
