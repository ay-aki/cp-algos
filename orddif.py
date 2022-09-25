"""
状微分方程式の解法
Eular法、RugneKutta法の２種類を扱う。
ここでは１次元の場合について
"""

dt = 0.01

def f(t, x):
  return 1 - x**2

# Eular Method
def f_D_EularMethod(t, x):
  dx = f(t, x)*dt
  return t + dt, x + dx

# Runge-Kutta Method
def f_D_RungeKuttaMethod(t, x):
  d1 = f(t, x)
  d2 = f(t+dt/2, x+d1*dt/2)
  d3 = f(t+dt/2, x+d2*dt/2)
  d4 = f(t+dt, x+d3*dt)
  dx = (d1 + 2*d2 + 2*d3 + d4)/6 * dt
  return t + dt, x + dx

# 状微分方程式の解法(ordinary differencial equation)
def orddif(N=100, f_D=f_D_EularMethod):
  t0, x0 = 0., 0.
  t, x = t0, x0
  for n in range(N):
    t, x = f_D(t, x)
    print(t, x)

orddif()
