# -*- coding: UTF-8 -*-
import start
from public import variables

a21 = variables.a21  # 临时储存
b = variables.b  # 密码
c2c2 = variables.c2c2  # 管理员初始密码&重设密码
a4 = variables.a4  # 临时储存
z = variables.z  # 储存账号
f1 = variables.f1  # 临时储存
z_m = variables.z_m  # 储存账号密码
al3 = variables.al3  # 管理员账号&密码
global d1, a


def zhang_hao_chang_du():
    qq3 = len(z)
    print('\n----当前共有{}个账号----'.format(qq3))


def er_yuan():
    a1 = eval(input('a1='))
    b1 = eval(input('b1='))
    c1 = eval(input('c1='))
    a25 = eval(input('a2='))
    b2 = eval(input('b2='))
    c2 = eval(input('c2='))

    x = (c2 * b1 - c1 * b2) / (a25 * b1 - a1 * b2)
    y = (a1 * c2 - a25 * c1) / (b2 * a1 - b1 * a25)
    print('x=', x)
    print('y=', y)


def cai_shu_zi():
    import random
    a1000 = random.randint(0, 200)
    while True:
        b1000 = int(input("按0退出\n猜一个0~200之间的数字:"))
        if b1000 == 0:
            break
        elif b1000 > a1000:
            print("这个数字太大了")
        elif b1000 < a1000:
            print("这个数字太小了")
        else:
            print("恭喜，你猜对了，这个数字是:{}!".format(a))
            break


def toss():
    import random
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


def guan_li():
    while True:
        qqq = str(input('\n输入0退出\n\n输入1查看已有的账号密码\n\n输入2查看已有的账号\n\n输入3查看已有的账号个数\n\n请输入:'))
        if qqq == '1':
            print('\n当前有账号密码:', z_m)
        elif qqq == '2':
            print('\n当前有账号:\n')
            for c1c1 in z:
                print(c1c1)
        elif qqq == '3':
            zhang_hao_chang_du()
        elif qqq == '4':
            pass
        elif qqq == '5':
            pass
        elif qqq == '0':
            mi_ma()
        else:
            print('\n无效选择！')


def mi_ma():
    global al3
    if al3:
        print('\n----欢迎进入管理系统!----')
        ccc2: str = str(input('\n输入0退出\n\n输入1改密码\n\n请输入密码：'))
        aaa = {'admin': ccc2}
        if aaa == al3:
            print(' \n密码验证成功!\n\n成功进入管理系统\n\n\n----欢迎进入管理系统!----')
            guan_li()
        elif ccc2 == '0':
            zhu_ye_mian()
        elif ccc2 == '1':
            yan_zheng_2()
        else:
            print('\n验证失败！')
            mi_ma()
    else:
        print('\n请设置您的初始密码')
        chu_shi()


def yan_zheng_2():
    z8 = str(input('\n----修改密码----\n\n密码验证:'))
    if c2c2[0] == z8:
        print('\n验证成功!')
        gai_mi_ma()
    elif c2c2[0] != z8:
        print('\n验证失败!')
        mi_ma()
    else:
        print('\n无效选择!')
        yan_zheng_2()


def gai_mi_ma():
    c3c3 = str(input('\n退出请按0\n\n重设密码：'))
    if c3c3 == '0':
        print('\n已退出!')
        mi_ma()
    elif len(c3c3) < 4:
        print('\n密码长度不得小于4位')
        gai_mi_ma()
    ao2 = {'admin': c3c3}
    al3.update(ao2)
    global c2c2
    c2c2.append(c3c3)
    print('\n重设成功!')
    mi_ma()


def chu_shi():
    c3c3 = str(input('\n初始密码设置:'))
    if len(c3c3) < 4:
        print('\n密码的长度不得小于4位')
        chu_shi()
    ao2 = {'admin': c3c3}
    al3.update(ao2)
    global c2c2
    c2c2.clear()
    c2c2.append(c3c3)
    print('\n设置成功!')
    mi_ma()


def mi_ma_pan_duan_1():
    global b
    b = str(input(' \n请输入密码(按0退出)：'))
    d3: int = len(b)
    if b == '0':
        print('\n已退出!')
        xuan_ze()
    if d3 < 8:
        print(' \n请输入大于8位的密码！')
        mi_ma_pan_duan_1()


def yan_zhen_1():
    global b
    mi_ma_pan_duan_1()
    c = str(input(' \n请再次输入密码：'))
    if b != c:
        print(' \n密码不相同！')
        yan_zhen_1()
    else:
        print('\n注册成功！')


