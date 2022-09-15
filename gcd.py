# ユークリッドの互除法 # O(log(min(a, b)))
def gcd(a, b):
  if b == 0: 
    return a
  else: 
    return gcd(b, a % b)

print(gcd(12, 20)) # 最大公約数は？
