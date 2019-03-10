#remove duplicates from a list
def print_ele(a):
    size=len(a)
    list=[]
    for i in range(size):
        k=i+1
        for j in ramge(k,size):
            if a[i]==a[j] and a[i] not in list:
                list.append(a[i])
    return list

    list1=[10, 20, 30, 20, 20, 30, 40,50, -20, 60, 60, -20, -20]
    print(print_ele(list1))
