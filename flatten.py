'''
Write a function to flatten a list. For example:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
'''

# function
def flatten(l):
    flattenList=[]
    for i in l:
        if type(i) != type([]):
            flattenList.append(i)
        else:
            flattenList.extend(flatten(i))
    return flattenList
#test
flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])