#check binary is palindrome or not
def bin_pal(n):
    binary=bin(n)
    binary=binary[2:]
    return binary==binary[-1::-1]
