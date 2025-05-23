def get_word_count(book):
    split_book = book.split()
    return len(split_book)

def get_char_count(book):
    split_book = book.split()
    char_dict = {}
    for w in split_book:
        for c in list(w):
            low_c = c.lower()
            if low_c not in char_dict:
                char_dict[low_c] = 1
            else:
                char_dict[low_c] += 1
    return char_dict

def sort_on(dict_item):
    return dict_item["num"]

def get_sorted_char_count(char_dict):
    dict_list = []
    for key in char_dict:
        new_dict = {"char": key, "num": char_dict[key]}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

