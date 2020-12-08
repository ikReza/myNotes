# empty list
li = []
print(li, type(li))

my_list = list()
print(my_list, type(my_list))

my_list = [1] * 5
print(my_list)

my_list = [1, 3, -2, 9, 5, 0]
new_list = sorted(my_list)
print(my_list, new_list)
print(my_list[::2])

# list copy
my_li = ["apple", "banana"]

# method-1
new_li1 = list(my_li)
new_li1.append("orange")
# method-2
new_li2 = my_li[:]
new_li2.append("lemon")

print(my_li)
print(new_li1)
print(new_li2)

# list comprehension
my_list = [1, 2, 3, 4]
new_list = [i*i for i in my_list]
print(new_list)