def xin_jian_1():
    global a, z, a21
    import random
    a21 = '1' + str(random.randint(100000000, 999999999))
    if a21 in z:
        xin_jian_1()
    print(' \n你的账号是：' + a21)


def chu_cun_1():
    global z_m, b, z
    z_m[a21] = b  # 账号密码储存
    z.append(a21)  # 账号储存
    variables.msg[a21] = []  # 个人信息储存
    variables.all_friend[a21] = []  # 个人好友储存


def deng_lu_2():
    global d1, z
    print(' \n登录')
    i1 = str(input(' \n请输入账号(按0退出)：'))
    if i1 == '0':
        xuan_ze()
    i2 = str(input(' \n请输入密码：'))
    d1 = dict()
    if i1 == '  visitor ':
        print(' \n登录失败！')
        deng_lu_2()
    d1[i1] = i2
    g2 = set(z_m.items())
    h2 = set(d1.items())
    if h2.issubset(g2):
        print(' \n登录成功！')
        d1.clear()
        zhu_ye_mian()
    else:
        print(' \n登录失败！')
        deng_lu_2()


def zhu_ce_2():
    xin_jian_1()
    yan_zhen_1()
    chu_cun_1()
    xuan_ze()


def xuan_ze():
    global z_m
    print('\n欢迎进入登录系统!')
    print(' \n----按1登录----\n \n----按2注册----\n \n----按3改密----')
    i3 = str(input(' \n请输入：'))
    if i3 == '1':
        deng_lu_2()
    elif i3 == '2':
        zhu_ce_2()
    elif i3 == '3':
        xiu_gai_2()  # 改密2
    else:
        print(' \n无效选择！')
        xuan_ze()


def chong():
    global a4
    a4 = str(input(' \n重设密码:'))
    if len(a4) < 8:
        print(' \n请输入大于八位的密码！')
        chong()


def xiu_gai_2():
    global a4
    a103: str = str(input(' \n账号(按0退出)：'))
    if a103 == '0':
        print(' \n已退出！')
        xuan_ze()
    a3 = str(input(' \n密码：'))
    f2 = {a103: a3}
    g2 = set(z_m.items())
    h2 = set(f2.items())
    if h2.issubset(g2):
        print(' \n验证成功！')
        chong()
        f1[a103] = a4
        z_m.update(f1)
        f1.clear()
        print(' \n重设成功！')
        xuan_ze()
    else:
        print(' \n验证失败！')
        xiu_gai_2()


def po_yi():
    a5e: int = int(input(' \n(5位以内)请输入密码:'))
    while True:
        for item in range(0, 100000, 1):
            print(item)
            if item == a5e:
                break

        print(" \n密码是:{}!".format(a5e))
        break


def cheng_fa():
    print('\n'.join([' '.join(['%s x %s = %-2s ' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 100)]))


def kai_shi():
    """

    :return: system 1.0.1
    """
    qqq = str(input('\n----system 1.0.1----\n\n    --按1进入--\n\n    --按2退出--\n\n----按3返回开始界面----\n\n请输入:'))
    if qqq == '1':
        xuan_ze()
    elif qqq == '2':
        print('\n程序已结束!')
        exit()
    elif qqq == '3':
        print('\n已返回!\n')
        start.start()
    else:
        print('\n无效选择!')
        kai_shi()


def help2():
    print("\n欢迎进入help主界面!")
    print(
        '\n退出请按0\n\n重新登录请按1\n\n掷骰子请按2\n\n猜数字请按3\n\n解二元一次方程请按4\n\n破译密码请按5\n\n查看九九九九乘法表请按6\n\n进入管理员请按7\n\n返回开始请按8')
    # print('')
    zhu_ye_mian()


def zhu_ye_mian():
    while True:
        j = str(input(
            '  \n(输入help以查看帮助)请输入：'))
        if j == '0':
            exit()
        elif j == '1':
            xuan_ze()
        elif j == '2':
            toss()
        elif j == '3':
            cai_shu_zi()
        elif j == '4':
            er_yuan()
        elif j == '5':
            po_yi()
        elif j == '6':
            cheng_fa()
        elif j == "7":
            mi_ma()
        elif j == "8":
            kai_shi()
        elif j == "help":
            help2()
        else:
            print(' \n无效选择!')


def system_1_0_1():
    kai_shi()


if __name__ == '__main__':
    system_1_0_1()

# 1.0.1版本最新版
# 更新了管理员的权限（修改密码权限）
# 修改了以中文命名的函数（改为英文）
# 削减了toss函数的格子占有
