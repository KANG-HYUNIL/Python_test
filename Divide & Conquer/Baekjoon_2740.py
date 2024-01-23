import sys

#행렬 곱셈 2740번(백준) 분할 정복 문제


a = []
b = []
c = []


n, m = list(map(int, sys.stdin.readline().split(sep=" ")))

for j in range(n):
    a.append(list(map(int, sys.stdin.readline().split(sep=" "))))



m, k = list(map(int, sys.stdin.readline().split(sep=" ")))

for j in range(m):
    b.append(list(map(int, sys.stdin.readline().split(sep=" "))))

 
for x in range(n):

    sum = 0
    sum_ary = []

    for y in range(k):

        sum = 0
        
        for z in range(m):

            sum += a[x][z] * b[z][y]
        
        sum_ary.append(sum)

    c.append(sum_ary)


for i in range(n):

    print(" ".join(list(map(str, c[i]))))

