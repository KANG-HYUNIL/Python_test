#백준 1916번 최소비용 구하기

import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

#버스 노선 비용
graph = [[] for _ in range(N+1)]

#최단 거리 추출 용 Min Heap
min_heap = []

#출발지에서 도착지까지 최단거리 저장할 배열
distance = [INF] * (N+1)

#입력 처리리
for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])  #시작 노드에서 도착 노드까지의 비용을 저장

#출발지와 도착지 입력
Start_Node, End_Node = map(int, input().split())

#실 연산 로직 수행
distance[Start_Node] = 0 #시작 노드의 거리는 0으로 설정

heapq.heappush(min_heap, (distance[Start_Node], Start_Node)) #시작 노드를 힙에 삽입

#다익스트라 알고리즘 수행, min_heap이 비어있다면 이미 모든 최단거리를 획득했다는 의미미
while min_heap:
    dist, cur_node = heapq.heappop(min_heap) #힙에서 노드를 꺼내옴

    #min heap에서 나온 cur_node가 End_Node와 같다는 것은, 이미 End_Node로 가는 최단거리를 구했다는 의미다
    #(min heap을 이용하기에, 저장된 거리가 최소인 것만 나옴옴)
    #이 이상 연산을 하는 것은 문제에는 필요가 사실 없는 부분임
    if cur_node == End_Node:
        break

    #현재 노드에서 이동할 수 있는 버스들을 탐색
    for bus in graph[cur_node]: 
        next_node, next_cost = bus
        cal_cost = dist + next_cost #현재 노드에서 다음 노드까지의 비용 계산

        #현재 루프 기준에서 최단거리인지 아닌지 확인
        if cal_cost < distance[next_node]:
            distance[next_node] = cal_cost #최단거리 갱신
            heapq.heappush(min_heap, (cal_cost, next_node)) #힙에 삽입

print(distance[End_Node]) #도착지의 최단거리 출력

#시간초과가 발생하였다. N은 1000, M은 100000 까지 가능하다
#입출력 처리에서 시간을 줄일 수는 없으니, 다익스트라 알고리즘을 수행하는 while 문에서 단축을 시도
#Min Heap 쓰는 다익스트라에서, 루프에 의해 특정 노드로 가는 최단거리를 구했다면, 그 값은 확정적 아닌가?