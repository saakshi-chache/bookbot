def word_count(text):
    words = text.split()
    return len(words)


def character(text):
    text = text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
        #if char in char_count:
          #char_count[char] += 1
        #else:
            #char_count[char] = 1
    return char_count



def sorted_char(char_count):
    char_names = []

    for char, count in char_count.items():
        if char.isalpha():
            char_names.append({"char": char, "num": count})

    def sorted_num(item):
        return item["num"]
    
    char_names.sort(reverse=True, key=sorted_num)

    return char_names


