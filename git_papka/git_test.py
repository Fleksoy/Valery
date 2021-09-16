'''
Выведите таблицу размером n×n n \times n n×n, заполненную числами от 1 1 1 до n2 n^2 n2 по спирали, выходящей из
левого верхнего угла и закрученной по часовой стрелке:
'''

n=int(input())
s=0
A=[[1]*n for i in range(n)]
if(n%2==1):
    A[n//2][n//2]=n*n
for probel in range(n):
    for i in range(n):
       for j in range(n):
               if i==probel-1 and probel-1<=j<(n-probel):               #право
                   A[probel-1][j]+=s
                   s += 1
               elif j==n-probel and probel-1<=i<n-probel:              #vniz
                   A[i][j]+=s
                   s += 1
               elif i==(n-probel) and probel-1<j<=(n-probel):           #vlevo
                    A[i][-j ] += s
                    s+=1
    for i in range(n):
        for j in range(n):
            if j == probel-1 and probel-1 < i <= n -  probel:  # verh
                A[ n - i][j] += s
                s += 1
for i in range(len(A)):
    for j in range(len(A)):
        A[i][j]=int(A[i][j])
        print(A[i][j],end=' ')
    print()