x = {"a", "b", "c"}
y = {"l", "c", "a", "o", "k", "t", "b"}
z = x.symmetric_difference(y)
print(z)
z = x.symmetric_difference_update(y)
print(x)
