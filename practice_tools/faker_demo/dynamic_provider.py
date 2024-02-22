from faker import Faker
from faker.providers import DynamicProvider

fake = Faker()


framework_provider = DynamicProvider(
    provider_name="framework",
    elements=["FastAPI", "Django", "Flask"]
)


fake.add_provider(framework_provider)

for _ in range(5):
    print(fake.framework())

"""
Example
-------
Flask
FastAPI
Django
Flask
FastAPI
"""
