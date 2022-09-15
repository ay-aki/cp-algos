import math

# 素数判定 # O(√N)
def is_prime(N):
  sq_N = math.floor(math.sqrt(N))
  for n in range(2, sq_N + 1):
    if N % n == 0:
      return False
  return True

print(is_prime(31)) # 31は素数か？
