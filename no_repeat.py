def first_non_repeating_letter(string):
    lower = string.lower()
    if not string:
        return "t"
    for i in range(len(lower)):
        if lower.count(lower[i]) == 1:
            return string[i]
    return ""
# print(first_non_repeating_letter('hello world, eh?'))

# print(first_non_repeating_letter('a'))
print(first_non_repeating_letter())
# print(first_non_repeating_letter('moonmen'))


# print(first_non_repeating_letter(''))

# print(first_non_repeating_letter('abba'))
# print(first_non_repeating_letter('aa'))


# print(first_non_repeating_letter('~><#~><'))
# print(first_non_repeating_letter('hello world, eh?'))


# print(first_non_repeating_letter('sTreSS'))
# print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))