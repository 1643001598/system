# -*- coding: UTF-8 -*-
from __init__ import *
from public import read_write_file
import start
from public import new
from public import variables
from public.exit_2 import exit_2
import random
a21 = variables.a21  # 临时储存
b = variables.b  # 密码
c2c2 = variables.c2c2  # 管理员初始密码&重设密码
a4 = variables.a4  # 临时储存
z = variables.z  # 储存账号
f1 = variables.f1  # 临时储存
z_m = variables.z_m  # 储存账号密码
al3 = variables.al3  # 管理员账号&密码
r = 4
global d1, v1, point2, point3, f2020, b2020, c2020, e2020, d2020, a2020, q0q0, a321, b256


def zhang_hao_chang_du():
    qq3 = len(z)
    print('\n----当前共有{}个账号----'.format(qq3))


def guan_li():
    while True:
        qqq = '\n输入0退出\n\n输入1查看已有的账号密码\n\n输入2查看已有的账号\n\n输入3查看已有的账号个数\n\n输入4删除账号\n\n输入5添加账号\n\n输入6清空所有数据'
        a45 = input('\n(输入h查看帮助)请输入:')
        if a45 == '1':
            if not z_m:
                print('\n*****当前没有账号注册!*****')
                guan_li()
            print('\n当前有:')
            f(z_m)
        elif a45 == '2':
            if not z:
                print('\n*****当前没有账号注册!*****')
                guan_li()
            print('\n当前有账号:')
            f2(z)
            # for c1c1 in l:
            #     print(c1c1)  # 账号
        elif a45 == '3':
            zhang_hao_chang_du()  # 账号个数
        elif a45 == '4':
            print('\n欢迎进入账号删除页面!')
            shan_chu()  # 删除页面
        elif a45 == '5':
            print('\n欢迎进入添加系统!\n\n输入r以查看规则')
            tian_jia()  # 添加主页面
        elif a45 == '6':
            print('\n清空数据,请谨慎操作!')
            delete_2()
        elif a45 == '0':
            control()
        elif a45 == 'h':
            print(qqq)
        else:
            print('\n无效选择！')


def delete_2():
    """管理系统清空用户信息分模块"""

    def d(*args):
        for i in args:
            i.clear()

    global a321, b256, r
    try:
        b256 = random.randint(1, 9)
        a321 = int(input('\n你确定要清空所有数据吗？(输入0退出,继续请按:{},剩余机会:{}):'.format(b256, r + 1)))
    except ValueError:
        print('\n错误!')
        delete_2()
    if a321 == 0:
        print('\n已退出!')
        guan_li()
    elif r == 0:
        d(z_m, z, f1, al3, c2c2, variables.msg, variables.a_m, variables.n_s, variables.all_friend, variables.s56)
        variables.z.append('  visitor ')
        variables.z_m['  visitor '] = None
        variables.all_friend['  visitor '] = []
        variables.msg['  visitor '] = []
        read_write_file.write_file(
            variables.uan, z)
        read_write_file.write_file(
            variables.uanp, z_m)
        read_write_file.write_file(
            variables.aanp, al3)
        read_write_file.write_file(
            variables.am, variables.a_m)
        read_write_file.write_file(
            variables.uf, variables.all_friend)
        read_write_file.write_file(
            variables.um, variables.msg)
        print('\n******************************删除成功!******************************')
        start.start()
    elif a321 == b256:
        r -= 1
        delete_2()
    else:
        print('\n条件错误!')
        r -= 0
        delete_2()


def tian_jia():
    pq = '\n添加规则如下:\n\n1.只可以添加以"1"开头的10位数字\n\n2.密码长度不得小于8位,大于16位\n\n3.输入0退出'
    m1 = input('\n请输入新账号:')
    if m1 in z:
        print('\n账号重复!')
        tian_jia()
    elif m1 == 'r':
        print(pq)
        tian_jia()
    elif m1 == '0':
        guan_li()
    elif len(m1) == 10:
        if m1.find('1') != 0:
            print('\n未以"1"开头!')
            tian_jia()
    else:
        print('\n账号不符合要求!')
        tian_jia()
    m2 = input('\n请输入新密码:')
    if 8 <= len(m2) <= 16:
        pass
    else:
        print('\n密码长度出错!(密码只可为8~16位)')
        tian_jia()
    q2 = {m1: m2}
    z_m.update(q2)
    z.append(m1)
    q2.clear()
    print('\n添加成功!')
    tian_jia()


def shan_chu():
    global z_m
    m5 = input('\n输入0退出\n\n输入1以查看账号密码\n\n请输入您想要删除的账号:')
    if m5 == '0':
        print('\n已退出!')
        guan_li()
    elif m5 == '1':
        if z:
            print('\n当前有:')
            f(z_m)
            shan_chu()
        else:
            print('\n当前没有账号!')
            shan_chu()
    elif len(m5) != 10:
        print('\n无效数据!')
        shan_chu()
    try:
        c24 = input('\n是(0)否(1)删除:')
        if c24 == '1':
            print('\n已取消删除!')
            shan_chu()
        elif c24 == '0':
            del z_m[m5]
            z.remove(m5)
            print('\n删除成功!')
            shan_chu()
        else:
            print('\n无效选择!')
            shan_chu()
    except KeyError:
        print('\n该账号不存在!')
        shan_chu()


def control():
    global al3
    if al3:
        print('\n----欢迎进入管理系统!----')
        ccc2 = input('\n输入0退出\n\n输入1改密码\n\n请输入密码：')
        aaa = {'admin': ccc2}
        if aaa == al3:
            print(' \n密码验证成功!\n\n成功进入管理系统\n\n\n\n\n\n\n\n\n----欢迎进入管理系统!----')
            guan_li()  # 管理系统
        elif ccc2 == '0':
            zhu_ye_mian()
        elif ccc2 == '1':
            yan_zheng_2()
        else:
            print('\n验证失败！')
            control()
    else:
        print('\n--欢迎加入管理系统!--\n\n请设置您的初始密码:')
        chu_shi()


