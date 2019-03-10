def reverse(list): 
    return list[::-1] 
def pal(list): 
    rev = reverse(list) 
    if (list == rev): 
        return True
    return False
list = ['1','2','3','5','1']
res = pal(list) 
if res == 1: 
    print("Yes") 
else: 
    print("No") 
