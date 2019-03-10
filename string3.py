#permutations of a string
from itertools import permutations
def per(str):
    perlist=permutations(str)
    for perm in list(perlist):
        print(''.join(perm))
if_name_=="main":
    str='ABC'
    per(str)
