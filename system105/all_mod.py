# -*- coding: UTF-8 -*-
from random import randint
from system.system105 import system_1_0_5

f2020 = 0
b2020 = 0
c2020 = 0
e2020 = 0
d2020 = 0
a2020 = 0
x = 0
y = 0
n = 0
m = 0
q = 0
b5 = 0
b2 = {
    1456654456: 1456654456, 1231231323: 1456654456
}
c2 = [
    1456654456, 1231231323
]
global v1, point2, point3, a5e


def a():
    pass


def cheng_fa(f4):
    try:
        print('\n您希望看到几几乘法表?')
        x2 = int(input('\n第一个:'))
        y2 = int(input('\n第二个:'))
        print('\n'.join(
            [' '.join(['%s x %s = %-2s ' % (y2, x2, x2 * y2) for y2 in range(1, x2 + 1)]) for x2 in range(x2, y2 + 1)]))
        f4()
    except ValueError:
        print('\n输入错误!')
        cheng_fa(a)


def er_yuan(f3):
    global f2020, b2020, c2020, e2020, d2020, a2020, x, y
    try:
        a2020 = int(input('\na1='))
        b2020 = int(input('\nb1='))
        c2020 = int(input('\nc1='))
        d2020 = int(input('\na2='))
        e2020 = int(input('\nb2='))
        f2020 = int(input('\nc2='))
    except ZeroDivisionError:
        print('\n原方程无解!')
        f3()
    except ValueError:
        print('\n原方程无解!')
        f3()
    try:
        x = (f2020 * b2020 - c2020 * e2020) / (d2020 * b2020 - a2020 * e2020)
        y = (a2020 * f2020 - d2020 * c2020) / (e2020 * a2020 - b2020 * d2020)
    except ZeroDivisionError:
        print('\n原方程无解!')
        f3()
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
        print('\n错误!')
        cai_shu_zi()


def help2(f8):
    print("\n---欢迎进入help主界面!")
    print(
        '\n***退出请按0***\n\n***重新登录请按1***\n\n***掷骰子请按2***\n\n***猜数字请按3***\n\n***解二元一次方程组请按4***\n\n***测试电脑性能请按5***\n\n'
        '***查看乘法表请按6***\n\n***进入管理员请按7***\n\n***返回开始请按8***\n\n***查看更新内容请按9***')
    # print('')
    f8()


def po_yi(f5):
    global a5e
    print('\n电脑性能测试(输入0退出)')
    try:
        a5e = int(input('\n(5位以内)请输入:'))
    except NameError:
        print('\n错误!')
        po_yi(a)
    except ValueError:
        print('\n错误!')
        po_yi(a)
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
        po_yi(a)


def toss():
    global v1, point2, point3, m, n, q, b5
    y1 = 0
    point2 = 0
    point3 = 0
    try:
        v1 = int(input('\n输入0退出\n\n请输入您想骰的次数(最大100000):'))
    except ValueError or KeyboardInterrupt:
        print('\n无效选择!')
        toss()
    if v1 == 0:
        print('\n已退出!')
        system_1_0_5.zhu_ye_mian()
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
        n += 1
        print('\n你总共赢了{}局，电脑总共赢了{}局，打平了{}局，总共{}局'.format(n, m, q, n + m + q))
    elif point2 < point3:
        print('\n**********************电脑胜!**********************')
        m += 1
        print('\n你总共赢了{}局，电脑总共赢了{}局，打平了{}局，总共{}局'.format(n, m, q, n + m + q))
    else:
        print('\n**********************平局!**********************')
        q += 1
        print('\n你总共赢了{}局，电脑总共赢了{}局，打平了{}局，总共{}局'.format(n, m, q, n + m + q))
    if n > m:
        b5 = '你'
    elif n < m:
        b5 = '电脑'
    elif n == m:
        b5 = '没人'
    print('\n**********当前{}领先**********'.format(b5))
    toss()


def f(a0):
    """

    :param a0:dict
    :return: 账号&密码
    """
    n7 = 1
    print('\n======================================')
    for i, t in a0.items():
        print('= NO.{} 账号：{} 密码：{}'.format(n, i, t))
        n7 += 1
    print('======================================')


def f2(yz):
    """

    :param yz:list
    :return: 账号
    """
    n2 = 1
    print('\n=======================')
    for i2 in yz:
        print('= No.{} 账号:{} ='.format(n2, i2))
        n2 += 1
    print('=======================')


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
        elif n5 == '6':
            f(b2)
        elif n5 == '7':
            f2(c2)
        else:
            test()


    test()
