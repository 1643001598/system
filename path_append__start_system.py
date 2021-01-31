# -*- coding: UTF-8 -*-
import sys
from public import variables, read_write_file
import start


def synchronizing_information():
    all_message = read_write_file.my_read_list(
        variables.am)
    user_account_number = read_write_file.my_read_list(
        variables.uan)
    user_account_number_password = read_write_file.my_read_dict(variables.uanp)
    user_message = read_write_file.my_read_dict(
        variables.um)
    user_friend = read_write_file.my_read_dict(
        variables.uf)
    administrator_account_number_password = read_write_file.my_read_dict(
        variables.aanp
    )
    c2c21 = read_write_file.my_read_list(variables.mp + 'c2c2.txt')
    # print(user_account_number, user_account_number_password, all_message)
    variables.a_m[:] = all_message
    variables.z[:] = user_account_number
    variables.z_m.update(user_account_number_password)
    variables.msg.update(user_message)
    variables.all_friend.update(user_friend)
    variables.al3.update(administrator_account_number_password)
    variables.c2c2[:] = c2c21


def s():
    sys.setrecursionlimit(1000000)
    synchronizing_information()
    start.start()


if __name__ == '__main__':
    print('\n欢迎进入system,创始人:wrh,净大小:166530 字节.')
    print('创作不易,请多支持!\n\n')
    s()
