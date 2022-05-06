import io
import sys

_INPUT = """\
6
1
12
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  print(int(input())%12+1)