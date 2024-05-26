# Write your solution here
def list_sums(lis1,lis2):
    nlis = []
    for i in range(len(lis1)):
        nlis.append(lis1[i] + lis2[i])
    return nlis
    
lis1 = [1,2,3,4]
lis2 = [5,6,7,8]

list_sums(lis1, lis2)