def get_unique( words ):
    unique_words = []
    for i in words :
        if i not in unique_words : unique_words.append(i)
    return unique_words

words = ['x', 'y', 'z', 'y', 'xyz', 'z']
print(get_unique(words))