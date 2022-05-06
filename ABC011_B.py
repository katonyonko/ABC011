import io
import sys

_INPUT = """\
6
taKahAshI
A
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  ans=[S[0].upper()]
  for i in range(len(S)-1):
    ans.append(S[i+1].lower())
  print(*ans,sep='')