from datetime import date


def vote(birth):
    current = date.today().year
    age = current - birth
    if age < 16:
        return f"With{age} years of age: DENIED"
    elif age < 18 or age >= 65:
        return f"With{age} years of age: OPTIONAL"
    elif age < 65:
        return f"With{age} years of age: MANDATORY"


ybirth = int(input("What year were you born? \n"))
print(vote(ybirth))
