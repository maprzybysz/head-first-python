# def search_for_vowels(word):
#     """Displays the vowels found in the word specified by the user.""" 
#     vowels = set('aeiou')

#     found = vowels.intersection(set(word))
#     for vowel in found:
#         print(vowel)


# word = input('Give a word in which to look for vowels: ');

# def search_for_vowels(word):
#     # """Returns a logical value depending on whether any vowels are found."""
#     """Returns the vowels found in the word given as an argument."""
#     vowels = set('aeiou')

#     # found = 
#     return vowels.intersection(set(word))
#     # return bool(found)
#     # return found


# def search_for_vowels(phrase:str) -> set:
#     """Returns the vowels found in the phrase given as an argument."""
#     vowels = set('aeiou')
#     return vowels.intersection(set(phrase))

# print(search_for_vowels('mm'))
# print(type(search_for_vowels('mm')))
# help(search_for_vowels)

def search_for_letters(phrase : str, letters:str='aeiou') -> set:
    """Returns the set of letters from the letters variable found in the phrase variable."""

    return set(letters).intersection(set(phrase))


print(search_for_letters('mierni', 'aeiou'))
print(search_for_letters('galaktyka', 'tym'))
print(search_for_letters('Zycie, wszechświat i całą reszta'))
print(search_for_letters(phrase='galaktyka', letters='tym'))