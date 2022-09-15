class G():
  def __init__(self, V, adj):
    self.V, self.adj = V, adj
  def next(self, v): return self.adj[v]

def seen(v, lseen): lseen[v] = True

def is_seen(v, lseen): return lseen[v] == True

def proc(v):
  print("passed: {}".format(v))


# 深さ優先探索 # [wrost case]O(V+E)
def dfs(g, v, lseen):
  seen(v, lseen)
  proc(v)
  for u in g.next(v):
    if not is_seen(u, lseen):
      dfs(g, u, lseen)


V   = [1, 2, 3, 4, 5]
adj = { # 隣接リスト表現
    1: [3, 5],
    2: [3, 4, 5],
    3: [1, 2, 5],
    4: [2],
    5: [1, 2, 3]
}
g = G(V, adj)
lseen = {v:False for v in V}

dfs(g, 1, lseen)
