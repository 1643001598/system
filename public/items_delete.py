# -*- coding: UTF-8 -*-
a = {'1643001598': '=1=1=1=1=1=1=1=1=1=', '1234567890': '0987654321', '0123012301': '1231231231'}
b = {1: 1, 2: 2, 3: 3}
c = [2, 3, 21, 321, 3, 2]


def items_delete(delete_dict, number):
    for i, n in list(enumerate(delete_dict)):
        if number == i:
            delete_dict.pop(n)


if __name__ == '__main__':
    items_delete(a, 1)
    items_delete(b, 2)
    print(a, b)
