from time import sleep


def write(txt):
    tam = len(txt) + 4
    print("~" * tam)
    print(f"  {txt}")
    print("~" * tam)


def pyhelp(comand):
    help(comand)


def default():
    while True:
        write("Helper system PyHELP")
        funcorlib = input("Function or Lib > ")

        if funcorlib[0].lower() == "f":
            break
        else:
            pyhelp(funcorlib)


default()
