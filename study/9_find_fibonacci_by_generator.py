def fib_generator():
    a, b = 0, 1
    while True:
        print("1g",b)
        yield b
        print("2g",b)
        a, b = b, a+b
        print("3g", a, b)
        print()

if __name__ == "__main__":
    fg = fib_generator()
    for _ in range(10):
        # print(next(str(_)))
        # print(fg)
        print("r",next(fg), end=" ")
        # print()