#백준 1753번 최단경로 문제(다익스트라 알고리즘)
#i번째 줄에 시작점에서 i번 정점으로 가는 최단경로 출력, 
#시작점에서 시작점으로 가는 것은 0으로 처리.

from collections import deque
import heapq

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

#정점들간의 간선의 가중치를 저장할 2차원 배열, -1이면 연결이 안되어 있다는 것
connect_list = [[-1 for _ in range(v + 1)] for _ in range(v + 1)]

#간선의 가중치들 입력 받기
for i in range(e):

    value = list(map(int, input().split(sep=" ")))


    connect_list[value[0]][value[1]] = value[2]

    pass

priority_q = []

    
priority_q.append(start_v)



#우선순위 배열의 길이가 0이 아닐 때
while len(priority_q) != 0:

    #우선순위 큐를 임시로 deque 형태로 변환()
    # dq = deque(priority_q)

    #시작 정점에서의 거리 값이 가장 작은 가중치 정보 빼오기
    value = heapq.heappop(priority_q)



    for i in range(1, v + 1):

        #배온 간선과 연결되어 있다면
        if connect_list[value][i] != -1:

            #연결되어 있는 점의 최단 거리가 기록되어 있지 않다면
            if answer_list[i] == -1: #

                #최단거리 기록
                answer_list[i] = answer_list[value] + connect_list[value][i]

                #배열에 [정점 번호, 정답 배열의 값] 의 형태로 저장
                heapq.heappush(priority_q, i)
                #priority_q.append(i)

            #연결되어 있는 점의 최단 거리가 이미 기록되어 있다면
            elif answer_list[i] != -1:

                #이미 기록되어 있는 거리와, value 점을 거쳐 가는 거리 중 작은 값 저장
                answer_list[i] = min(answer_list[i], answer_list[value] + connect_list[value][i])

    priority_q = sorted(priority_q, key=lambda x : answer_list[x])


    
    
#시작 정점의 정답 값 0으로 설정
answer_list[start_v] = 0

#정답 출력문 
for i in range(1, v + 1):
    
    if answer_list[i] == -1:
        print(INF)
    else:
        print(answer_list[i])





