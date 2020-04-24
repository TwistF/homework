#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: fight.py
@time: 2020/4/10  18:52
"""
from human import Human
from dog import Dog
import random
import time

human_list = []
dog_list = []
for i in range(2):
    human_list.append(Human(i+1))
for i in range(3):
    dog_list.append(Dog(i+1))

turn = random.randint(0, 1)   # 0代表人先手，1代表狗先手
print(turn)
while True:
    time.sleep(0.1)
    if human_list == []:
        print("狗方胜利")
        break
    if dog_list == []:
        print("人方胜利")
        break
    if turn == 0:
        attacker = random.randint(0, len(human_list)-1)
        defender = random.randint(0, len(dog_list)-1)
        dog_list[defender].hurt(human_list[attacker].attack)
        print("人%d对狗%d造成了%d点伤害"%(human_list[attacker].no, dog_list[defender].no, human_list[attacker].attack))
        if dog_list[defender].alive == False:
            print("狗%d阵亡"%dog_list[defender].no)
            dog_list.remove(dog_list[defender])
        turn = 1
        continue

    if turn == 1:
        attacker = random.randint(0, len(dog_list)-1)
        defender = random.randint(0, len(human_list)-1)
        human_list[defender].hurt(dog_list[attacker].attack)
        print("狗%d对人%d造成了%d点伤害"%(dog_list[attacker].no, human_list[defender].no, dog_list[attacker].attack))
        if human_list[defender].alive == False:
            print("人%d阵亡"%human_list[defender].no)
            human_list.remove(human_list[defender])
        turn = 0
        continue

