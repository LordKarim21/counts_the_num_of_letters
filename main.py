import collections


def start_program():
    text = input("Input text")
    return sorted_of_value(counts_the_number_of_letters(text))


def sorted_of_value(letters):
    answer = {}
    value_sum = sum(letters.values())
    letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    for key, value in letters:
        proc = 100 * (value / value_sum)
        answer[key] = str(round(proc, 2)) + "%"
    return answer


def counts_the_number_of_letters(text):
    letters_dict = collections.Counter(text)
    for key, value in letters_dict.items():
        if value == 0:
            letters_dict.pop(key)
    return letters_dict
