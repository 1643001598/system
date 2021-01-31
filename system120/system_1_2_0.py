# -*- coding: UTF-8 -*-
"""this is system_1_2_0,the newest version"""
from public import read_write_file
import start
from public import new
from system120 import all_mod
from public import items_delete, variables
from public.exit_2 import exit_2
from chat import index
import random

a21 = variables.a21  # 临时储存
b = variables.b  # 密码
c2c2 = variables.c2c2  # 管理员初始密码&重设密码
a4 = variables.a4  # 临时储存
z = variables.z  # 储存账号
f1 = variables.f1  # 临时储存
z_m = variables.z_m  # 储存账号密码
al3 = variables.al3  # 管理员账号&密码
n_z = variables.n_z  # 在线的账号
r = 4
global d1, v1, point2, point3, f2020, b2020, c2020, e2020, d2020, a2020, q0q0, a321, b256

# ==============================================
"""管理系统板块"""


def control():
    """管理系统主页面主模块"""
    global al3
    if al3:
        print('\n----欢迎进入管理系统!----')
        ccc2 = input('\n输入0退出\n\n输入1改密码\n\n请输入密码：')
        aaa = {'admin': ccc2}
        if aaa == al3:
            print('\n 密码验证成功!\n\n成功进入管理系统\n\n  -欢迎进入-\n\n  -管理系统-\n\n   -主页面-\n')
            control_1()  # 管理系统
        elif ccc2 == '0':
            print('\n已退出!')
            main_page()
        elif ccc2 == '1':
            verification()
        else:
            print('\n验证失败！')
            control()
    else:
        print('\n--欢迎加入管理系统!--\n\n请设置您的初始密码:')
        initial()


def control_1():
    """管理员控制页面主模块"""
    while True:
        qqq = '\n输入0退出\n\n输入1查看已有的账号密码\n\n输入2查看已有的账号\n\n输入3查看已有的账号个数\n\n输入4删除账号\n\n输入5添加账号\n\n输入6清空所有数据'
        a45 = input('\n(输入h查看帮助)请输入:')
        if a45 == '1':
            if not z_m:
                print('\n*****当前没有账号注册!*****')
                control_1()
            print('\n当前有:')
            all_mod.f(z_m)
        elif a45 == '2':
            if not z:
                print('\n*****当前没有账号注册!*****')
                control_1()
            print('\n当前有账号:')
            all_mod.f2(z)
            # for c1c1 in l:
            #     print(c1c1)  # 账号
        elif a45 == '3':
            zhang_hao_chang_du()  # 账号个数
        elif a45 == '4':
            print('\n欢迎进入账号删除页面!')
            delete()  # 删除页面
        elif a45 == '5':
            print('\n欢迎进入添加系统!\n\n输入r以查看规则')
            add()  # 添加主页面
        elif a45 == '6':
            print('\n清空数据,请谨慎操作!')
            delete_2()
        elif a45 == '0':
            control()
        elif a45 == 'h':
            print(qqq)
        else:
            print('\n无效选择！')


def zhang_hao_chang_du():
    """管理员查看账号长度模块"""
    qq3 = len(z)
    print('\n----当前共有{}个账号----'.format(qq3))


def delete():
    """管理员删除用户分模块"""
    m5 = input('\n输入0退出\n\n输入-1以查看账号\n\n请输入您想要删除的账号序号:')
    if m5 == '0':
        print('\n已退出!')
        control_1()
    elif m5 == '-1':
        if z:
            print('\n当前有:')
            all_mod.f2(z_m)
            delete()
        else:
            print('\n当前没有账号!')
            delete()
    if m5 == '1':
        print('\n无法删除游客账号!')
        delete()
    for i2 in enumerate(z_m):
        if i2[0] == int(m5) - 1:
            try:
                c24 = input('\n是(0)否(1)删除:')
                if c24 == '1':
                    print('\n已取消删除!')
                    delete()
                elif c24 == '0':
                    items_delete.items_delete(z_m, int(m5) - 1)
                    items_delete.items_delete(variables.msg, int(m5) - 1)
                    items_delete.items_delete(variables.all_friend, int(m5) - 1)
                    z.pop(int(m5) - 1)
                    print('\n删除成功!')
                    read_write_file.write_file(
                        variables.uan, z)
                    read_write_file.write_file(
                        variables.uanp, z_m)
                    delete()
                else:
                    print('\n无效选择!')
                    delete()
            except KeyError:
                print('\n该账号不存在!')
                delete()


