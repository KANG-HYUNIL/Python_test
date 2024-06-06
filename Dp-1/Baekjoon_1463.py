#백준 1463번 1로 만들기 DP 문제
#n을 3 혹은 2 로 나누거나, 1을 빼는 3가지의 과정을 통해 1로 만들기
#1로 만드는데 필요한 최소 연산 횟수를 구해야 함
#재귀로 모든 연산의 수를 계산하며 접근해야 할듯?
#모든 경우의 수를 계산하는 것은 시간 초과로 탈락한다!
#
import sys
import copy

sys.setrecursionlimit(10**6)

#정수 n 받기
n = int(input())

#연산 후의 결과들을 저장할 리스트
#각 idx번 째의 값은 1에서 idx 숫자가 되기 위해 필요한 연산의 최소 횟수
answerList = [0] * (n + 1)
answerList2 = [0] * (n + 1)

if n >= 2:
    answerList[2] = 1
    answerList2[2] = 1
    if n >= 3:
        answerList[3] = 1
        answerList2[3] = 1

#answerList[n] = 의 값이 문제가 원하는 최소 연산 횟수

#n이 되기 위한 최소 연산 횟수를 계산하는 함수
#처음으로 시도한 재귀를 이용한 함수. 시간 초과가 발생함
def calculateCost(x):

    #n번째 값이 계산되어 있지 않다면
    if answerList[x] == 0:

        subList = []

        if x % 3 == 0:
            subList.append(calculateCost(x//3))

        if x % 2 == 0:
            subList.append(calculateCost(x//2))

        subList.append(calculateCost(x - 1))

        answerList[x] = min(subList) + 1

        pass

  

    return answerList[x]

#print(type(n))

# answer = calculateCost(n)
# print(answer)

#두 번째로 시도한 for문을 이용해 n으로 끝내는 방법
#맨 밑에서 n까지 차근차근 올라와 n에 도달함
if n <= 3:

    print(answerList2[n])

else:

    for i in range(4, n + 1):

        subList = []

        if i % 3 == 0:
            subList.append(answerList2[i//3])

        if i % 2 == 0:
            subList.append(answerList2[i//2])

        subList.append(answerList2[i - 1])

        answerList2[i] = min(subList) + 1

    print(answerList2[n])

