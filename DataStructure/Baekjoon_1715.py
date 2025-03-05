#백준 1715번 카드 정렬하기
#큰 수가 연산에 최대한 적게 포함되게끔 해야 하나?
#그렇다면, Min heap을 통해 작은 수 먼저 빼내는 방식으로?
#제일 작은 수와 두 번째로 작은 수를 얻어내고, 그 수를 더한 후에, 다시 heap에 추가

import sys
import heapq


N = int(input()) #N개의 수 입력
heapq_list = [] #heapq list 생성
answer = 0  #정답 변수 생성

for i in range(N):

    #입력 받고
    num = int(sys.stdin.readline())
    heapq.heappush(heapq_list, num)


while len(heapq_list) > 0 :

    first_min = heapq.heappop(heapq_list) #첫번째 최소값

    #최초의 연산이라면
    if (len(heapq_list) > 0):
        second_min = heapq.heappop(heapq_list) #두 번째 최소값
        sum = first_min + second_min
        answer += sum #정답에 더하기
        heapq.heappush(heapq_list, sum) #연산 결과 저장


    else:
        break

#110, 200, 220, 420
    pass

print(answer)









