"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)  # TODO: replace this line with your code


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums
    # TODO: replace this line with your code


def get_odd_indices(items):
    result = []
    for indx, item in enumerate(items):
        if indx % 2 != 0:
            result.append(item)

    return result  # TODO: replace this line with your code


def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f"{i} {item}")
        i += 1

    # TODO: replace this line with your code


def get_range(start, stop):
    nums = []
    for i in range(start, stop):
        nums.append(i)
        i += 1

    # print(nums)  # TODO: replace this line with your code


def censor_vowels(word):
    chars = []
    for char in word:
        if char in "aeiou":
            char = "*"
            chars.append(char)
        else:
            chars.append(char)
    print("".join(chars))

    # TODO: replace this line with your code


def snake_to_camel(string):
    camel_case = []
    string_list = string.split("_")
    for word in string_list:
        # camel_case.append(f"{word[0].upper()}{word[1:]}")  #FIRST METHOD

        camel_case.append(word[0].upper())  # SECOND METHOD
        camel_case.append(word[1:])

    print("".join(camel_case))  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
