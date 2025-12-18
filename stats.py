def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    chars_count = {}
    for char in text.lower():
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    return chars_count


def sort_on(item):
    return item["num"]


def sort_dict(chars_dict):
    chars_list = []
    for char, count in chars_dict.items():
        chars_list.append({"char": char, "num": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
