n = int(input())
l = list(map(int,input().split()))
l.sort()
m = int(input())
total = sum(l)

if total <= m :
    print(max(l))

else : 

    d = total - m 
    for i in range(len(l)):
