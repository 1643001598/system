# -*- coding: UTF-8 -*-

from time import sleep
from system100_103 import system_1_0_0, system_1_0_1, system_1_0_2, system_1_0_3
from system104 import system_1_0_4
from system105 import system_1_0_5
from system106 import system_1_0_6
from system110 import system_1_1_0
from system120 import system_1_2_0
from public import variables

s56 = variables.s56
a2 = [0, 1, 2, 3, 4, 5, 6, 10]


def time_sleep():
    print('\n正在进入...')
    sleep(0.5)
    print('\n****进入成功!****')


def g2():
    a = '==版本:1.{}.{}已准备就绪!=='
    if 0 in s56:
        print(a.format('0', '0'))
    if 1 in s56:
        print(a.format('0', '1'))
    if 2 in s56:
        print(a.format('0', '2'))
    if 3 in s56:
        print(a.format('0', '3'))
    if 4 in s56:
        print(a.format('0', '4'))
    if 5 in s56:
        print(a.format('0', '5'))
    if 6 in s56:
        print(a.format('0', '6'))
    if 10 in s56:
        print(a.format('1', '0'))
    if 20 in s56:
        print(a.format('2', '0'))
    if not s56:
        print('当前没有版本就绪!')
    if a2 == [x for x in a2 if x in s56]:
        print('所有版本已就绪!')
    elif s56:
        print('当前共有{}个版本就绪'.format(len(s56)))


def start():
    g2()
    n5 = input('\n请输入您想要进入的版本(输入版本的末尾号:整数0~6,10,20以进入)(输入c清空所有已就绪的版本):')

    if n5 == '0':
        if 0 in s56:
            print('\n进入成功!')
            system_1_0_0.system_1_0_0()
        else:
            s56.append(00)
            time_sleep()
            system_1_0_0.system_1_0_0()
    elif n5 == '1':
        if 1 in s56:
            print('\n进入成功!')
            system_1_0_1.system_1_0_1()
        else:
            s56.append(1)
            time_sleep()
            system_1_0_1.system_1_0_1()
    elif n5 == '2':
        if 2 in s56:
            print('\n进入成功!')
            system_1_0_2.system_1_0_2()
        else:
            s56.append(2)
            time_sleep()
            system_1_0_2.system_1_0_2()
    elif n5 == '3':
        if 3 in s56:
            print('\n进入成功!')
            system_1_0_3.system_1_0_3()
        else:
            s56.append(3)
            time_sleep()
            system_1_0_3.system_1_0_3()
    elif n5 == '4':
        if 4 in s56:
            print('\n进入成功!')
            system_1_0_4.system_1_0_4()
        else:
            s56.append(4)
            time_sleep()
            system_1_0_4.system_1_0_4()
    elif n5 == '5':
        if 5 in s56:
            print('\n进入成功!')
            system_1_0_5.system_1_0_5()
        else:
            s56.append(5)
            time_sleep()
            system_1_0_5.system_1_0_5()
    elif n5 == '6':
        if 6 in s56:
            print('\n进入成功!')
            system_1_0_6.system_1_0_6()
        else:
            s56.append(6)
            time_sleep()
            system_1_0_6.system_1_0_6()
    elif n5 == '10':
        if 10 in s56:
            print('\n进入成功!')
            system_1_1_0.system_1_1_0()
        else:
            s56.append(10)
            time_sleep()
            system_1_1_0.system_1_1_0()
    elif n5 == '20':
        if 20 in s56:
            print('\n进入成功!')
            system_1_2_0.system_1_2_0()
        else:
            s56.append(20)
            time_sleep()
            system_1_2_0.system_1_2_0()
    elif n5 == 'c':
        if not s56:
            print('\n没有版本就绪,无法清空!\n')
            start()
        print('\n正在清空...')
        sleep(len(s56) / 3)
        s56.clear()
        print('\n****已清空!****\n')
        start()
    else:
        print('\n选择无效!')
        start()


if __name__ == '__main__':
    start()
