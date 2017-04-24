A = [1,2,3]
B =[2,3,4]

#assume there is no duplicate value in a set; mathematically it wouldn't make sense anyways

#set of all objects in A, B, or both
def union(A, B):
    return A + [x for x in B if x not in A]

def intersection(A, B):
    return [x for x in A if x in B]

def set_diff(A, B):
    return [x for x in A if x not in B]

def sym_diff(A, B):
    return set_diff(union(A, B), intersection(A, B))

def cart_prod(A, B):
    return [(a, b) for a in A for b in B]

print 'A: ', A
print 'B: ', B
#test cases
print 'union', union(A, B)
print 'intersection', intersection(A, B)
print 'set_diff', set_diff(A, B)
print 'sym_diff', sym_diff(A, B)
print 'cart_prod', cart_prod(A, ["green", "blue", "red"])
