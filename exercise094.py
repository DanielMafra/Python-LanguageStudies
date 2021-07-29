person = dict()
info, names, nquantity, ages, women, above = list(
), list(), list(), list(), list(), list()

while True:
    person['name'] = input("Name: \n")
    gender = input("Gender [M/F]: \n")
    gender = gender[0].upper()
    person['gender'] = gender
    person['age'] = float(input("Age: \n"))
    info.append(person.copy())
    leave = input("Continue? [Y/N] \n")
    leave = leave.upper()
    if leave[0] == "N":
        break

for dictionary in info:
    nquantity.append(dictionary.get("name"))
    ages.append(dictionary.get("age"))
    age = sum(ages)/len(ages)
    for key, value in dictionary.items():
        if value == "F":
            women.append(dictionary.get("name"))
    if dictionary.get("age") > (age):
        above.append(dictionary.get("name"))

print(f"Registered people: {len(nquantity)}")
print(f"Average age of the group: {age:.1f} anos.")
print(f"Group women: {women}")
print(f"People over the average age: {above}")
