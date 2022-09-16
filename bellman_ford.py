class Graph():
  def __init__(self, V, E, cost):
    self.V  = V
    self.E  = E
    self.cost = cost # e -> cost(e)
    self.nV = len(V)

def init_d(g, s):
  d = {v:float("inf") for v in g.V}
  d[s] = 0
  return d

# ベルマン・フォードのアルゴリズム # O(V*E)
def bellman_ford(g, s):
  d = init_d(g, s)
  for i in range(g.nV):
    update = False
    for e in g.E:
      u, w = e
      if d[w] > d[u] + g.cost[e]:
        d[w] = d[u] + g.cost[e]
        update = True
    if not update: break # 更新がなければ
    if i == g.nV - 1: return -1 # 負閉路が存在
  return d

V = "abcdefg"
cost = {
    "ab":4, "ac":3, "bd":1, "be":5, "bc":1, "cf":2, "de":3, "eg":2, "fe":1, "fg":4
}
E = cost.keys()

g = Graph(V, E, cost)
d = bellman_ford(g, "a")

print(d)
