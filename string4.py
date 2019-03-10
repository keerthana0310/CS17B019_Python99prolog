#palindrome
def rev(str):
    return str[::-1]
def is_pal(str):
    reverse=rev(str)
    if(str==reverse):
        return True
    return False
#enter the string
res=is_pal(str)
if res==1:
    print("Yes")
else:
    print("No")