def add():
    """管理系统添加用户分模块"""
    pq = '\n添加规则如下:\n\n1.只可以添加以"1"开头的10位数字\n\n2.密码长度不得小于8位,大于16位\n\n3.输入0退出'
    m1 = input('\n请输入新账号:')
    if m1 in z:
        print('\n账号重复!')
        add()
    elif m1 == 'r':
        print(pq)
        add()
    elif m1 == '0':
        control_1()
    elif len(m1) == 10:
        if m1.find('1') != 0:
            print('\n未以"1"开头!')
            add()
    else:
        print('\n账号不符合要求!')
        add()
    m2 = input('\n请输入新密码:')
    if 8 <= len(m2) <= 16:
        pass
    else:
        print('\n密码长度出错!(密码只可为8~16位)')
        add()
    q2 = {m1: m2}
    z_m.update(q2)
    z.append(m1)
    variables.msg[m1] = []  # 个人信息储存
    variables.all_friend[m1] = []  # 个人好友储存
    read_write_file.write_file(
        variables.uan, z)
    read_write_file.write_file(
        variables.uanp, z_m)
    read_write_file.write_file(
        variables.uf, variables.all_friend)
    read_write_file.write_file(
        variables.um, variables.msg)
    q2.clear()
    print('\n添加成功!')
    add()


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
        control_1()
    elif r == 0:
        d(z_m, z, f1, al3, n_z, c2c2, variables.msg, variables.a_m, variables.n_s, variables.all_friend, variables.s56)
        variables.z.append('  visitor ')
        variables.z_m['  visitor '] = None
        variables.all_friend['  visitor '] = []
        variables.msg['  visitor '] = []
        read_write_file.write_file(
            variables.mp + 'c2c2.txt', c2c2)
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


def initial():
    """管理员初始密码设置分模块"""
    global c2c2
    c3c3 = input('\n初始密码设置:')
    if len(c3c3) < 4:
        print('\n密码的长度不得小于4位')
        initial()
    ao2 = {'admin': c3c3}
    c2c2.append(c3c3)
    al3.update(ao2)
    read_write_file.write_file(variables.aanp, ao2)
    read_write_file.write_file(variables.mp + 'c2c2.txt', c2c2)
    print('\n设置成功!')
    control()


def verification():
    """管理员重设密码分模块"""
    z1 = input('\n----修改密码----\n\n----输入0退出----\n\n密码验证:')
    if z1 == '0':
        print('\n已退出!')
        control()
    elif c2c2[0] == z1:
        print('\n验证成功!')
        fix_password()
    elif c2c2[0] != z1:
        print('\n验证失败!')
        verification()
    else:
        print('\n无效选择!')
        verification()


def fix_password():
    """管理员重设密码分上分模块"""
    global c2c2
    c3c3 = input('\n退出请按0\n\n重设密码：')
    if c3c3 == '0':
        print('\n已退出!')
        control()
    elif len(c3c3) < 4:
        print('\n密码长度不得小于4位')
        fix_password()
    ao2 = {'admin': c3c3}
    al3.update(ao2)
    ao2.clear()
    c2c2.clear()
    c2c2.append(c3c3)
    print('\n重设成功!')
    al3.update(ao2)
    read_write_file.write_file(variables.uanp, ao2)
    read_write_file.write_file(variables.mp + 'c2c2.txt', c2c2)
    control()


# ==============================================

# ==============================================
"""用户登录版块"""


def log_in():
    """用户登录分模块"""
    global d1, z
    print(' \n登录')
    i1 = input(' \n请输入账号(按0退出)：')
    if i1 == '0':
        choose()
    i2 = input(' \n请输入密码：')
    if i1 == '  visitor ':
        print(' \n登录失败！')
        log_in()
    g2 = set(z_m.items())
    h2 = set({i1: i2}.items())
    if h2.issubset(g2):
        print(' \n登录成功！')
        n_z.clear()
        n_z.append(i1)
        g2.clear()
        h2.clear()
        main_page()
    else:
        print(' \n登录失败！')
        log_in()


# ==============================================

# ==============================================
"""用户注册版块"""


def register():
    """用户登录部分的注册模块"""
    new_1()
    check()
    lay_in()
    choose()


def new_1():
    """用户登录部分的注册分模块"""
    global z, a21
    a21 = '1' + str(random.randint(100000000, 999999999))
    if a21 in z:
        new_1()
    print(' \n你的账号是：' + a21)


def check():
    """用户登录部分的注册分模块"""
    global b
    check_password()
    c = input(' \n请再次输入密码：')
    if b != c:
        print(' \n密码不相同！')
        check()
    else:
        print('\n注册成功！')


