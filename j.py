#run length
def runlength(list):
    list1=[]
    count=1
    len_list=len(list)
    for i in range(len_list):
        if i==len_list-1:

            if list[i]==list[i-1]:
                count=count+1
                list1.append(count)
                return list1

list=['a','a','a','b','b','c']
print(runlength(list)
            
