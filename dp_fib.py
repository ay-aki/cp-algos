# フィボナッチ数列(動的計画法) # O(n)
def fib(n):
  dp = [0] * (n+1)
  dp[0], dp[1], dp[2] = 0, 1, 1
  for i in range(1, n - 1):
    dp[i+2] = dp[i+1] + dp[i]
  return dp

print(fib(20))
