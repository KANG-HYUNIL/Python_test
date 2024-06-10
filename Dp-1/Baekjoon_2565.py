#백준 2565번 문제 전깃줄 DP
#로직에 필요한 코드는 매우 단순하나, 로직을 떠올리는 것이 매우 신박한 문제
#전깃줄이 교차하지 않는다 == 왼쪽 기준 정렬했을 때 오른쪽이 오름차순이여야 함


#n 받기
n = int(input())

#dp 배열, 처음부터 idx 번째 까지만 고려했을 때 지워야 하는 최소 전깃줄 개수 저장
dp = [1] * n

#전깃줄 입력을 저장할 2차원 배열
ary = []

#입력 받기
for i in range(n):
    subAry = list(map(int, input().split(" ")))
    ary.append(subAry)

#왼쪽 전봇대 기준으로 정렬
ary.sort()

#print(ary)

#그래서 이제 어캐함? 2중반복 n^2 = LIS 처럼?

#1부터 n까지
for i in range(1, n):

    #0부터 i까지
    for j in range(0, i):
        
        if ary[j][1] < ary[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)


        pass

#print(dp)

print(n - max(dp))

#1 8
#2 2
#3 9
#4 1
#6 4
#7 6
#9 7
#10 10
#
#








