import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
x,y = n //2,n //2 
length = [-1,0,1,0]
width = [0,1,0,-1]
d = 0
l = [[0] * n for _ in range(n)]
t = l[x][y] = 1
r = 0
xx, yy = x, y

for i in range(2*n+1):
    if i % 2 == 0 : r += 1
    for a in range(r):
        if l[x][y] == n*n : break
        dx = x + length[d] 
        dy = y + width[d]
        l[dx][dy] = l[x][y]+1 
        if l[dx][dy] == k:
            xx = dx
            yy = dy
        x,y = dx,dy

    d = (d+1) %4 
    
    
for i in l :
    print(' '.join(map(str,i)))
print(xx+1,yy+1)