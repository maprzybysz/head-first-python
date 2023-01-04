def search_for_vowels(phrase: str) -> set:
    """Returns the vowels found in the phrase given as an argument."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Returns the set of letters
     from the letters variable found in the phrase variable."""

    return set(letters).intersection(set(phrase))
