def average(*args):
    print(type(args))
    print(f"args is {args}")
    print(f"*args is ", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


print(average(1, 2, 3, 4))


def tuppleBuilder(*arguments):
    return arguments


print()
m = tuppleBuilder("hello", "Planet", "earth", "take")
print(m)
print(type(m))


def print_backwards(*args):
    for word in args[::-1]:
        print(word[::-1], end=' ')


print()
print_backwards("Hello", "Planet", "Earth", "Take")


def kwargs_args(*args, **kwargs):
    print(kwargs)
    kwargs.pop('end', None)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)


with open("backward.txt", 'w') as backwards:
    kwargs_args("hello", "planet", "earth", "take", "me", "to", end='\n')
