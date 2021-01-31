# -*- coding: UTF-8 -*-
def natural_num_dec(number):
    if type(number) is not int:
        return False
    else:
        if number > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(natural_num_dec(1), natural_num_dec('1'), natural_num_dec([1]), natural_num_dec({1}), natural_num_dec(1.1))
