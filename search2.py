#binary search through recursion
def bin_search(arr,x,a,b):
    if b>=a:
        mid=a+(b-1)/2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return bin_search(arr,x,a,mid-1)
        else:
            return bin_search(arr,x,mid+1,b)
    else:
        return -1
