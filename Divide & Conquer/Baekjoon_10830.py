import sys

#행렬 제곱 10830번(백준) 분할 정복 문제

a = []

#Input 받기
n, b = list(map(int, sys.stdin.readline().split(sep=" ")))

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split(sep=" "))))

#행렬 곱셈을 연산하는 함수
def multiple_matrix(a, i, n):
    
    c = []

    for x in range(n):

        sub_c = []

        for y in range(n):

            sum = 0

            for z in range(n):

                sum += (a[x][z] * i[z][y]) % 1000 #각 원소를 1000으로 나눈 나머지 
            
            sum %= 1000 #각 원소를 1000으로 나눈 나머지 

            sub_c.append(sum)
        
        c.append(sub_c)

    return c #행렬 곱 return


#행렬 거듭제곱을 실행하는 함수
def devide(b):

    if b == 1: #1제곱일 경우, a 그대로 return

        return a
    
    elif b % 2 == 0: #짝수 제곱일 경우, 절반으로 분할해 계산 진행
        
        d = devide(b / 2)
        return (multiple_matrix(d, d, n))

    elif b % 2 == 1: #홀수 제곱일 경우, (b - 1) / 2로 분할해 진행
        d = devide((b - 1) / 2)
        return (multiple_matrix(multiple_matrix(d, d, n), a, n))


for i in devide(b):
    print(" ".join(list(map(str, i))))
    

