class UnionFind():
  """
  比較的単純な構造のUF木
  """
  def __init__(self, V):
    self.V = V
    self.par = {v:v for v in V}
  def root(self, v):
    self.par[v] = v if self.par[v] == v else self.root(self.par[v])
    return self.par[v]
  def unite(self, v1, v2):
    r1, r2 = self.root(v1), self.root(v2)
    self.par[r1] = self.par[r1] if r1 == r2 else r2
  def is_samegroup(self, v1, v2):
    r1, r2 = self.root(v1), self.root(v2)
    return r1 == r2
  def roots(self):
    return [v for v in self.par if v == self.par[v]]



V = ["a", 2, 3, 4, 5, 6, 7]
uf = UnionFind(V)

uf.unite("a", 2)
uf.unite(4, 3)
uf.unite(4, 5)
uf.unite(3, 7)

# {"a", 2}
# {3, 4, 5, 7}
# {6}


print(uf.is_samegroup(5, 7))
