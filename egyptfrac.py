def is_divisible(m, n):
  return n % m == 0

# エジプトの分数(1/k + 1/h + ...) # (greedy algorithm)
def egypt_frac(m, n):
  deno = []
  while not is_divisible(m, n):
    q = n // m + 1
    deno.append(q)
    m, n = m*q - n, n*q
  deno.append(n)
  return deno

deno = egypt_frac(6, 13)

s = ["1/{}".format(d) for d in deno]
print(s)
