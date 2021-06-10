def find_Len(words):
    counter = 0    
    for i in words:
        counter += 1
    return counter
words = input("Enter words: ")
print(find_Len(words))