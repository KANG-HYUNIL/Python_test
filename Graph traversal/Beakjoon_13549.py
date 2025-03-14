#백준 13549번 숨바꼭질 3

from collections import deque
import sys
import heapq


input = sys.stdin.readline

N, K = map(int, input().split()) #수빈이의 위치 N, 동생의 위치 K

INT_MAX = 100001 #최대값

#최단 소요 시간 배열
Time = [INT_MAX] * 100001

min_heap = [] #우선순위 큐

#해당 지점이 점 범위 내에 들어가는지 검증
def check(x):

    return 0 <= x < 100001


#사고 회로 돌려보기
#5 -> 17로 가는 예제 
#(0, 5) 에서 시작
#(1, 4) , (1, 6), (0, 10) 들어감
#그 후에 우선순위 큐로 (0, 10) 나옴
#(1, 4), (1, 6), (1, 9), (1, 11), (0, 20) 들어감
#그 후에 우선순위 큐로 (0, 20) 나옴
#(1,4), (1, 6), (1, 9), (1, 11), (1, 19) 
#그 후에 우선순위 큐로 (1, 4) 나옴
#(1, 6), (1, 9), (1, 11), (1, 19), (1, 8), (2, 3) 들어감, (2, 5)는 이미 (0, 5)라는 최단거리가 있기에 안들어감
#이렇게 반복... (2, 17)이 나올 때 까지.

def dijkstra(start, end):

    #(시간, 노드) 형태로 저장
    heapq.heappush(min_heap, (0, start)) #시작점을 우선순위 큐에 넣음
    Time[start] = 0 #시작점의 시간은 0

    while min_heap:
        
        time, node = heapq.heappop(min_heap) #우선순위 큐에서 노드를 꺼냄

        #도착점에 도달했다면 시간을 반환
        if node == end:
            return time


        left_node = node - 1 #왼쪽 노드
        right_node = node + 1 #오른쪽 노드
        teleport_node = node * 2 #순간이동 노드

        #왼쪽 노드 검증
        if check(left_node):
            if Time[left_node] > time + 1:
                Time[left_node] = time + 1
                heapq.heappush(min_heap, (time + 1, left_node))

        #추출한 노드 위치가 도착점을 이미 넘었다면, 오른쪽 노드 및 순간이동 노드를 검증할 필요가 없음
        if node > end :
            continue

        #오른쪽 노드 검증
        if check(right_node):
            if Time[right_node] > time + 1 :
                Time[right_node] = time + 1
                heapq.heappush(min_heap, (time + 1, right_node))
        
        #순간이동 노드 검증
        if check(teleport_node):
            if Time[teleport_node] > time:
                Time[teleport_node] = time
                heapq.heappush(min_heap, (time, teleport_node))


answer = dijkstra(N, K) #다익스트라 알고리즘을 통해 최단 소요 시간을 구함
print(answer)

