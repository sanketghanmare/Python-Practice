def spam1():
    def spam2():
        def spam3():
            z = " even more spam "
            z += y
            print(f"In spam3, locals are {locals()}")
            return z

        y = " more spam " + x
        y += spam3()
        print(f"In spam2, locals are {locals()}")
        return y

    x = " spam "
    x += spam2()
    print(f"In spam1, locals are {locals()}")
    return x

print(spam1())