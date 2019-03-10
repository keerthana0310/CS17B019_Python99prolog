#f=open("1.txt","r")
#print(f.read())
def count(fname):
    with open(fname) as f:
        return counter(f.read().split())
print(" words :",count("1.txt"))
