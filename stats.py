def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_chars(book_text):
    char_count = {}
        
    for chars in book_text:
        lower_char=chars.lower()

        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def create_list(char_count):
    final_list = []
    
    for key, value in char_count.items():
       new_dict = {}
       new_dict["char"] = key
       new_dict["num"] = value 
       final_list.append(new_dict)
    final_list.sort(reverse=True, key=sort_on)
    return final_list


   
        



