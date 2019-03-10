#count +ve and -ve numbers in a list
list=[10,-2,45,-69,100,0,4,-78]
pos_count,neg_count=0,0
for n in list:
    if n >= 0:
        pos_count+=1
    else:
        neg_count+=1
        
print(pos_count)
print(neg_count)
