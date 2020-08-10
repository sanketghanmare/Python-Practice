from player import Player

tim = Player("Tim")

# print(tim.name)
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 9
# print(tim)
#
# tim.level = 2
# print(tim)
#
# tim.level += 5
# print(tim)
#
# tim.level = 3
# print(tim)
#
# tim.score = 500
# print(tim)

from enemy import Enemy, Troll, Vampyre, VampyreKing

# monster = Enemy("Basic Enemy", 12, 1)
#
# monster.take_damage(4)
# print(monster)

# python does not have a concept of overloading method(method overloading)
# ugly_troll = Troll("Pug")
# print(f"ugly Troll {ugly_troll}")
#
# another_troll = Troll('Ug')
# print(f"Another troll {another_troll}")
#
# brother = Troll('Urg')
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# blood = Vampyre("Blood")
# print(blood)
#
# blood.take_damage(1)
# print(blood)
#
# # while blood.alive:
# #     blood.take_damage(1)
#
# blood._lives = 0
# blood._hit_points = 1
# print(blood)

dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(12)
dracula.take_damage(12)
dracula.take_damage(12)
dracula.take_damage(12)
dracula.take_damage(12)
print(dracula)
