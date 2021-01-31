# -*- coding: UTF-8 -*-
import os

a21 = ''  # 临时储存
b = ''  # 密码
a4 = ''  # 临时储存
stub_path = os.path.dirname(os.path.realpath('')) + '\\system\\public\\users\\'
mp = stub_path
aanp = stub_path + 'administrator_account_number_password.txt'
am = stub_path + 'all_message.txt'
uan = stub_path + 'user_account_number.txt'
uanp = stub_path + 'user_account_number_password.txt'
uf = stub_path + 'user_friends.txt'
um = stub_path + 'user_message.txt'
if_on = False
c2c2 = []  # 管理员初始密码&重设密码
z = ['  visitor ']  # 储存账号
s56 = []  # 储存已就绪的版本
n_z = []  # 临时储存当前使用的账号
a_m = []  # 储存所有信息
n_s = []  # 储存当前正在使用的系统
toss_data = [0, 0, 0]
f1 = {}  # 账号密码临时储存
al3 = {}  # 管理员账号&密码
z_m = {'  visitor ': None}  # 储存账号密码
msg = {'  visitor ': []}  # 储存所有信息&发出的人
all_friend = {'  visitor ': []}  # 储存朋友信息
n = 0  # 骰子
m = 0  # 骰子
q = 0  # 骰子
