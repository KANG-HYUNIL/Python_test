#백준 1010번 다리 놓기

import sys



#조합을 이용한 풀이, 근데 조합 기억 안나요

input = sys.stdin.readline

TestCase = int(input())

for _ in range(TestCase):
    
        N, M = map(int, input().split())
    
        #조합을 이용한 풀이
        result = 1

        #???? 이게 뭐야
        #nCm = n! / (m! * (n - m)!) 으로 풀 수 있었다
        for i in range(N):
            result *= (M - i)
            result /= (i + 1)
    
        print(int(result))




