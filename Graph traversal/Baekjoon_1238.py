#백준 1238번 파티


import sys
import heapq

input = sys.stdin.readline
INT_MAX = int(1e9) #무한대 값

#입력 처리
N, M, X = map(int, input().split())

#단방향 도로 비용 그래프
graph = [[] for _ in range(N+1)]

for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost]) #시작 노드 idx에, (도착 노드, 비용) 형태로 저장

answer = 0 #정답을 저장할 변수

distance = [[INT_MAX] * (N+1) for _ in range(N+1)] #출발지에서 도착지까지의 최단거리를 저장할 배열

#Start_node에서 End_node로 가는 최소 비용을 계산해 반환하는 dijkstra 알고리즘 메서드드
def dijkstra(start_node, end_node):
    min_heap = [] #최단거리 추출용 Min Heap

    distance[start_node][start_node] = 0 #시작 노드의 거리는 0으로 설정
    heapq.heappush(min_heap, (distance[start_node][start_node], start_node)) #시작 노드를 힙에 삽입

    while min_heap :
        cur_cost, cur_node = heapq.heappop(min_heap) #힙에서 노드를 꺼내옴

        #min heap에서 나온 cur_node가 End_Node와 같다는 것은, 이미 End_Node로 가는 최단거리를 구했다는 의미다
        if cur_node == end_node:
            #print(start_node, end_node, cur_cost) 
            return cur_cost #Start에서 End로 가는 최단거리 반환

        for next_node, next_cost in graph[cur_node]: #현재 노드에서 이동할 수 있는 노드들을 탐색
            cal_cost = cur_cost + next_cost #다음 노드로 가는 비용 계산

            #Start_node에서 next_node로 이동하는 데에 필요한 기록된 최소 비용이 새로 계산한 비용보다 크다면면
            if distance[start_node][next_node] >= cal_cost :
                distance[start_node][next_node] = cal_cost # 최소 비용 갱신
                heapq.heappush(min_heap, (distance[start_node][next_node], next_node))

            

    return INT_MAX #while 문 내에서 처리가 되지 않을 경우에, 우선적으로 INT_MAX 반환하게 함

for i in range(1, N + 1):

    home_to_party = dijkstra(i, X) #i번째 집에서 파티 장소 X로 가는 최소 비용
    party_to_home = dijkstra(X, i) #파티 장로 X에서 i번째 집으로 돌아가는 최소 비용용

    answer = max(answer, home_to_party + party_to_home)

#print(distance)
print(answer)