# -*- coding: UTF-8 -*-
import start
import random

a5 = ""
a4 = ""
a3 = ""
a2 = ""
c = ''
d = ''
i = ''
f1 = {}
z_m = {1: '1'}
a100 = ['123456']


def 二元():
    a1 = eval(input('a1='))
    b1 = eval(input('b1='))
    c1 = eval(input('c1='))
    a9 = eval(input('a2='))
    b2 = eval(input('b2='))
    c2 = eval(input('c2='))

    x = (c2 * b1 - c1 * b2) / (a9 * b1 - a1 * b2)
    y = (a1 * c2 - a9 * c1) / (b2 * a1 - b1 * a9)
    print('x=', x)
    print('y=', y)


def 猜数字():
    a = random.randint(0, 200)
    while True:
        b = int(input("按0退出\n猜一个0~200之间的数字:"))
        if b == 0:
            break
        elif b > a:
            print("这个数字太大了")
        elif b < a:
            print("这个数字太小了")
        else:
            print("恭喜，你猜对了，这个数字是:{}!".format(a))
            break


def toss():
    point = random.randint(1, 6)
    point1 = random.randint(1, 6)
    if point == 1:
        print("电脑点数：", point)
        print("=========\n=       =\n=   0   =\n=       =\n=========")
    elif point == 2:
        print("电脑点数：", point)
        print("=========\n= 0     =\n=       =\n=     0 =\n=========")
    elif point == 3:
        print("电脑点数：", point)
        print("=========\n= 0     =\n=   0   =\n=     0 =\n=========")
    elif point == 4:
        print("电脑点数：", point)
        print("=========\n= 0   0 =\n=       =\n= 0   0 =\n=========")
    elif point == 5:
        print("电脑点数：", point)
        print("=========\n= 0   0 =\n=   0   =\n= 0   0 =\n=========")
    elif point == 6:
        print("电脑点数：", point)
        print("=========\n= 0   0 =\n= 0   0 =\n= 0   0 =\n=========")
    if point1 == 1:
        print("玩家点数：", point1)
        print("=========\n=       =\n=   0   =\n=       =\n=========")
    elif point1 == 2:
        print("玩家点数：", point1)
        print("=========\n= 0     =\n=       =\n=     0 =\n=========")
    elif point1 == 3:
        print("玩家点数：", point1)
        print("=========\n= 0     =\n=   0   =\n=     0 =\n=========")
    elif point1 == 4:
        print("玩家点数：", point1)
        print("=========\n= 0   0 =\n=       =\n= 0   0 =\n=========")
    elif point1 == 5:
        print("玩家点数：", point1)
        print("=========\n= 0   0 =\n=   0   =\n= 0   0 =\n=========")
    else:
        print("玩家点数：", point1)
        print("=========\n= 0   0 =\n= 0   0 =\n= 0   0 =\n=========")

    if point1 > point:
        print("你胜")
    elif point1 < point:
        print("电脑胜")
    else:
        print("平局")


def 管理():
    qqq = str(input(' \n输入0退出\n \n输入1查看已有的账号密码:'))
    if qqq == '1':
        print(z_m)


def 密码():
    while True:
        aaa = str(input(' \n输入0退出\n \n请输入密码：'))
        if aaa == '123456':
            print(' \n成功！')
            管理()
        elif aaa == '0':
            主页面()
        else:
            print(' \n失败！')
            密码()


def 修改():
    global a4, a2, a5
    print(' \n按0退出')
    a2 = str(input(' \n账号：'))
    m3 = str(input(' \n密码：'))
    f2 = {a2: m3}
    g2 = set(z_m.items())
    h2 = set(f2.items())
    if h2.issubset(g2):
        print(' \n验证成功！')
        a4 = str(input(' \n重设密码:'))
        f1[a2] = a4
        z_m.update(f1)
        f1.clear()
        if a4:
            a5 = True
        else:
            a5 = False
    elif a2 == '0' == m3:
        print(' \n已退出！')
        登录()
    else:
        print(' \n验证失败！')
        修改()


def 登录():
    global z_m, d, c, i, a3, f1, a2, a4, a5

    while True:
        print(' \n1.注册账号(请在账号密码各输入1)\n \n2.修改密码(请在账号密码各输入2(请不要注册账号1：1))\n \n3.退出请扣3')
        a = str(input(' \n请输入账号：'))
        if a == '3':
            print(' \nbye bye,下次再见！')
            exit()
        b = str(input(' \n请输入密码：'))
        if a == b == '1':
            print(" \n注册")
            c = str(input(' \n新账号：'))
            d = str(input(' \n新密码：'))
            i = str(input(" \n请再输入一遍密码："))
            if c == d == i == '1':
                print(' \n对不起，您想卡的BUG已失效！')
                return 登录()
        if a == '2' == b:
            print(' \n修改密码')
            修改()
        else:
            a5 = False
        while True:
            if d == i:
                z_m[c] = d
                break
            elif d != i:
                print(" \n密码错误！")
                break
        f = {a: b}
        g = set(z_m.items())
        h = set(f.items())
        if h.issubset(g):
            print(' \n登录成功！')
            主页面()
        elif d != i:
            print(" \n请重新注册")
        elif a == b == '1':
            print(" \n注册成功！")
        elif a5 is True:
            print(' \n修改成功！')
        else:
            print(' \n登录失败！')


def 破译():
    a = int(input('(5位以内)请输入密码:'))
    while True:
        for item in range(0, 100000, 1):
            print(item)
            if item == a:
                break

        print("密码是:{}!".format(a))
        break


def 乘法():
    print('\n'.join([' '.join(['%s x %s = %-2s ' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 100)]))


def 开始():
    """

    :return: system 1.0.0
    """
    qqq = str(input('\n----system 1.0.0----\n\n    --按1进入--\n\n    --按2退出--\n\n----按3返回开始界面----\n//此版本为独立版本\n请输入:'))
    if qqq == '1':
        登录()
    elif qqq == '2':
        print(' \n程序已结束！')
        exit()
    elif qqq == '3':
        print('\n已返回!\n')
        start.start()
    else:
        print(' \n无效选择')
        开始()


def 主页面():
    j = str(
        input(
            '\n退出请按0\n \n重新登录请按1\n \n掷骰子请按2\n \n猜数字请按3\n \n解二元一次方程请按4\n \n破译密码请按5\n \n查看九九九九乘法表请按6\n \n进入管理员请按7\n '
            '\n返回开始请按8\n \n请输入：'))
    if j == '0':
        exit()
    elif j == '1':
        登录()
    elif j == '2':
        toss()
    elif j == '3':
        猜数字()
    elif j == '4':
        二元()
    elif j == '5':
        破译()
    elif j == '6':
        乘法()
    elif j == "7":
        密码()
    elif j == "8":
        开始()
    else:
        print(' \n无效选择!')
        主页面()


def system_1_0_0():
    开始()


if __name__ == '__main__':
    system_1_0_0()

# 1.0.0版本
