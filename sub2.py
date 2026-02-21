n = int(input())
w = 4*n -3
h = 2*n -1
l = [[' ']*w for _ in range(h)]

for i in range(n):
    l[0][i] = '*'
    l[0][w-n+i] = '*'
    l[h-1][i]='*'
    l[h-1][w-n+i]='*'

for i in range(1,n-1):
    l[i][i]='*'
    l[i][n+i-1]='*'
    l[i][w-n-i]='*'
    l[i][w-i-1]='*'

m = n-1
l[m][m]='*'
l[m][m+n-1]='*'
l[m][m+2*n-2]='*'

for i in range(1,n-1):
    r=m+i
    l[r][m-i]='*'
    l[r][2*m-i]='*'
    l[r][2*m+i]='*'
    l[r][2*m+i+n-1]='*'

for row in l:
    print(''.join(row).rstrip())
    




