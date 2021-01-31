# -*- coding: UTF-8 -*-


def a():
    pass


def exit_2(n5):
    h2 = input('\n你确定要退出吗?\n\n继续退出请输入0,输入任意键取消:')
    if h2 == '0':
        print('\n程序已结束!')
        exit()
    else:
        print('\n已取消!')
        n5()


if __name__ == '__main__':
    exit_2(a)
