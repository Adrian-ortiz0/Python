def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):      #calcula la cantidad de veces que cabe sub_string en String
        if string[i : i + len(sub_string)] == sub_string:   #Hace un slice de string donde este arranca desde 0 y arropa hasta la longitud
                                                            #donde esta tambien se ira sumando de a 1
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)