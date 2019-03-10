def pack(list):
    list1 = []
    for item in set(list):
        list1.append([item] * list.count(item))

    return list1

list= [1, 2, 10, 3, 4, 1, '5', 2, 3, 1, 4, '5']

print (pack(list))
