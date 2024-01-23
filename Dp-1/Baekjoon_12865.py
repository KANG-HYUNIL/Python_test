import sys
sys.setrecursionlimit(10**6)

#평범한 배낭 12865번(백준) Dp문제
#냅색 문제, 같은 물건을 여러 번 넣을 수 없다. 중복 X


#Input 받기
n, k = list(map(int, sys.stdin.readline().split(sep=" ")))

weight = []
value = []

for i in range(n):
    w, v = list(map(int, sys.stdin.readline().split(sep=" ")))
    weight.append(w)
    value.append(v)

#가치를 저장할 list, 무게 제한을 열, 물건 제한을 행으로 하는 2차원
#각 물건의 무게 제한 당 최대 가치를 저장함
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]


for i in range(1, n + 1): #각 물건, 행에 대해서

    for j in range(1, k + 1): #각 무게 제한, 열에 대해서

        #물건의 무게가 무게 제한 j보다 작아서 넣을 수 있다면
        if j >= weight[i - 1]:  

            #i번째 물건을 억지로 담을 때와, 담지 않을 때의 가치 중 큰 것을 저장

            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
        
        #물건의 무게가 무게 제한 j보다 커서 넣을 수 없다면
        elif j < weight[i - 1]:

            #i번째 물건 취급 전의 최대 가치값을 그대로 가져오기
            dp[i][j] = dp[i - 1][j] 

        





print(dp[n][k])
