from time import sleep


def counter(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(f"Counting from {i} to {f} of {p} in {p}.")

    if i < f:
        counter = i
        while counter <= f:
            print(f"{counter} ", end="")
            sleep(0.2)
            counter += p
        print("End")
    else:
        counter = i
        while counter >= f:
            print(f"{counter} ", end="")
            sleep(0.2)
            counter -= p
        print("End")


start = int(input("Start: \n"))
end = int(input("End: \n"))
step = int(input("Step: \n"))

counter(1, 10, 1)
counter(10, 0, 2)
counter(start, end, step)
