import io
from os import TMP_MAX
import sys

_INPUT = """\
6
2 10000000
10000000 10000000
100 2
3 7
11 8562174
25686522 17124348
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,D=map(int,input().split())
  X,Y=map(int,input().split())
  if X%D!=0 or Y%D!=0: print(0)
  else:
    X//=D; Y//=D
    if abs(X)+abs(Y)>N or (N-abs(X)-abs(Y))%2==1: print(0)
    else:
      X=abs(X); Y=abs(Y)
      N-=X+Y
      ans=0
      for i in range(N//2+1):
        l,r,u,d=X+i,i,Y+N//2-i,N//2-i
        tmp=1
        for j in range(l+r+u+d):
          if j<l: tmp/=l-j
          elif j<l+r: tmp/=r-(j-l)
          elif j<l+r+u: tmp/=u-(j-l-r)
          else: tmp/=d-(j-l-r-u)
          tmp*=(l+r+u+d-j)/4
        ans+=tmp
      print(ans)