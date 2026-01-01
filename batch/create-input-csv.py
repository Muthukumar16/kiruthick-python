import csv
import random

# Sample names to combine
first_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia"]
last_names = ["Johnson", "Smith", "Brown", "Prince", "Hunt", "Taylor", "Clark", "Lewis", "Walker", "Hall"]

with open("input.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "email"])  # header

    for i in range(1, 1201):  # 1200 records
        fname = random.choice(first_names)
        lname = random.choice(last_names)
        name = f"{fname} {lname}"
        email = f"{fname.lower()}.{lname.lower()}{i}@example.com"
        writer.writerow([i, name, email])

print("input.csv with 1200 records created.")
