#quick sort
#partition function
def par(arr,a,b):
    i=(a-1)
    pivot=arr[b]
    for j in range(a,b):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[b]=arr[b],arr[i+1]
    return (i+1)
#quict sort function
def quick_sort(arr,a,b):
    if a<b:
        p=par(arr,a,b)
        quick_sort(arr,a,p-1)
        quick_sort(arr,p+1,b)
        
