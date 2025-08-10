def get_num_words(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    with open(path) as f:
        contents = f.read()
        split_content = contents.split()
        text_quantity = 0
        
        for i in split_content:
            text_quantity += 1
        print("----------- Word Count ----------")
        print(f"Found {text_quantity} total words")
        
        return contents, text_quantity
    
def get_num_char():
    char_count = {}
    char_list = []

    content, count = get_num_words()
    content = content.lower()
    for i in content:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    for n in char_count:
        if n.isalpha():
            char_list.append({"char": n, "num": char_count[n]})

    char_list.sort(reverse=True, key=sort_on)
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    return char_list

def sort_on(dict):
    return dict["num"]