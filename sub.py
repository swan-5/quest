n = int(input())
l = list(map(int,input().split()))
m = int(input())
total = sum(l)
b = [] # m//n 보다 큰 애들
s = []

if total <= m :
    print(max(l))

else : 
    d = total - m  
    for i in range(len(l)):
        if l[i] >= m//n : 
            b.append(l[i])
        else : 
            s.append(l[i])
    print((m -sum(s)) // len(b))