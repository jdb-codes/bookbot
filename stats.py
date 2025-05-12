def get_num_words(text):
    return len(text.split())

def get_letter_count(text):
    letter_count = {}
    text = text.lower()
    for character in text:
        if character.isalpha():
            if character in letter_count:
                letter_count[character] += 1
            else:
                letter_count[character] = 1
    return letter_count

def get_sorted_dict(dict):
    letter_list = []
    for key in dict:
        letter_list.append({
            "name": key,
            "num": dict[key]
        })
    def sort_on(dict):
        return dict["num"]
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list
