# encoding: gbk
from time import sleep
from public import variables, read_write_file
from chat import index
a_m = variables.a_m
p_m = {}
n_z = variables.n_z
msg = variables.msg


# \n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n
def chat():
    print(
        '------------------------------------------------------------------------------------------------------------'
        '-----\n                                         welcome to chatting room\n                                  '
        '======   =     =    =======    =========\n                                =          =     =   =       =    '
        '   =\n                               =           =======  =         =      =\n                              '
        '  =          =     =   =       =       =\n                                  ======   =     =    ======  === '
        '   =\nloading...\n------------------------------------------------------------------------------------------'
        '-----------------------\n'
    )
    sleep(3)
    send()


def send():
    print('------------------------------------------------------------------------------------------------------------'
          '-----')
    if len(a_m) < 10:
        for i in a_m:
            print(i + '\n')
    else:
        n = 0
        h = []
        for i3 in a_m[::-1]:
            h.append(i3)
            n += 1
            if n == 10:
                for i2 in h[::-1]:
                    print(i2 + '\n')
    print('------------------------------------------------------------------------------------------------------------'
          '-----')
    me = input('(enter with message=send,enter with no message=exit)message:')
    if me == '':
        if input('Do you want to exit?(Yes(write “y”)/No(Enter)):') == 'y':
            print('\nexited!')
            variables.if_on = False
            index.chatroom_helper()
        else:
            print('\nreturned!')
            send()
    s_m = '{}:{}'.format(n_z[0], me)
    msg.get(n_z[0]).append(me)
    a_m.append(s_m)
    read_write_file.write_file(variables.am, variables.a_m)
    read_write_file.write_file(variables.um, variables.msg)
    send()


if __name__ == '__main__':
    variables.n_z.append('  visitor ')
    send()
