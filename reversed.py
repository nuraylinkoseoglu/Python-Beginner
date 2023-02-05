"""
Write a function to return reverse of the list list. For example:
input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

#function
def get_reversed(aList):
    L=[]
    for i in range(len(aList)-1,-1,-1):
        L.append(aList[i][::-1])
    return L
#test
get_reversed([[1, 2], [3, 4], [5, 6, 7]])