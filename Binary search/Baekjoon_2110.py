#2110번 공유기 설치(백준)



n , c = list(map(int, input().split(sep=" ")))


ary = []

global answer
answer = 0

for i in range(n):
    ary.append(int(input()))

ary.sort()


 
#최소 거리, 최대 거리, 중간 거리 지정
left = 1
right = ary[-1] 
mid = (left + right) // 2


 
def bs(left, mid, right):

    global answer

    last_pos = ary[0]
    cnt = 1


    for x in ary:

        if x == ary[0]:
            pass

        else:

            if x - last_pos >= mid:

                cnt += 1
                last_pos = x
    

    if cnt >= c:

        if answer < mid:
            answer = mid
         
        if left >= right:
            return

        bs(mid + 1, (mid + 1 + right) // 2, right)



    elif cnt < c:

        if left >= right:
            return

        bs(left, (left + mid) // 2, mid)



bs(left, mid, right)

print(answer)




