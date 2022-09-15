import math

def init(N):
  prime = [True] * (N + 1)
  prime[0], prime[1] = False, False
  return prime

# エラトステネスの篩 # √N
def soe(N):
  prime = init(N)
  sq_N = math.floor(math.sqrt(N))
  for p in range(2, sq_N + 1):
    if prime[p]:
      for q in range(p, N//p + 1): # p*q <= N
        prime[p*q] = False
  return prime

print(soe(20)[17]) # 17は素数か?
