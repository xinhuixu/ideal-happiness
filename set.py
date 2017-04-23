A = [1,2,3]
B =[2,3,4]

#set of all objects in A, B, or both
def union(A, B):
    return A + [x for x in B if x not in A]


print 'A: ', A
print 'B: ', B
#test cases
print 'union', union(A, B)
