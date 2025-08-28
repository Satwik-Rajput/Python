# S = set() , this is the way of writing void set

S = {3,5,32,5,6,7}
S1 = {3,7,9,0,4,2}

print(type(S))

S.add(9)

print(S)

print(len(S))

S.remove(5)

print(S)

print(S.union(S1))

print(S.intersection(S1))

print({3,0}.issubset(S1))

print(S-S1)