#!/usr/bin/env python3
import bisect
import sys
sys.set_int_max_str_digits(10**9)

I = lambda: int(input())
M = lambda: map(int, input().split())
M_DEC = lambda: map(lambda x: int(x) - 1, input().split())
L = lambda: list(map(int, input().split()))
S = lambda: input().split()

N, M = L()
A = sorted(L())
candidates = set()
for i in A:
    st = bisect.bisect_left(A, i-0.5) - 1
    end = bisect.bisect_left(A, i+M-0.5, st+1) - 1
    candidates.add(end-st)
try:
    print(max(candidates))
except ValueError:
    print(0)
