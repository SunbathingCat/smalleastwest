import random

__all__ = ['randstr']

def num():
    '''生成随机数字'''
    i = str(random.randint(0, 9))
    return i


def alp():
    '''生成随机字母'''
    if random.randint(0, 1):  # 随机大小写
        s = chr(random.randint(65, 90))
    else:
        s = chr(random.randint(97, 122))
    return s


def sym():
    '''生成随机符号'''
    sy = ['@', '#', '$', '%', '&', '*', '+', '-', '/', '\\', '!', '?']
    s = sy[random.randint(0, 11)]
    return s


def ranfun(typ):
    '''根据字符串组成类型选择随机函数'''
    optnas = [num(), alp(), sym()]
    optna = [num(), alp()]
    optas = [alp(), sym()]
    optns = [num(), sym()]

    if typ == 's':	# 数字
        return optnas[0]

    elif typ == 'z':	# 字母
        return optnas[1]

    elif typ == 'f':	# 符号
        return optnas[2]

    elif typ == 'sz' or typ == 'zs':
        return optna[random.randint(0, 1)]

    elif typ == 'zf' or typ == 'fz':
        return optas[random.randint(0, 1)]

    elif typ == 'sf' or typ == 'fs':
        return optns[random.randint(0, 1)]

    elif typ == 'szf' or typ == 'sfz' or typ == 'zsf' or typ == 'zfs' or typ == 'fsz' or typ == 'fzs':
        return optnas[random.randint(0, 2)]

    else:
        print("字符串组成类型有误，已生成默认格式字符串，")
        return optna[random.randint(0, 1)]


def randstr(long=10,type='sz',num=1):
    '''
    生成指定长度，组成类型若干数量的随机字符串
    :param long: 所需字符串长度
    :param type: 字符串组成类型，s 代表数字，z 代表字母，f 代表符号
    :param num: 生成字符串数量
    :return: 如果num值为1则返回一个字符串，否则以列表形式返回num数量的字符串
    '''
    long = long
    typ = type
    howmany = num
    pwd = []
    for j in range(1, howmany + 1):
        password = ''
        for i in range(0, long):
            password = password + ranfun(typ)
        # print('生成的第%d组密码：%s' % (j, password))
        pwd.append(password)
    if num == 1:
        return pwd[0]
    else:
        return pwd

if __name__ == '__main__':
    print(randstr())
    print(randstr(8,'szf',5))
