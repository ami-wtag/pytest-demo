from faker import Faker

# faker.Faker can take a locale as an argument, to return localized data.
fake = Faker(["en_US"])


print("name: ", fake.name())
print("email: ", fake.email())
print("first_name: ", fake.first_name())
print("last_name: ", fake.last_name())
print("address: ", fake.address())
print("city: ", fake.city())
print("country: ", fake.country())
print("country_code: ", fake.country_code())
print("sentence: ", fake.sentence())
print("text: ", fake.text())
print("zipcode: ", fake.zipcode())
print("locale: ", fake.locale())
print("license_plate: ", fake.license_plate())
print("phone_number: ", fake.phone_number())

print("hexify: ", fake.hexify(text="MAC: ^^:^^:^^:^^:^^", upper=True))
print("bothify: ", fake.bothify(text="ID:2024:???:####:???", letters="ABCDE"))

"""
Example
-------
name:  Brad Brown
email:  jenniferallen@example.org
first_name:  Kim
last_name:  Vargas
address:  42162 Vasquez Dam
New David, SC 77581
city:  Chadborough
country:  Malaysia
country_code:  GW
sentence:  Particular remember manager ahead couple during.
text:  Table improve friend western never. Which those around. Real debate source machine race night drive. Sister right modern just size stock remain.
zipcode:  64723
locale:  bs_BA
license_plate:  1SF L92
phone_number:  001-626-594-0082
hexify:  MAC: B9:F3:3E:BF:6F
bothify:  ID:2024:EDA:6760:CBD
"""
