#date and time
def convert(s1):
    if s1[-2:]=="AM" and s1[:2] == "12":
        return "00"+s1[2:-2]
    elif s1[-2:]=="AM":
        return s1[:-2]
    elif s1[-2:] == "PM" and s1[:2]=="12":
        return s1[:-2]
    else:
        return str(int(s1[:2])+12)+s1[2:8]


