############ game package ##################
import game.characters.player
game.characters.player.get_player_info()

from game.characters import player
player.get_player_info()

from game.characters.boss import Boss
objBoss = Boss()
objBoss.get_boss_info()



########### DataStructure package ###########
from DataStructure.stack import Stack
from DataStructure.queue import Queue


########### Calculator package ##############
from Calculator.add import Add
from Calculator.subtract import Subtract
from Calculator.multiply import Multiply
from Calculator.division import Division


objAdd = Add()
result = objAdd.add_two_numbers(10, 5)
print("Addition Result = " + str(result))

objSub = Subtract()
result = objSub.sub_two_numbers(10, 5)
print("Subtraction Result = " + str(result))

objMul = Multiply()
result = objMul.multiply_two_numbers(10, 5)
print("Multification Result = " + str(result))

objDiv = Division()
result = objDiv.division_two_numbers(10, 5)
print("Division Result = " + str(result))







