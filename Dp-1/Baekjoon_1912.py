import sys


#1912번 연속합(백준) Dp 문제

#배열의 길이 n 과 배열 입력받기
n = int(input())

ary = list(map(int, sys.stdin.readline().split(sep=" ")))


max_ary = [] #최댓값 후보들을 모을 배열

mx = "0" #그때그때의 최댓값을 저장할 변수, "0"은 현재 저장값 없음

for i in range(n): 

    if mx == "0": #변수에 값이 없으면, 우선 ary[i] 저장
        mx = ary[i]
    

    else: #변수에 값이 저장되어 있다면

        if ary[i] < 0: #ary[i]가 음수라면 

            #ary[i]의 절댓값이 mx보다 작아서, mx와 합해도 최대일 수 있다면
            if mx + ary[i] >= 0:  
                max_ary.append(mx) #우선 현재 mx값을 저장
                mx += ary[i] #그 후 ary[i]와 합하기
        
            #ary[i]의 절댓값이 mx보다 커서, 더하는게 의미가 없다면
            elif mx + ary[i] < 0:
                max_ary.append(mx) #현재 mx값 저장
                max_ary.append(ary[i])
                mx = "0" #ary[i] 값은 취급하지 않게, 넘겨버리기


        elif ary[i] >= 0: #ary[i]가 양수라면, mx에 더하기

            if mx < 0: #기존 mx가 음수라면, 기존 mx를 버리고 ary[i] 사용
                mx = ary[i]

            else: #기존 mx도 양수면, 더해버리기
                mx += ary[i]

#마지막 mx의 값도 append
if mx != "0":
    max_ary.append(mx)

print(max(max_ary)) #최댓값 후보들 중 가장 큰 값 출력

