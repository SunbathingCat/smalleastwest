from Cryptodome.Cipher import AES
from Cryptodome import Random
from mymods.random_str import randstr
# from binascii import b2a_hex

def GenerateAESKeys(long=16):
    '''
    生成密码
    :param long: 必须为16，24，32，越长越安全,单位字符
    :return:
    '''
    key = randstr(long,'sz')
    iv = Random.new().read(AES.block_size)
    with open('mima.txt','w') as f:
        f.write('key:{}\niv:{}'.format(key,iv))
    return (key,iv)

def AES_en(key,iv,data):
    '''
    加密数据
    :param key: 密钥
    :param iv: 必要参数
    :param data: 数据
    :return: 加密字符串
    '''
    mycipher = AES.new(key.encode('utf-8'), AES.MODE_CFB, iv)
    ciphertext = iv + mycipher.encrypt(data.encode('utf-8'))
    return ciphertext

def AES_de(key,data):
    '''
    解密数据
    :param key: 密钥
    :param iv: 必要参数
    :param data: 加密字符串
    :return: 原来数据
    '''
    mydecrypt = AES.new(key.encode('utf-8'), AES.MODE_CFB, data[:len(key)])
    decrypttext = mydecrypt.decrypt(data[len(key):])
    return decrypttext.decode('utf-8')

# key,iv = GenerateKeys()
# print(key,iv)
# data = 'exit_flag = input("亲,你确定要退出么?~~~~(>_<)~~~~(yes or no) ")'
# jami = AES_en(key,iv,data)
# with open('tem.txt','wb') as f:
#     f.write(jami)

# key = '1Nr988Uc3S3B4n4q'
# with open('tem.txt','rb') as f:
#     data = f.read()
# jiemi = AES_de(key,data)
# print(jiemi)