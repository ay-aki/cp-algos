import math

ret = []

def proc(N, n):
  ret.append(n)
  if n**2 != N:
    ret.append(N//n)

# 約数列挙アルゴリズム # O(√N)
def divisor(N):
  sq_N = math.floor(math.sqrt(N))
  for n in range(1, sq_N + 1):
    if N % n == 0: # N/nとnは約数となる。
      proc(N, n) 

divisor(100)
ret.sort()

print(ret)