def check_password():
    """用户登录部分的注册分模块"""
    global b
    b = input(' \n请输入密码(按0退出)：')
    d3: int = len(b)
    if b == '0':
        print('\n已退出!')
        choose()
    if d3 < 8:
        print(' \n请输入大于8位的密码！')
        check_password()


def lay_in():
    """用户登录部分的注册分模块"""
    z.append(a21)  # 账号储存
    z_m[a21] = b  # 账号密码储存
    variables.msg[a21] = []  # 个人信息储存
    variables.all_friend[a21] = []  # 个人好友储存
    read_write_file.write_file(
        variables.uan, z)
    read_write_file.write_file(
        variables.uanp, z_m)
    read_write_file.write_file(
        variables.uf, variables.all_friend)
    read_write_file.write_file(
        variables.um, variables.msg)


# ==============================================

# ==============================================
"""用户修改密码版块"""


def fix_2():
    """用户登录部分的修改密码分模块"""
    global a4
    a103 = input(' \n账号(按0退出)：')
    if a103 == '0':
        print(' \n已退出！')
        choose()
    a3 = input(' \n密码：')
    qt5 = {a103: a3}
    g2 = set(z_m.items())
    h2 = set(qt5.items())
    if h2.issubset(g2):
        print(' \n验证成功！')
        reset_password()
        f1[a103] = a4
        z_m.update(f1)
        f1.clear()
        print('\n重设成功！')
        read_write_file.write_file(
            variables.uanp, z_m)
        choose()
    else:
        print('\n验证失败！')
        fix_2()


def reset_password():
    """用户登录部分的修改密码分上分模块"""
    global a4
    a4 = input(' \n重设密码:')
    if len(a4) < 8:
        print(' \n请输入大于八位的密码！')
        reset_password()


# ==============================================

# ==============================================
"""系统主模块"""


def system_1_2_0():
    """
    使用system\n
    :return: system 1.2.0
    """
    start_1()


def start_1():
    """
    system主页面主模块
    开始使用system
    :return:system120
    """
    # print(b, 'b\n', e, 'e\n', a4, 'a4\n', a24, 'a24\n', l, 'l\n', f1, 'f1\n', c3c3, 'c3c3\n', ao3, 'ao3\n', d, 'd\n')
    qqq = input('=====================\n'
                '=   system 1.2.0    =\n'
                '=                   =\n'
                '=    输 入 1 进 入    =\n'
                '=    输 入 2 退 出    =\n'
                '=    输 入 3 返 回    =\n'
                '=     开 始 界 面     =\n'
                '======================\n'
                '请  输  入:')
    if qqq == '1':
        choose()
    elif qqq == '2':
        exit_2(start_1)
    elif qqq == '3':
        print('\n已返回!\n')
        start.start()
    else:
        print('\n无效选择!')
        start_1()


def choose():
    """用户登录部分的登录注册修改密码主页面主模块"""
    global z_m
    print('\n欢迎进入登录系统!')
    print('\n---按0退出程序---\n\n----按1登录----\n\n----按2注册----\n\n----按3改密----\n\n---按4游客登录---\n\n---按5返回开始---')
    i3 = input(' \n请输入：')
    if i3 == '0':
        exit_2(choose)
    elif i3 == '1':
        log_in()
    elif i3 == '2':
        register()
    elif i3 == '3':
        fix_2()  # 改密
    elif i3 == '4':
        print('\n***************游客模式***************')
        n_z.clear()
        n_z.append('  visitor ')
        main_page()
    elif i3 == '5':
        start_1()
    else:
        print(' \n无效选择！')
        choose()


def main_page():
    """系统主页面主模块"""
    if n_z[0] not in z:
        print('\n您登录的账号不存在!')
        log_in()
    while True:
        j = input('\n当前你正在使用账号:{}\n\n(输入h以查看帮助)请输入:'.format(n_z[0]))
        if j == '0':
            exit_2(main_page)
        elif j == '1':
            n_z.clear()
            choose()
        elif j == '2':
            all_mod.toss()
        elif j == '3':
            all_mod.cai_shu_zi()
        elif j == '4':
            all_mod.er_yuan(main_page)
        elif j == '5':
            all_mod.po_yi(main_page)
        elif j == '6':
            all_mod.cheng_fa(main_page)
        elif j == "7":
            control()
        elif j == "8":
            n_z.clear()
            start_1()
        elif j == '9':
            new.new(main_page)
        elif j == '10':
            print(globals())
        elif j == 'c':
            variables.n_s.append(120)
            index.chatroom_helper()
        elif j == "h":
            all_mod.help2(main_page)
        else:
            print(' \n无效选择!')


# ==============================================

if __name__ == '__main__':
    system_1_2_0()
