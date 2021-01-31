# -*- coding: UTF-8 -*-
from time import sleep
from public import variables, natural_number_decide, read_write_file
from chat import index


def find_friend():
    c = variables.all_friend.get(variables.n_z[0])
    a = input('Enter the account number you want to find(print “0” to exit):')
    if a == '  visitor ':
        sleep(0.5)
        print('Wrong adding!')
        find_friend()
    if a == '0':
        sleep(0.5)
        print('Exited!')
        index.friend_helper()
    elif a not in variables.all_friend:
        sleep(0.5)
        print('This account number was not found!')
        find_friend()
    else:
        if a not in c and a != variables.n_z[0]:
            sleep(0.5)
            if input('Found!\nDo you want to add it(Yes(Enter)/No(write “n”)):') == 'n':
                print('Canceled!')
                find_friend()
            else:
                sleep(0.5)
                c.append(a)
                print('Added!')
                # print(variables.all_friend)
                read_write_file.write_file(
                    variables.uf,
                    variables.all_friend)
                find_friend()
        else:
            sleep(0.5)
            print('Wrong adding!')
            find_friend()


def get_friend(sleep_sec):
    c = variables.all_friend.get(variables.n_z[0])
    if c:
        print('You have {} friends'.format(len(c)))
        print('------------------------')
        n = 1
        for i in c:
            print('-Friend No.{}:{}-'.format(n, i))
            n += 1
        print('------------------------')
        sleep(sleep_sec)
    else:
        print('You have no friend!')
        sleep(0.5)


def delete_friend():
    c2 = variables.all_friend.get(variables.n_z[0])
    if not c2:
        print('You have no friend!')
        sleep(0.5)
        index.friend_helper()
    get_friend(0)
    v = str(input('Please print the number(No.) you want to delete(print “0” to exit):'))
    if v == '0':
        index.friend_helper()
    try:
        if natural_number_decide.natural_num_dec(int(v)) is False:
            print('Wrong input!')
            delete_friend()
    except ValueError:
        pass
    try:
        sleep(0.3)
        if input(
                'Do you want to delete Friend:{friend}?(yes(Enter)/No(print "n"))'.format(friend=c2[int(v) - 1])) == '':
            sleep(0.1)
            c2.pop(int(v) - 1)
            print('Deleted')
            read_write_file.write_file(
                variables.uf,
                variables.all_friend)
            delete_friend()
        else:
            print('Canceled!')
            delete_friend()
    except IndexError:
        print('Wrong number!')
        sleep(0.5)
        delete_friend()
    except ValueError:
        print('Wrong number!')
        sleep(0.5)
        delete_friend()


if __name__ == '__main__':
    variables.n_z.append('  visitor ')
