import csv
from faker import Faker


faker = Faker('ru_RU')


num_entries = 1000
test_data = []

for _ in range(num_entries):
    is_female = faker.random_element(["female", "male"]) == "female"
    last_name = faker.last_name_female() if is_female else faker.last_name_male()

    entry = {
        "surname": last_name,
        "first_name": faker.first_name_female() if is_female else faker.first_name_male(),
        "middle_name": faker.middle_name_female() if is_female else faker.middle_name_male(),
        "organization": faker.company(),
        "work_phone": faker.phone_number(),
        "personal_phone": faker.phone_number(),
        "address": faker.address(),
        "email": faker.email(),
    }
    test_data.append(entry)


csv_file = "data/test_data.csv"
fieldnames = test_data[0].keys()

with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(test_data)

print(f"Тестовые данные успешно сгенерированы и сохранены в файл {csv_file}.")