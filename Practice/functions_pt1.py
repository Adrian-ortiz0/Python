""""
def print_many_times(text, times):
    
    i = 0
    while i < times:
        print(text)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)
"""

"""
def hash_square(length):
    i = 0
    while i < length:
        print("#" * length)
        i += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(1)
"""

"""
def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1
"""

def squared(characters, size):
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += characters[i % len(characters)]
        i += 1
    print(row)