def yan_zheng_2():
    z1 = input('\n----修改密码----\n\n----输入0退出----\n\n密码验证:')
    if z1 == '0':
        print('\n已退出!')
        control()
    elif c2c2[0] == z1:
        print('\n验证成功!')
        gai_mi_ma()
    elif c2c2[0] != z1:
        print('\n验证失败!')
        yan_zheng_2()
    else:
        print('\n无效选择!')
        yan_zheng_2()


def gai_mi_ma():
    c3c3 = input('\n退出请按0\n\n重设密码：')
    if c3c3 == '0':
        print('\n已退出!')
        control()
    elif len(c3c3) < 4:
        print('\n密码长度不得小于4位')
        gai_mi_ma()
    ao2 = {'admin': c3c3}
    al3.update(ao2)
    global c2c2
    c2c2.clear()
    c2c2.append(c3c3)
    print('\n重设成功!')
    control()


def chu_shi():
    c3c3 = input('\n初始密码设置:')
    if len(c3c3) < 4:
        print('\n密码的长度不得小于4位')
        chu_shi()
    ao2 = {'admin': c3c3}
    global c2c2
    c2c2.append(c3c3)
    al3.update(ao2)
    ao2.clear()
    print('\n设置成功!')
    control()


def mi_ma_pan_duan_1():
    global b
    b = input(' \n请输入密码(按0退出)：')
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
    c = input(' \n请再次输入密码：')
    if b != c:
        print(' \n密码不相同！')
        yan_zhen_1()
    else:
        print('\n注册成功！')


def xin_jian_1():
    global z, a21
    a21 = '1' + str(randint(100000000, 999999999))
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
    i1 = input(' \n请输入账号(按0退出)：')
    if i1 == '0':
        xuan_ze()
    if i1 == '  visitor ':
        print(' \n登录失败！')
        deng_lu_2()
    i2 = input(' \n请输入密码：')
    d1 = dict()
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
    global z_m, q0q0
    print('\n欢迎进入登录系统!')
    print('\n---按0退出程序---\n\n----按1登录----\n\n----按2注册----\n\n----按3改密----\n\n---按4游客登录---\n\n---按5返回开始---')
    i3 = input(' \n请输入：')
    if i3 == '0':
        exit_2(xuan_ze)
    elif i3 == '1':
        deng_lu_2()
    elif i3 == '2':
        zhu_ce_2()
    elif i3 == '3':
        xiu_gai_2()  # 改密2
    elif i3 == '4':
        print('\n***************游客模式***************')
        q0q0 = False
        zhu_ye_mian()
    elif i3 == '5':
        kai_shi()
    else:
        print(' \n无效选择！')
        xuan_ze()


def chong():
    global a4
    a4 = input(' \n重设密码:')
    if len(a4) < 8:
        print(' \n请输入大于八位的密码！')
        chong()


def xiu_gai_2():
    global a4
    a103 = input(' \n账号(按0退出)：')
    if a103 == '0':
        print(' \n已退出！')
        xuan_ze()
    a3 = input(' \n密码：')
    qt5 = {a103: a3}
    g2 = set(z_m.items())
    h2 = set(qt5.items())
    if h2.issubset(g2):
        print(' \n验证成功！')
        chong()
        f1[a103] = a4
        z_m.update(f1)
        f1.clear()
        print('\n重设成功！')
        xuan_ze()
    else:
        print('\n验证失败！')
        xiu_gai_2()


def kai_shi():
    """

    :return:system106
    """
    # print(b, 'b\n', e, 'e\n', a4, 'a4\n', a24, 'a24\n', l, 'l\n', f1, 'f1\n', c3c3, 'c3c3\n', ao3, 'ao3\n', d, 'd\n')
    qqq = input('=====================\n'
                '=   system 1.0.6    =\n'
                '=                   =\n'
                '=    输 入 1 进 入    =\n'
                '=    输 入 2 退 出    =\n'
                '=    输 入 3 返 回    =\n'
                '=     开 始 界 面     =\n'
                '======================\n'
                '请  输  入:')
    if qqq == '1':
        xuan_ze()
    elif qqq == '2':
        exit_2(kai_shi)
    elif qqq == '3':
        print('\n已返回!\n')
        start.start()
    else:
        print('\n无效选择!')
        kai_shi()


def zhu_ye_mian():
    while True:
        j = input('\n(输入h以查看帮助)请输入：')
        if j == '0':
            exit_2(zhu_ye_mian)
        elif j == '1':
            xuan_ze()
        elif j == '2':
            toss()
        elif j == '3':
            cai_shu_zi()
        elif j == '4':
            er_yuan(zhu_ye_mian)
        elif j == '5':
            po_yi(zhu_ye_mian)
        elif j == '6':
            cheng_fa(zhu_ye_mian)
        elif j == "7":
            control()
        elif j == "8":
            kai_shi()
        elif j == '9':
            new(zhu_ye_mian)
        # elif j == '10': print( 'a24{}\nb{}\nc3c3{}\na4{}\nz{}\nf1{}\nz_m{}\nal3{}\nm{}\nn{}\nq{}'.format(a21, b,
        # c3c3, a4, z, f1, z_m, al3, m, n, q))
        elif j == "h":
            help2(zhu_ye_mian)
        else:
            print(' \n无效选择!')


def system_1_0_6():
    """
    使用system\n
    :return: system 1.0.6
    """
    kai_shi()


if __name__ == '__main__':
    system_1_0_6()
