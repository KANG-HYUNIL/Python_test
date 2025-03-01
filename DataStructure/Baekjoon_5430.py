#백준 5430번 자료구조 문제 - AC

#정수 배열 연산 처리, R 뒤집기 / D 버리기
#뒤집기는 배열 순서 반전, 버리기는 첫번째 숫자 버리기

#매 번 실제로 배열을 뒤집을 필요는 없다는거네
#또한 pop(0) 는 O(n)이라서 시간이 오래걸린다
#귀찮아도 deque 써야함

import sys
from collections import deque #deque 쓰기 위해


TestCase = int(sys.stdin.readline()) #테스트 케이스 수
ErrorStr = "error" #에러 메시지

l_R = 0 #좌측이 끝이면 0, 우측이 끝이면 1
errorStatus = 0; #에러 상태

for i in range(TestCase):


    #최초 초기화화
    command = sys.stdin.readline().strip() #명령어를 입력받는다
    length = int(sys.stdin.readline()) #배열의 길이를 입력받는다
    array = sys.stdin.readline().strip() #배열을 입력받는다

    l_R = 0 #좌측이 끝이면 0, 우측이 끝이면 1
    errorStatus = 0; #에러 상태

    #문자열일 array를 실 배열로 바꾸기
    if length == 0:
        array = []
    else:
        #여기가 문제일 거 같은데? 문자열 슬라이싱이니까 길이가 길면 시간이 걸릴거임임
        array = list(map(int, array[1:-1].split(",")))
         
    dq = deque(array) #deque로 바꾸기

    #명령어 처리
    #이 문자열 반복문도 문제일 거 같은데? 시간이 걸릴거임
    for j in command:
        if j == 'R':
            if l_R == 0:
                l_R = 1
            else:
                l_R = 0

        elif j == 'D':
            if length == 0:
                #길이가 0인데 뽑기 시도하면 에러 코드 만들고 break로 탈출
                errorStatus = 1
                break

            else:
                #길이 1 감소시키기기
                length -= 1
                #좌측을 보고 있으면 popleft, 아니면 pop으로 오른쪽 뽑기기
                if l_R == 0:
                    dq.popleft()
                else:
                    dq.pop()

    #에러코그 상태면 에러 메세지 출력하고 상태 초기화 후 반복문 재실행
    if errorStatus == 1:
        print(ErrorStr)
        errorStatus = 0
        l_R = 0
        continue

    if l_R == 1:
        dq.reverse() #뒤집기

    sys.stdout.write((str(list(dq)) + "\n").replace(" ", "")) #출력           











