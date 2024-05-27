# Write your solution here
def length_of_longest(lis):
    longes = len(lis[0])
    for i in lis:
        if longes < len(i):
            longes = len(i)
    return longes
    





if __name__ == "__main__":
    
    my_list = ['Alan', 'Grace', 'Frances', 'Kim', 'Susan']
    result = length_of_longest(my_list)
    print(result)