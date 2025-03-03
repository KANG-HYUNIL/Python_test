#백준 2042버 구간 합 구하기 문제
#단순하게 DP 문제에서 연속하는 부분 수열 합 같은 문제르 취급하여서, List로 해결하려 하였다
#그러나, List 연산은 내가 예상하였던 것처럼 시간 복잡도가 O(N)
#이 문제에서는 N, M, K의 수 단위가 매우 크기에 List 연산은 시간 초과가 발생할 것이다
#따라서, Segment Tree를 사용하여야 한다
#Segment Tree는 구간 합을 구하는데 O(logN)의 시간 복잡도를 가진다


import sys

#N, K, M
N, K, M = map(int, sys.stdin.readline().split())

#N개의 수 처리
numbers = [0]
for i in range(N):
    numbers.append(int(sys.stdin.readline()))

segment_tree = [0] * 4 * N #Segment Tree를 위한 배열 선언

#Segment Tree 초기화 //완료료
def init_tree(start, end, idx):

    #리프 노드(가장 아래의 자식 노드) 도달 시에, 수 하나의 값 그대로 저장
    if start == end :
        segment_tree[idx] = numbers[start]
        return segment_tree[idx]

    #리프 노드가 아닌 경우, 자식 노드의 합을 저장
    mid = (start + end) // 2 #중간 지점
    #좌측 자식 노드의 값 + 우측 자식 노드의 값 재귀로 이용해 연산하기
    segment_tree[idx] = init_tree(start, mid, idx * 2) + init_tree(mid + 1, end, idx * 2 + 1)
    return segment_tree[idx]


#구간 합 연산
#b ~ c 의 구간 합 처리리
def interval_sum(interval_start, interval_end, idx, left, right):
    
    #구간이 완전히 벗어난 경우
    if right < interval_start or interval_end < left:
        return 0

    #구간이 완전히 포함된 경우
    if interval_start <= left and right <= interval_end:
        return segment_tree[idx]

    #구간이 일부만 포함된 경우
    mid = (left + right) // 2

    #좌측과 우측의 값 연산산
    return interval_sum(interval_start, interval_end, idx * 2, left, mid) + interval_sum(interval_start, interval_end, idx * 2 + 1, mid + 1, right)

#트리 특정 원소 갱신
def update_tree(start, end, idx, target_idx, val):

    #바꾸려는 idx에 도달한 경우
    if start == end == target_idx:
        segment_tree[idx] = val #값 갱신
        return
    
    #현재 연산을 시도하는 구간(start~ end)가 범위에 포함되지 않을 경우에
    if target_idx < start or end < target_idx:
        return
    
    mid = (start + end) // 2 
    update_tree(start, mid, idx * 2, target_idx, val) #좌측 자식 노드 갱신
    update_tree(mid + 1, end, idx * 2 + 1, target_idx, val) #우측 자식 노드 갱신
    segment_tree[idx] = segment_tree[idx * 2] + segment_tree[idx * 2 + 1] #갱신된 자식 노드의 값으로 현재 노드 갱신

ROOT_NODE_IDX = 1
init_tree(1, N, ROOT_NODE_IDX) #Segment Tree 초기화, 루트 노드의 idx를 1로 설정정

#K+M개의 연산 처리
for i in range(K+M):
    a, b, c = list(map(int, sys.stdin.readline().split()))

    if a == 1:
        update_tree(ROOT_NODE_IDX, N, ROOT_NODE_IDX, b, c) #트리 특정 원소 갱신
        pass

    elif a == 2:
        sum = interval_sum(b, c, ROOT_NODE_IDX, ROOT_NODE_IDX, N) #구간 합 연산
        print(sum)
        pass
 


