#백준 1202번 보석 도둑
#가방 무게가 적은 것 부터 연산을 해야 하나?
#그렇다면 가방을 입력받은 후에 가방 무게가 낮은 순으로 정렬해서 deque에 넣어 관리?>
#가방의 무게 한계보다 무게가 같거나 낮은 보석들만을 모아서, Max heap을 통해 그 보석을 얻어야 한다


import sys
import heapq
from collections import deque

#현재 가방의 무게 한계보다 무게가 낮거나 같은 보석들 중에서,
#가치가 가장 높은 보석을 얻어야 하는데,
#최대 힙을 2차원 배열에 적용해야 한다?
#무게 순으로 가방을 정렬하고, 루프를 통해 보석 리스트를 추려내서,
#추려낸 보석들을 Max Heap에 넣어 바로 처리하기? 
#처리한 후에는 그 보석을 보석 리스트에서 제거해야?

N, K = map(int, sys.stdin.readline().split())
jewel = [] #보석 무게, 가치
bag = [] #가방 무게

answer = 0
temp = []


#보석 정보 입력
for i in range(N):

    M, V = map(int, sys.stdin.readline().split())
    jewel.append([M, V])

#가방 정보 입력
for i in range(K):
    bag.append(int(sys.stdin.readline()))

#가방과 보석 배열 정렬
bag.sort()
jewel.sort(key = lambda x : x[0]) #2차원 배열은 보석의 무게 순으로.
jewel = deque(jewel)

for i in range(len(bag)) :

    while len(jewel) > 0:
        #가방의 무게 한계보다 무게가 낮은 보석이 나오면 루프를 빠져나간다
        if bag[i] < jewel[0][0]:
            break

        heapq.heappush(temp, jewel[0][1] * -1)
        jewel.popleft()


    if len(temp) > 0 :
        answer += heapq.heappop(temp) * -1

print(answer)