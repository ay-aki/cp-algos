import math

def func(x):
  return x**2 + 3*x - 4

# 黄金分割法
def gold_section(f, a, b, eps=1e-5, N=1e5):
  """
  f(x)の区間(xa, xb)での最小となる点xminを求める。
  なお、f(x)は(xa,xmin)で単調減少、(xmin, xb)で単調増加するものと考える。
  """
  r     = 2 / (3 + math.sqrt(5))
  t     = lambda x1, x2: r*(x2 - x1)
  c, d  = a + t(a, b), b - t(a, b)
  fc, fd= f(c), f(d)
  for n in range(int(N)):
    if fc > fd:
      a, b = c, b; c, d = d, b - t(a, b); fc, fd = fd, f(d)
      if d - c < eps: return c
    else:
      a, b = a, d; c, d = a + t(a, b), c; fc, fd = f(c), fc
      if d - c < eps: return d
  return None

print(gold_section(func, -3, 3))
