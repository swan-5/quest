n = int(input())
l= []
ls = []
t1 = 0
t2 = 0
k1 = []
k2 = []
for i in range(n):
        t,a = input().split()
        t = int(t)
        l.append(t)
        m,s = str(a).split(':')
        m,s = int(m), int(s)
        ls.append(m*60 + s) #초로 변환 
        
#농구는 48분동안 진행된다. 
for i in range(len(l)):
        if l[i] == 1:
                t1 += 1
                if t1 > t2 :
                        k1[i] = ls[i] 
                else : k1[i] = 0
        else : 
                t2 += 1
                if t2 > t1 :
                        k2[i] = ls[i]
                else : k2[i] = 0

print 
