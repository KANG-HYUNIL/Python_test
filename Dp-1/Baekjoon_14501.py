#백준 14501번 퇴사




N = int(input()) #N일
dp = [0] * (N + 2) #dp 테이블 생성

table = [[0, 0] for _ in range(N + 1)] #테이블 생성

for i in range(1, N + 1):
    table[i][0], table[i][1] = map(int, input().split()) #입력값 받기


for i in range(1, N + 1):
    
    #i일에 상담을 진행하는데, 상담에 필요한 일자가 N을 넘어가지 않는다면
    if i + table[i][0] <= N + 1: 
        dp[i + table[i][0]] = max(dp[i + table[i][0]], dp[i] + table[i][1])

    if i >= N:
        continue

    dp[i + 1] = max(dp[i + 1], dp[i]) #i일에 상담을 진행하지 않는다면, i+1일에도 최대값을 저장한다.

print(max(dp)) #최대값 출력


