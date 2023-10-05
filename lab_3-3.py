import random

# I was not able to do this lab in class, so classmat echecks are empty

random_integer = random.randint(1, 100)
print(f"Random Integer between 1 and 100: {random_integer}")

random_seed = 42  # my dad suggested the number 7
random.seed(random_seed)

random_even = random.randrange(0, 101, 2)
print(f"Random Even Number between 0 and 100: {random_even}")