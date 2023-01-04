vowels = {'a', 'e', 'e', 'i', 'o', 'u', 'u'}
print(vowels) # {'e', 'a', 'i', 'u', 'o'}

vowels2 = set('aeeiouu')
print(vowels2) #{‘i’, ‘u’, ‘o’, ‘e’, ‘a’}

word = 'halo'

u = vowels.union(set(word))
print(u) #{'h', 'l', 'o', 'i', 'a', 'u', 'e'}
u_list = sorted(list(u))
print(u_list) #['a', 'e', 'h', 'i', 'l', 'o', 'u']

d = vowels.difference(set(word))
print(d) # {‘i’, ‘u’, ‘e’}

i = vowels.intersection(set(word))
print(i) # {‘o’, ‘a’}