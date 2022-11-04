word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "beer on the wall.")
    print(beer_num, word, "beers.")
    print("Take one.")
    print("Pass around.")
    if beer_num == 1:
        print("No more beer bottles on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "beer on the wall.")
    print()