def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_desc(char_dict):
    sorted_list = sorted(char_dict.items(), reverse=True, key=lambda x: x[1])
    return {key: value for key, value in sorted_list if key.isalpha()}


