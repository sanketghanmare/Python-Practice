class Kettle(object):
    # Class attribute share by all instances
    power_source = 'electricity'

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print("Price updated", kenwood.price)

hamilton = Kettle('Hamilton', 14.55)

print(hamilton.make)

print(f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}")

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# Another approach to use switch on
Kettle.switch_on(kenwood)
print(kenwood.on)

kenwood.power = 200

print(kenwood.power)

# Hamilton instance does not have power attribute like kenwood, this is dynamic nature of python
# print(hamilton.power)

print(Kettle.power_source)
print(kenwood.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)










