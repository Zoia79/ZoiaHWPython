n = int(input("Введите число:"))

def fizz_buss(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print(f"{i} - Fizz")
        elif i % 5 == 0:
            print(f"{i} - Buzz")
        elif i % 15 == 0:
            print(f"{i} - FizzBuzz")
        else:
            print(i)

fizz_buss(n)