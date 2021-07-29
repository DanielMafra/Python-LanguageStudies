def readint(user):
    ok = False
    value = None
    while True:
        number = input(f"{user} \n")
        if number.isnumeric():
            value = number
            ok = True
        else:
            print("\033[0;31mERROR! Try again!\033[m")
        if ok:
            break
    return value


n = readint("Enter a value:")
print(f"You enter a number: {n}.")
