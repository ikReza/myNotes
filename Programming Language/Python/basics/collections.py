from collections import Counter

random_string = "aaaaabbbbcccccaa"
my_counter = Counter(random_string)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

# find most common items
print(my_counter.most_common(1))
print(my_counter.most_common(2))