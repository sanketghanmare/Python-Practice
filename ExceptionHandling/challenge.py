import sys


def division():
    while True:
        try:
            num1 = int(input("Please enter number 1: "))
            num2 = int(input("Please enter number 2: "))
            print(f"Division of Number 1 and Number 2 is: {num1 / num2}")
            break
        except ZeroDivisionError:
            print(f"Can't be divided")
        except TypeError:
            print("Type error occured")
        except ValueError:
            print("Please enter valid number")
        except EOFError:
            sys.exit(1)


if __name__ == '__main__':
    division()
