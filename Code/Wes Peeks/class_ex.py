class character:



    def __init__(self, hp, dp, ap):
        self.__health = hp
        self.__defense = dp
        self.__attack = ap

    def __str__(self):
        return str(self.__health) + str(self.__attack) + str(self.__defense)



    def damage(self):
        return self.__attack


    def take_dam(self, dam):
        if dam > self.__defense:
            self.__health -= dam - self.__defense

    def ret_def(self):
        return self.__defense


    def is_dead(self):
        if self.__health <=0:
            return True
        else:
            return False




class wizard_kobold(character):
    __fireball = 10


    def __init__(self, fire):
        self.__fireball = fire
        super().__init__(1, 1, 1)

    def fireball(self):
        print(wizard_kobold.__fireball)
        return self.__fireball

    def take_dam(self, dam):
        super().take_dam(dam + super().ret_def())



wk = wizard_kobold(5)

print(wk.fireball())


# my_char = character(10,5,5)
#
# enemy = wizard_kobold(20)
#
# # print(my_char,enemy)
# #
# #
# # enemy.take_dam(my_char.damage())
# #
# #
# #
# # print(my_char,enemy)
#
# combat = True
#
# while combat:
#     print(my_char, enemy)
#     enemy.take_dam(my_char.damage())
#     my_char.take_dam(enemy.damage())
#     print(my_char, enemy)
#     if enemy.is_dead() or my_char.is_dead():
#         break
#
#     enemy.take_dam(my_char.damage())
#     my_char.take_dam(enemy.fireball())
#     print(my_char, enemy)
#     if enemy.is_dead() or my_char.is_dead():
#         break
#
