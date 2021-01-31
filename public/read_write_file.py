# -*- coding: UTF-8 -*-
def my_read_list(filepath):
    str2 = ""
    with open(filepath, encoding='Utf-8') as fp:
        content = fp.readlines()
        for c in content:
            str2 += c.replace('\n', '\n')
        fp.close()
        return list(eval(str2))


def my_read_dict(filepath):
    fr = open(filepath, 'r+', encoding='UTF-8')
    dic = eval(fr.read())  # 读取的str转换为字典
    fr.close()
    return dic


def write_file(filepath, message):
    with open(filepath, 'w', encoding='UTF-8') as fw:
        fw.write(str(message))
