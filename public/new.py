# -*- coding: UTF-8 -*-


def a():
    pass


def new(f8):
    print('\n输入0退出')
    r = input(' \n输入版本末尾号(1~6,10,20)查看各版本更新内容\n\n请输入:')
    n101 = ('\n1.0.1更新内容'
            '\n本次更新了3个内容:'
            '\n1.更新了管理员的权限(修改密码权限)'
            '\n2.修改了以中文命名的函数(改为英文)'
            '\n3.削减了toss函数的格子占有')
    n102 = ('\n1.0.2更新内容'
            '\n本次更新了4个内容:'
            '\n1.添加了管理员功能（删除账号，添加账号）。'
            '\n2.添加一些小功能，以及修改了一些语言。'
            '\n3.修复一些bug。'
            '\n4.优化页面设置。')
    n103 = ('\n1.0.3更新内容'
            '\n本次更新了2个内容:'
            '\n1.更新了骰子'
            '\n2.修复了BUG')
    n104 = ('\n1.0.4更新内容'
            '\n本次更新了4个内容:'
            '\n1.修复了BUG。'
            '\n2.新增了管理员功能:清除数据。'
            '\n3.将文件分了类。'
            '\n4.可以查看更新内容。')
    n105 = ('\n1.0.5更新内容'
            '\n本次更新了9个内容'
            '\n1.修复了BUG。'
            '\n2.改善了页面。'
            '\n3.优化整体性能。'
            '\n4.减少文件整体大小。'
            '\n5.新增start以及返回start的功能。'
            '\n6.完善start功能。'
            '\n7.更新了exit功能。'
            '\n8.所有账号共享(即账号为版本通用，不再私有)([1.0.0]版本除外)。'
            '\n9.优化文件大小。')
    n106 = ('\n1.0.6更新内容'
            '\n注:本版本为system1.0系列的最后一个版本。'
            '\n本次更新了2个内容:'
            '\n1.优化页面。'
            '\n2.增加管理员清除数据功能的范围(所有数据数据)。')
    n110 = ('\n1.1.0更新内容:'
            '\n本次更新5了个内容'
            '\n1.新增聊天室功能(不完全)。'
            '\n2.修复了bug。'
            '\n3.更新了好友功能。'
            '\n4.优化管理员删除账号的操作。'
            '\n5.完整了添加路径的函数。')
    n120 = ('\n1.2.0更新内容:'
            '\n本次更新了3个内容'
            '\n1.所有信息可以永久储存,储存在public/users文件夹里。'
            '\n2.程序可以独立运行,无需配置。'
            '\n3.修复了已知问题。'
            '\n注意:此版本是system的最后一个版本,从此system不再更新。')
    if r == '0':
        print('\n已退出!')
        f8()
    elif r == '1':
        print(n101), new(a)
    elif r == '2':
        print(n102), new(a)
    elif r == '3':
        print(n103), new(a)
    elif r == '4':
        print(n104), new(a)
    elif r == '5':
        print(n105), new(a)
    elif r == '6':
        print(n106), new(a)
    elif r == '10':
        print(n110), new(a)
    elif r == '20':
        print(n120), new(a)
    else:
        print('\n该版本不存在!'), new(a)


if __name__ == '__main__':
    new(a)
