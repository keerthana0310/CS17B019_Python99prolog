list=['a','b','c','d','e','f','g','h']
def split(list1,n):
    for i in range(0,len(list1),n):
        yield list1[i:i + n]
n=5
list2=list(split(list,n))
print (list2)
