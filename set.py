A = [1,2,3]
B =['a','b','c',1]

#set of all objects in A, B, or both
def union(A, B):
    return A + [x for x in B if x not in A]


#test cases
print union(A, B)
