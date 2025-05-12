import string

def get_num_words(text):
    return len(text.split())

def get_letter_count(text):
    letter_count = {}
    text = text.lower()
    for character in text:
        if character in string.ascii_lowercase:
            if character in letter_count:
                letter_count[character] += 1
            else:
                letter_count[character] = 1
    return letter_count

""" def get_sorted_dict(dict):
    dict.sort(reverse=True)
    print(dict) """
