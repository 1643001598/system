# encoding: GBK
from chat import chat
from public import variables
from system110 import system_1_1_0
from system120 import system_1_2_0
from chat import friend
n_z = variables.n_z


def judge():
    if variables.n_s[0] == 110:
        system_1_1_0.main_page()
    elif variables.n_s[0] == 120:
        system_1_2_0.main_page()


def chatroom_helper():
    h1 = input(
        '\n\n---------------------------------------------------------------------------------------------------------'
        '--------\n                                              聊天室帮助界面                                         您有{}份信'
        '息未读\n帮助：1.输入0查看未读信息(未开放)                                                              '
        '  ====\n     2.输入1进'
        '入聊天室主界面                                                                ====      ====\n     3.输入2查看个人信'
        '息(未开放)        '
        '                                                ====  {}  ====\n     4.输入3进入好友界面                        '
        '          '
        '                                 ====      ====\n     5.输入4返回system主页面                                      '
        '         '
        '                     ====\n-----------------------------------------------------------------------------------'
        '------------------------------\n请输入:'.format(0, n_z[0]))
    if h1 == '0':
        print('\n无效选择!')
        chatroom_helper()
        pass
    elif h1 == '1':
        variables.if_on = True
        chat.chat()
    elif h1 == '2':
        print('\n无效选择!')
        chatroom_helper()
        pass
    elif h1 == '3':
        if n_z[0] == '  visitor ':
            print('\n检测到是游客账号,无法添加好友!')
            chatroom_helper()
        else:
            print('Welcome!')
            friend_helper()
    elif h1 == '4':
        judge()
    else:
        print('\n无效选择!')
        chatroom_helper()


def friend_helper():
    a = input('\n\n----------------------------------------------------------------------------------------------------'
              '----'
              '---------\n                                              friend界面\n帮助：1.输入0返回聊天室帮助界面                   '
              '                                                ====\n     2.输入1进入添加好友界面                               '
              '                                 ====     ====\n     3.输入2查看我的好友                                  '
              '       '
              '                      ==== {}  ====\n     4.输入3删除好友                                           '
              '                           ====     ====\n     5.输入4返回system主页面                                        '
              '                           ====\n-----------------------------------------------------------------------'
              '------------------------------------------\n请输入:'.format(n_z[0]))
    if a == '0':
        chatroom_helper()
    elif a == '1':
        friend.find_friend()
    elif a == '2':
        friend.get_friend(2)
    elif a == '3':
        friend.delete_friend()
    elif a == '4':
        judge()
    else:
        print('\n无效选择!')
    friend_helper()


if __name__ == '__main__':
    variables.n_z.append('  visitor ')
    chatroom_helper()
