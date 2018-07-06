flowers = ['Lily', 'Snapdragon', 'Rose', 'Tulip']
bees = ['bumblebee', "honeybee", "dobee", "Aybee"]

# With a comprehension
large_flowers = [
  f'the {bee} pollinates the {flower}'
  for flower in flowers
  for bee in bees
]

# With a loop
large_flowers = []
for flower in flowers:
  for bee in bees:
    large_flowers.append(f'the {bee} pollinates the {flower}')

print(large_flowers)

my_family = {
    'sister': {
        'name': 'Sarah',
        'age': 43
    },
    'mother': {
        'name': 'Judy',
        'age': 76
    },
    'father': {
        'name': 'Ray',
        'age': 79
    }
}

# Standard way with a loop. BTW, family_stuff could be a list or a tuple, too. doesn't matter
# family_stuff = set()
# for family_member, member_values in my_family.items():
#   family_stuff.add(f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old' )

# With comprehension instead
family_stuff = {
  f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.'
  for (family_member, member_values) in my_family.items()
}

print("My family!", family_stuff)
