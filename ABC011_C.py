import io
import sys

_INPUT = """\
6
2
1
7
15
5
1
4
2
300
57
121
244
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  NG=[int(input()) for _ in range(3)]
  NG.sort()
  if N in NG: print('NO')
  else:
    ans='NO'
    NG=set(NG)
    r=[0]*301
    r[N]=1
    for _ in range(100):
      tmp=[0]*301
      for i in range(301):
        if i not in NG:
          if i+1<301 and r[i+1]==1: tmp[i]=1
          if i+2<301 and r[i+2]==1: tmp[i]=1
          if i+3<301 and r[i+3]==1: tmp[i]=1
        if i==0 and tmp[0]==1: ans='YES'; break
      r=tmp.copy()
    print(ans)