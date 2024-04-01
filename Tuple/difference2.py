A={"a","b","c","d","e"}
B={"f","a","c","g"}
print(A.difference(B))
print(A.intersection(B))
print(A.isdisjoint(B))
print(A.issubset(B))
print(A.symmetric_difference(B))
print(A.union(B))

re= A.pop()
print(re)

y={"s","t","u","v"}
rel= y.pop()
print(rel)
print(y)