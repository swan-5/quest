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
        ls.append(m*60 + s) #초로 변환 ver6
        
#농구는 48분동안 진행된다. 
for i in range(len(l)):
        if l[i] == 1:
                t1 += 1
                if t1 > t2 :
                        k1.append(ls[i])
                else : k1.append(0)
        else : 
                t2 += 1
                if t2 > t1 :
                        k2.append(ls[i])
                else : k2.append(0)
ks = 2880- sum(k1)
kq = sum(k2)
print (f'{ks//60:02d}:{ks%60:02d}') 

print (f'{kq//60:02d}:{kq%60:02d}') 
