#백준 1753번 최단경로 문제(다익스트라 알고리즘)
#i번째 줄에 시작점에서 i번 정점으로 가는 최단경로 출력, 
#시작점에서 시작점으로 가는 것은 0으로 처리.

import heapq
import sys

input = sys.stdin.readline

#정점 v, 간선 e 받기
v, e = list(map(int, input().split(sep=" ")))

#시작 정점의 번호
start_v = int(input())

#경로 미존재시 출력할 문자열
INF = "INF"

#답을 저장할 배열
answer_list = [-1] * (v + 1)
# answer_list[start_v] = 0


#간선의 가중치를 받는 과정을 단순 v*v 2차원 배열로 설정하면 메모리 초과
#인접 리스트를 활용하여 배열을 단순화시켜야 한다!

connect_list = [[] for _ in range(v + 1)]

#간선의 가중치들 입력 받기
for i in range(e):

    value = list(map(int, input().split(sep=" ")))

    #인접 리스트에 [도착 정점, 가중치] 의 형태로 간선 정보 저장하기
    connect_list[value[0]].append([value[1], value[2]])

    pass

priority_q = []

#우선순위 큐에 [시작 정점, 간선 가중치(== 0)] 형태 삽입
priority_q.append([0, start_v])
answer_list[start_v] = 0


#우선순위 배열의 길이가 0이 아닐 때
while len(priority_q) != 0:


    #시작 정점에서의 거리 값이 가장 작은 가중치 정보[정점 번호, 가중치 값] 빼오기
    value = heapq.heappop(priority_q)

    if value[0] > answer_list[value[1]]:
        continue

    #뽑아온 정점에서 갈 수 있는 정점 정보들 접근
    for i in connect_list[value[1]]:

        #뽑아온 정점으로 가는 최단거리 값이 정답 배열에 기록되지 않아있다면
        if answer_list[i[0]] == -1:

            #정답 배열의 값 갱신
            answer_list[i[0]] = i[1] + value[0]

            #우선순위 큐에 [정점 번호, 정답 배열의 값] 의 형태로 추가
            # priority_q.append([i[0], answer_list[i[0]]])
            heapq.heappush(priority_q, [answer_list[i[0]], i[0]])

        #이미 정답 배열에 저장된 값이 존재한다면
        elif answer_list[i[0]] != -1:

            #이미 정답 배열에 저장된 값이 더 작다면(효율적이라면)
            if answer_list[i[0]] <= value[0] + i[1]:
                
                pass

            #계산해 새로 나온 값이 이미 정답 배열에 저장된 값보다 작다면(효율적이라면)
            elif answer_list[i[0]] > value[0] + i[1]:

                #정답 배열의 값 갱신
                answer_list[i[0]] = i[1] + value[0]
                heapq.heappush(priority_q, [answer_list[i[0]], i[0]])


#정답 출력문 
for i in range(1, v + 1):
    
    if answer_list[i] == -1:
        print(INF)
    else:
        print(answer_list[i])





