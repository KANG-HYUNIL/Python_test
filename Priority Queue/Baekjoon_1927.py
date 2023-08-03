#백준 1927번 최소 힙 문제 풀이
import sys


n = int(sys.stdin.readline())
#n = int(input())


ary = [0]


def Push(x):

    ary.append(x)

    child_idx = len(ary) - 1
    parent_idx = child_idx // 2

     

    while child_idx > 1 and ary[child_idx] < ary[parent_idx]:

        
        a = ary[child_idx]
        ary[child_idx] = ary[parent_idx]
        ary[parent_idx] = a
        child_idx = parent_idx
        parent_idx = child_idx // 2




def Pop():

    sys.stdout.write(str(ary[1]) + "\n")
    #print(ary[1])

    #마지막 원소를 맨 위로 올리기
    ary[1] = ary[-1]
    ary.pop()

    parent_idx = 1
    child_idx = parent_idx * 2

    
    while child_idx <= len(ary) - 1:

        #자식이 왼쪽만 잇는 경우
        if child_idx + 1 >= len(ary):

            if ary[parent_idx] > ary[child_idx]:
                
                a = ary[parent_idx]
                ary[parent_idx] = ary[child_idx]
                ary[child_idx] = a
                parent_idx = child_idx
                child_idx = parent_idx * 2
                
            else:
                break
        

        else:

            #자식 중 왼쪽이 더 작거나 같으면
            if ary[child_idx] <= ary[child_idx + 1]:

                if ary[parent_idx] > ary[child_idx]:

                    a = ary[parent_idx]
                    ary[parent_idx] = ary[child_idx]
                    ary[child_idx] = a
                    parent_idx = child_idx
                    child_idx = parent_idx * 2
                    
                else:
                    break

            #자식 중 오른쪽이 더 작으면
            elif ary[child_idx] > ary[child_idx + 1]:
                child_idx += 1

                if ary[parent_idx] > ary[child_idx]:

                    a = ary[parent_idx]
                    ary[parent_idx] = ary[child_idx]
                    ary[child_idx] = a
                    parent_idx = child_idx
                    child_idx = parent_idx * 2

                else:
                    break





for i in range(n):

    x = int(sys.stdin.readline())
    #x = int(input())


    if x == 0:
        
        if len(ary) == 1:
           # sys.stdout.write("0\n")
           print(0)
        
        #가장 우선순위가 높은 원소 빼주기
        else:

            Pop()
            # print(ary)
            # print("Pop")



    #원소 Push하고 이진 트리 유지
    else:

        Push(x)
        # print(ary)
        # print("Push")
      

