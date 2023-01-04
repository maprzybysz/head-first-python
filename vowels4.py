vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Give a word in which to look for vowels: ');

found = {}


for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'found', v, 'times')