#백준 1655번 문제 : 가운데를 말해요


#아 난 실제 부른 수의 중간에 위치하는 수를 찾는 줄 알았는데,
#실은 부른 수들의 크기를 비교하여 그 크기가 중간인 값들을 찾는 문제였다
#이러니까 문제 해설들이 내가 생각하는 방법과 전부 달랐지 
#heap을 직접 구현하니 시간초과가 발생한다(heap 구현은 올바르게 되어 있음)
#시간 제한이 빡센 문제라, 사소한 부분 처리 차이 때문에 어쩔 수 없이 heapq 모듈을 써야 한다

import sys
import heapq

 
left_heap = [0] #크기가 더 작은 수들이 위치할 heap
right_heap = [0] #크기가 더 큰 수들이 위치할 heap

 

HEAP_START_IDX = 1

middle_num = 0 #가운데에 있는(2개라면 그 중 작은 수) 수

# def operation(num):

#     if len(left_heap) == len(right_heap):
#         max_heap_push(left_heap, num)
#     else:
#         min_heap_push(right_heap, num)


#     if len(right_heap) == 1:
#         return left_heap[HEAP_START_IDX]


#     #left heap의 가장 위쪽 값은 전체 수들 중에서 중간 값을 가지고 있어야 한다.
#     #또한 right heap의 가장 위쪽 값은 left heap의 가장 위쪽 값보다 작아야 한다
#     #왜냐하면 right heap에는 중간값(left heap의 위값)보다 큰 값들을 배치할 공간이기 때문문
#     if left_heap[HEAP_START_IDX] > right_heap[HEAP_START_IDX] :

#         right_min_num = min_heap_pop(right_heap)
#         left_max_num = max_heap_pop(left_heap)
#         min_heap_push(right_heap, left_max_num)
#         max_heap_push(left_heap, right_min_num)
    
#     return left_heap[HEAP_START_IDX] #중간값 도출출

# #min heap push method
# def min_heap_push(target_heap, num) :

#     target_heap.append(num)
#     child_idx = len(target_heap) - 1
#     parent_idx = child_idx // 2

#     while child_idx > 1 and target_heap[child_idx] < target_heap[parent_idx]:

#         #값 교체체
#         a = target_heap[child_idx]
#         target_heap[child_idx] = target_heap[parent_idx]
#         target_heap[parent_idx] = a

#         #idx 재설정정
#         child_idx = parent_idx
#         parent_idx = child_idx // 2

# #max heap push method
# def max_heap_push(target_heap, num) :


#     target_heap.append(num)
#     child_idx = len(target_heap) - 1
#     parent_idx = child_idx // 2
    
#     while child_idx > 1 and target_heap[child_idx] > target_heap[parent_idx]:

#         #값 교체체
#         a = target_heap[child_idx]
#         target_heap[child_idx] = target_heap[parent_idx]
#         target_heap[parent_idx] = a

#         #idx 재설정정
#         child_idx = parent_idx
#         parent_idx = child_idx // 2

#     pass

# #min heap pop method
# def min_heap_pop(target_heap) :
    
#     #가장 위에 있는 최솟값 가져오기
#     min_num = target_heap[1]

#     #가장 아래에 있는(최댓값)을 맨 위에 올리기
#     target_heap[1] = target_heap[-1]
#     target_heap.pop() #맨 아래에 있는 값 삭제

#     #최초 부모 idx 설정정
#     parent_idx = 1
#     child_idx = parent_idx * 2

#     #자식 idx가 heap의 길이를 초과하지 않을 동안에에
#     while child_idx <= len(target_heap) - 1:

#         #자식 양쪽 여부 검증 및 작은은 값이 누구인지 검증증
#         if child_idx + 1 < len(target_heap) and target_heap[child_idx] > target_heap[child_idx + 1]:
#             child_idx += 1

#         if target_heap[parent_idx] > target_heap[child_idx]:
#             target_heap[parent_idx], target_heap[child_idx] = target_heap[child_idx], target_heap[parent_idx]
#             parent_idx = child_idx
#             child_idx = parent_idx * 2
#         else:
#             break
    
#     return min_num

    
# #max heap pop method
# def max_heap_pop(target_heap) :

#     max_num = target_heap[1]

#     target_heap[1] = target_heap[-1]
#     target_heap.pop()

#     parent_idx = 1
#     child_idx = parent_idx * 2

    
#     while child_idx <= len(target_heap) - 1:

#         if child_idx + 1 < len(target_heap) and target_heap[child_idx] < target_heap[child_idx + 1]:
#             child_idx += 1

#         if target_heap[parent_idx] < target_heap[child_idx]:
#             target_heap[parent_idx], target_heap[child_idx] = target_heap[child_idx], target_heap[parent_idx]
#             parent_idx = child_idx
#             child_idx = parent_idx * 2
#         else:
#             break

#     return max_num

N = int(input()) #N개의 수 입력
max_left_heapq = []
min_right_heapq = []

#어쩔 수 없이 heapq 모듈 사용, min heap만 지원하는 듯듯
for i in range(N):

    # #입력 받고
    # num = int(sys.stdin.readline())

    # #로직 처리 하고
    # middle_num = operation(num=num)

    # #최상단 값 출력
    # sys.stdout.write(str(middle_num) +'\n')

    answer = 0

    num = int(sys.stdin.readline())
    if len(max_left_heapq) == len(min_right_heapq):
        heapq.heappush(max_left_heapq, num * -1)
    else :
        heapq.heappush(min_right_heapq, num)

    if len(max_left_heapq) < 1 or len(min_right_heapq) < 1:
        pass

    elif max_left_heapq[0] * -1 > min_right_heapq[0]:    
        left_max = heapq.heappop(max_left_heapq) * -1
        right_min = heapq.heappop(min_right_heapq)

        heapq.heappush(max_left_heapq, right_min * -1)
        heapq.heappush(min_right_heapq, left_max)


    answer = max_left_heapq[0] * -1
    print(answer)






