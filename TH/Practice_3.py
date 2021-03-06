def Tach_Mang(n,chinh,phu):
  for i in range(n):
    a,b = map(int,input().split())
    chinh.append(a)
    phu.append(b)

def Quy_Hoach_Dong(n,a,b):
  F = [ [0]*(n+1) for i in range(n+1)]
  F[1][1] = b[0]
  for i in range(2,n+1):
    F[i][0] = F[i-1][1] + a[i-1]
    F[i][i] = F[i-1][i-1] + b[i-1]
    for j in range(1,i):
      F[i][j] = min(F[i-1][j+1]+a[i-1],
                    F[i-1][j-1]+b[i-1])
  print(F[n][0])

n = int(input())
chinh,phu,  = [], []
Tach_Mang(n,chinh,phu)
Quy_Hoach_Dong(n,chinh,phu)
