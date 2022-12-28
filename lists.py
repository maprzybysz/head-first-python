prices = []
temps = [0.0, 100, -17.78, 27.5, 37.78, 7.39]
words = ['hello', 'world']
car_details = ['Toyota', 'RAV4', 2.2, 60807]
everything = [prices, temps, words, car_details]
odds_and_ends = [[1, 2, 3], ['a', 'b', 'c'], ['one', 'two', 'three']]

# Delete a given value 
temps.remove(0.0);

# Delete and returns object from ist with specified index, if you do not specify an index he last element is deleted 
temps.pop(0);

temps.extend([1,2,3])

temps.insert(0,1);