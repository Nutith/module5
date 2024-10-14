from house import House


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

h1 *= 2
print(h1)

h2 = h2 * 3
print(h2)

h1 -= 5
print(h1)

h2 = h2 - 5
print(h2)

h2 = 100 - h2
print(h2)

h2 -= 100
print(h2)
