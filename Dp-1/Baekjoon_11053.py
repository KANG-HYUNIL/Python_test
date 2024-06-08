import sys

#가장 긴 증가하는 부분수열 11053(백준) Dp문제
#배열의 각 idx에, 각 idx의 칸만큼 보았을 때의 최대 길이 저장하는 방식으로 접근하기\


#입력 받기
n = int(input())
ary = list(map(int, sys.stdin.readline().split(sep=" ")))

#가장 긴 증가하는 부분수열의 길이 저장할 배열
dp = [1 for _ in range(n)] 


#O(n^2) 로 풀기?
for i in range(1, n):

    for j in range(0, i):
        
        if ary[j] < ary[i]: #앞 쪽 숫자가 뒤 쪽 숫자보다 작다면
            
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))

#예제 10 20 10 30 20 50
#1 2 1 3 2 4





