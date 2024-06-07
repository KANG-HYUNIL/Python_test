#백분 2156번 포도주 시식 DP 문제
#계단 오르기 문제와 유사하게, answerList에 매 i번째 음료를 마셨을 경우
#얻을 수 있는 최대 값을 저장.
#answerList 중 최댓값이 정답이다(꼭 마지막 포도주를 마실 필요가 없음)


#n 받기
n = int(input())

#포도주 양들을 기록할 배열
drinkList = []

answerList = [0] * n


#입력 받기
for i in range(n):
    drinkList.append(int(input()))

for i in range(n):

    if i == 0:
        answerList[i] = drinkList[i]

    elif i == 1:
        answerList[i] = answerList[i - 1] + drinkList[i]

    elif i == 2:
        answerList[i] = max(max(drinkList[i - 2], drinkList[i - 1]) + drinkList[i], answerList[i - 1])

    else:
        answerList[i] = max(answerList[i - 2] + drinkList[i], answerList[i - 3] + drinkList[i - 1] + drinkList[i], answerList[i - 1])

print(max(answerList))

#[100, 200, 200, 201, 301, 400]