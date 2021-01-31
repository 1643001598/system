# -*- coding: UTF-8 -*-
from random import randint
from system.system104 import system_1_0_4
global f2020, b2020, c2020, e2020, d2020, a2020, a5e, v1, point2, point3


def a2():
    pass


def cheng_fa(f4):
    print('\n'.join([' '.join(['%s x %s = %-2s ' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 100)]))
    f4()


def er_yuan(f3):
    global f2020, b2020, c2020, e2020, d2020, a2020
    try:
        a2020 = int(input('\na1='))
        b2020 = int(input('\nb1='))
        c2020 = int(input('\nc1='))
        d2020 = int(input('\na2='))
        e2020 = int(input('\nb2='))
        f2020 = int(input('\nc2='))
    except ZeroDivisionError:
        print('\n原方程无解!')
        er_yuan(1)
    except ValueError:
        print('\n原方程无解!')
        er_yuan(1)
    x = (f2020 * b2020 - c2020 * e2020) / (d2020 * b2020 - a2020 * e2020)
    y = (a2020 * f2020 - d2020 * c2020) / (e2020 * a2020 - b2020 * d2020)
    print('\nx=', x)
    print('\ny=', y)
    f3()


def cai_shu_zi():
    try:
        import random
        a1000 = random.randint(0, 200)
        while True:
            b1000 = int(input("\n按0退出\n \n猜一个0~200之间的数字:"))
            if b1000 == 0:
                break
            elif b1000 > a1000:
                print("\n这个数字太大了")
            elif b1000 < a1000:
                print("\n这个数字太小了")
            else:
                print("\n恭喜，你猜对了，这个数字是:{}!".format(a1000))
                break
    except ValueError:
        print('\n格式错误!!!')
        cai_shu_zi()


def help2(f):
    print("\n---欢迎进入help主界面!")
    print(
        '\n***退出请按0***\n\n***重新登录请按1***\n\n***掷骰子请按2\n\n***猜数字请按3***\n\n***解二元一次方程组请按4***\n\n***测试电脑性能请按5***\n\n'
        '***查看九九九九乘法表请按6***\n\n***进入管理员请按7***\n\n***返回开始请按8***\n\n***查看更新内容请按9***')
    # print('')
    f()


def po_yi(f5):
    global a5e
    print('\n电脑性能测试(输入0退出)')
    try:
        a5e = int(input('\n(5位以内)请输入:'))
    except NameError:
        print('\n错误!')
        po_yi(a2)
    except ValueError:
        print('\n错误!')
        po_yi(a2)
    if a5e == 0:
        f5()
    if 100000 > a5e > 0:
        while True:
            for item in range(0, 100000, 1):
                print(item)
                if item == a5e:
                    break
            print("\nfinished:{}!".format(a5e))
            break
    else:
        print('\n错误!')
        po_yi(a2)


def toss():
    global v1, point2, point3
    y1 = 0
    point2 = 0
    point3 = 0
    try:
        v1 = int(input('\n输入0退出\n\n请输入您想骰的次数(最大100000):'))
    except ValueError:
        print('\n无效选择!')
        toss()
    if v1 == 0:
        system_1_0_4.zhu_ye_mian()
    elif v1 > 100001:
        print('\n数值过大!')
        toss()
    elif v1 < 0:
        print('\n无效选择!')
        toss()
    while y1 != v1:
        point = randint(1, 6)
        point1 = randint(1, 6)
        print("\n电脑点数：", point)
        if point == 1:
            print("=========\n=       =\n=   0   =\n=       =\n=========")
        elif point == 2:
            print("=========\n= 0     =\n=       =\n=     0 =\n=========")
        elif point == 3:
            print("=========\n= 0     =\n=   0   =\n=     0 =\n=========")
        elif point == 4:
            print("=========\n= 0   0 =\n=       =\n= 0   0 =\n=========")
        elif point == 5:
            print("=========\n= 0   0 =\n=   0   =\n= 0   0 =\n=========")
        elif point == 6:
            print("=========\n= 0   0 =\n= 0   0 =\n= 0   0 =\n=========")
        print("\n玩家点数：", point1)
        if point1 == 1:
            print("=========\n=       =\n=   0   =\n=       =\n=========")
        elif point1 == 2:
            print("=========\n= 0     =\n=       =\n=     0 =\n=========")
        elif point1 == 3:
            print("=========\n= 0     =\n=   0   =\n=     0 =\n=========")
        elif point1 == 4:
            print("=========\n= 0   0 =\n=       =\n= 0   0 =\n=========")
        elif point1 == 5:
            print("=========\n= 0   0 =\n=   0   =\n= 0   0 =\n=========")
        else:
            print("=========\n= 0   0 =\n= 0   0 =\n= 0   0 =\n=========")
        if point1 > point:
            print("\n你胜!")
        elif point1 < point:
            print("\n电脑胜!")
        else:
            print("\n平局!")
        y1 += 1
        point2 += point
        point3 += point1
    print('\n你的总点数:', point2, '\n\n电脑的总点数:', point3)
    if point2 > point3:
        print('\n**********************你胜!**********************')
    elif point2 < point3:
        print('\n**********************电脑胜!**********************')
    else:
        print('\n**********************平局!**********************')
    toss()


if __name__ == '__main__':
    def test():
        n5 = input()
        if n5 == '0':
            cheng_fa(test)
        elif n5 == '1':
            er_yuan(test)
        elif n5 == '2':
            cai_shu_zi()
        elif n5 == '3':
            help2(test)
        elif n5 == '4':
            po_yi(test)
        elif n5 == '5':
            toss()
        else:
            test()


    test()
