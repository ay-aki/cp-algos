import numpy as np

### 『第一象限の1/4円の公式を求める』 ###
xdim = 2 # ２次元図形に関する公式を求める。
def gen_x(k): return np.random.rand(k) # 第一象限 [0, 1] **2 で乱数生成
def is_inside(x): return np.dot(x, x) < 1 # 第一象限 norm(x) < 1 の面積を求めたい。

# モンテカルロ法
def montecarlo(N=10000):
  cnt = 0
  for n in range(N):
    x    = gen_x(xdim)
    cnt += is_inside(x)
  return cnt / N

# 公式は、[area_of_1/4circle] = [lam] * [a]*[b]
lam = montecarlo()

print(lam)
