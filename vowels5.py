vowels = ['a', 'e', 'i', 'o', 'u'] # = set('aeiou')
word = input('Give a word in which to look for vowels: ');

found = set(vowels).intersection(word) # vowels.intersection(set(word))
print(found)