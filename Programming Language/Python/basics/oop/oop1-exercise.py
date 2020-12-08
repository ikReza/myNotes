# oop1-exercise
#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Tom", 4)
cat2 = Cat("Cricket", 1)
cat3 = Cat("Mentos", 9)


# 2 Create a function that finds the oldest cat
def find_old(*args):
    age_list = [x.age for x in args]
    return max(age_list)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
get_oldest = find_old(cat1, cat2, cat3)

print(f"The oldest cat is {get_oldest} years old.")