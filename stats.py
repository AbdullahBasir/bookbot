def word_count(file):

    word = file.split()
    num_words = len(word)
    return num_words

def text_dict(file):
    chars = {}
    for i in file.lower():
        if i not in chars:
            chars[i] = 1
        else:
            chars[i] += 1
        
    return chars

def sort_dict(sort):
    
    to_be_sorted = []

    for key in sort:
        small_dict = {}
        small_dict["char"] = key
        small_dict["num"] = sort[key]
        to_be_sorted.append(small_dict)

    to_be_sorted.sort(reverse=True, key=sort_on)

    return to_be_sorted

def sort_on(items):
    return items["num"]
