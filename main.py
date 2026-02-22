n = int(input())
l= []
lm = []
ls = []
t1 = 0
t2 = 0

for i in range(n):
        t,a = input().split()
        t = int(t)
        l.append(t)
        m,s = str(a).split(':')
        m,s = int(m), int(s)
        lm.append(m) #골 넣은 분
        ls.append(s) #초
        
#농구는 48분동안 진행된다. 
for i in range(len(l)):
        if l[i] == 1:
                t1 += 1
                if t1 > t2 :
                        lm[i]




print(l,lm,ls)