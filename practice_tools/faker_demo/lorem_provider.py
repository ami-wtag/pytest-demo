from faker import Faker

fake = Faker()


my_word_list = [
    'I', "am", "Kamal", "sky",
    "bar", "food", "sugar", "oats"
]

print(fake.sentence())

print(fake.sentence(ext_word_list=my_word_list))

"""
Example
-------
Smile teach door.
Sugar Kamal food.
"""
