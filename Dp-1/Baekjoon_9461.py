


#Dp 문제 9461번 파도반 수열


dp = [1, 1, 1, 2, 2] #초기 값 설정

testcase = int(input()) # 테스트케이스 수 입력받기

#dp의 n번째 값을 돌려주는 함수
def check(n):

    if dp[n] != 0 : #n 번째 값이 존재한다면
        
        return dp[n]
    
    else: #n 번째 값이 0이라면, 즉 없다면
        dp[n] = check(n - 5) + check(n - 1) #재귀 이용 n 번째 값 찾아주기
        return dp[n]



for i in range(testcase): #테스트케이스 반복문

    n = int(input()) #n 입력받기
    n -= 1

    if n <= 4: #n이 5 이하면 초기값 바로 사용
        print(dp[n]) 
        
    else:
        
        if len(dp) < n + 1: #dp 배열의 길이보다 n이 더 크면

            for j in range(n + 1 - len(dp)):
                dp.append(0) #dp 배열의 길이를 n으로 만들어주기
        
        print(check(n)) #n 번째 값 출력하기












