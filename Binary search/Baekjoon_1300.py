#1300번 K번째 수(백준)


#n, k 받기
n = int(input())

k = int(input())


#B[k] <= k 가 항상 성립한다?
#right 값을 n^2가 아닌 k로 설정한다?

#직접 B[k]를 구하는 것이 아닌, 임의의 값을 B[k]라 정하고, 
#정한 B[k]보다 작은 수의 개수를 구함으로써 B[k]의 위치를 추정한다
#B[k]보다 작은 수의 개수 >= k 인 수들 중, 가장 작은 B[k]가 정답?
#가장 작은 B[k] 여야만, 정렬 후 k 번째 수가 될 수 있다?


left = 1

right = k

answer = 0

while left <= right :

    #중간값 mid 구하기
    mid = (left + right) // 2
    
    #임의의 값 mid보다 작은 수의 개수를 담을 cnt
    cnt = 0

    #1번째 줄 부터 n번째 줄 까지, 차례차례 mid보다 작은 수의 개수 검사
    for i in range(1, n + 1):

        #mid//i가 n보다 크면, mid보다 작은 수는 n개라는 것이다
        cnt += min(mid // i, n)

     
    #cnt가 k보다 크다면, mid를 더 줄여봐도 된다
    #가장 최소의 B[k]를 찾기 위해서
    if cnt >= k :

        answer = mid
        right = mid - 1
       
    #cnt가 k보다 작다면, mid를 더 키워봐야 된다
    #mid가 문제 조건에 맞지 않는다는 것이기에
    else:

        left = mid + 1



print(answer)



