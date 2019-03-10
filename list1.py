#swapping  2 items in a list
def swap(list,a,b):
    list[a],list[b]=list[b],list[a]
    return list
list=[223,5,56,657]
a,b=1,3
result=swap(list,a,b)
print(result)
