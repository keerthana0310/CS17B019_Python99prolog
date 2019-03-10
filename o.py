def rotate(list,n):
    list1=[]
    for i in range(len(list)-n,len(list)):
        list1.append(list[i])
    for i in range(0,len(list)-n):
        list1.append(list[i])
    return list1

n=3
list=['1','2','3','4','5','6','7','8']
print(rotate(list,n))
