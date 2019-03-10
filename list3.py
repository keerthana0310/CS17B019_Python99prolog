#remove nth occurence of a given word
def remove(list,item,n):
    list1=[]
    count=0
    for i in list:
        if(i==item):
            count=count+1
            if (count!=n):
                list1.append(i)
        else:
            list1.append(i)
    list=list1
    
    if count == 0:
        print("no item")
    else:
        print(list)
    return list1


    list=["arr","ber","arr","cer","arr"]
    item="arr"
    n=3

    
    remove(list,item,n)
            
