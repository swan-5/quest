n = int(input())
l= []
ls = []
t1 = 0
t2 = 0
k1 = 0
k2 = 0
for i in range(n):
        t,a = input().split()
        t = int(t)
        l.append(t)
        m,s = str(a).split(':')
        m,s = int(m), int(s)
        ls.append(m*60 + s) #초로 변환   
pre = 0
#농구는 48분동안 진행된다. 
for i in range(len(l)):
        now = ls [i]

        if t1 > t2 : 
                k1 += now - pre
        elif t2 > t1 :
                k2 += now -pre

        if l[i] == 1 : 
                t1 += 1
        else : t2 += 1

        pre = now
end = 2880
if t1 > t2:
        k1 += end-pre
elif t2 > t1 :
        k2 += end - pre
        
print (f'{k1//60:02d}:{k1%60:02d}') 
print (f'{k2//60:02d}:{k2%60:02d}') 
