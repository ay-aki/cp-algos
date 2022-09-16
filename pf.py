import math

def spf_init(N):
  return [i for i in range(N+1)]

# SPF(Smallest Prime Fact) # O(N loglog(N))
def spf(N):
  spfl = spf_init(N)
  sq_N = math.floor(math.sqrt(N))
  for p in range(2, sq_N + 1):
    if spfl[p] == p:
      for q in range(p, N//p + 1):
        if spfl[p*q] == p*q:
          spfl[p*q] = p
  return spfl

# PF(Prime Fact) # O(log(N))
def pf(N, spfl): 
  ml = [0] * (N + 1)
  n = N
  while n != 1:
    ml[spfl[n]] += 1
    n = n // spfl[n]
  return ml

spfl = spf(40) # 40以下の値に対して素因数分解をしたい
print(pf(20, spfl))   # 20の素因数分解は？
