
word = input("Please type in a string: ")
# 20 - la longitud de la palabra
size = 20 - len(word)
# multiplicamos el resultado de size por los asteriscos, imprimimos y concatenamos
print(("*" * size) + word)