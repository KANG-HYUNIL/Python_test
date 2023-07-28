
#이분 탐색 문제

#2805번 나무 자르기(백준)


#나무의 수 n과, 필요한 나무의 길이 m 받기
n, m = list(map(int, input().split(sep=" ")))

#나무의 높이를 list로 받기
ary = list(map(int, input().split(sep=" ")))


left = 0

right = max(ary)

mid = right // 2

global answer 
answer = 0
 

def Binary_serach(left, mid, right):

    global answer

    sum = 0

    for x in ary:

        if x >= mid:
            
            sum += (x - mid)




    
    if sum >= m:

        if answer < mid:
            answer = mid

        if left == mid:
            return

        Binary_serach(mid + 1, (mid + 1 + right) // 2, right)
    
    elif sum < m:

        if left == mid:
            return

        Binary_serach(left, (left + mid ) // 2, mid)



Binary_serach(left, mid, right)

# print(n, m)
# print(ary)
print(answer)


