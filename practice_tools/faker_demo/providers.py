import random

from faker import Faker
from faker.providers import BaseProvider

fake = Faker()


class TopicProvider(BaseProvider):

    def topic_list(self):
        return random.choice([
            'Machine Leaning',
            'Artificial Inteligence',
            'Software Engineering'
        ])


fake.add_provider(TopicProvider)

for _ in range(5):
    print(fake.topic_list())


"""
Example
-------
Machine Leaning
Machine Leaning
Software Engineering
Machine Leaning
Artificial Inteligence
"""
