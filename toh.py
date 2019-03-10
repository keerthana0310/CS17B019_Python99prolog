#tower of hanoi
def toh(n,from_rod,to_rod,aux_rod):
    if n==1:
        print "move disk 1 from rod ",from_rod,"to rod ",to_rod
        return
    toh(n-1,from_rod,aux_rod,to_rod)
    print "move disk ",n" from rod",from_rod,"to rod ",to_rod
    toh(n-1,aux_rod,to_rod,from_rod)
