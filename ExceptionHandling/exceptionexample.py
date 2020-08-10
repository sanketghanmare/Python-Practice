def factorial(n):
    # n! can also be defined as a n * (n-1)!
    """ Calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    print(factorial(999))
except RecursionError:
    print("Program can't calculate that big factorial")

print("Program Terminating")
