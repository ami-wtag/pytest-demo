from faker import Faker

fake = Faker()


for _ in range(10):
    print(fake.unique.random_int(min=1, max=10), end=', ')


for _ in range(5):
    print(fake.unique.first_name(), end=', ')


for _ in range(5):
    # Raises a UniquenessException at 3rd iteration
    print(fake.unique.boolean())

"""
Example
-------
5, 2, 3, 4, 9, 1, 6, 10, 7, 8,

Elizabeth, James, Thomas, Jason, Johnny,

True
False
Raises a UniquenessException
"""
