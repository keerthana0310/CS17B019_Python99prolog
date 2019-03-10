#linear search
def search(a,x):
    for i in range(len(a)):
        if a[i]==x:
            return i
    return -1
#input array,x
