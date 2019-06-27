import rsa
def GenerateRSAKeys(long=1024):
    '''
    生成一对密钥
    :param long: 128,256,512,1024,2048,4096,越大耗时越长，越安全，可加密内容越长
    :return: （私钥，公钥）
    '''
    (pubkey, privkey) = rsa.newkeys(long)

    with open('public.pem','w+') as f:
        f.write(pubkey.save_pkcs1().decode())
    with open('private.pem','w+') as f:
        f.write(privkey.save_pkcs1().decode())
    return (privkey, pubkey)

def LoadKeys():
    '''
    从当前目录导入密钥，文件名必须为private.pem或public.pem
    :return: 返回导入的密钥，如果导入两个则返回（私钥，公钥）
    '''
    try:
        with open('private.pem', mode='rb') as privatefile:
            keydata = privatefile.read()
        privkey = rsa.PrivateKey.load_pkcs1(keydata)
    except:
        privkey = ''
    try:
        with open('public.pem', mode='rb') as pubkeyfile:
            keydata = pubkeyfile.read()
        pubkey = rsa.PublicKey.load_pkcs1(keydata)
    except:
        pubkey = ''
        if privkey == '':
            print('没有可加载的密钥文件')
            return
    if pubkey and privkey:
        return (privkey,pubkey)
    if privkey != '':
        return privkey
    else:
        return pubkey

def RSA_en(message,pubkey):
    message = message.encode('utf-8')
    crypto = rsa.encrypt(message,pubkey)
    return crypto

def RSA_de(crypto,privkey):
    message = rsa.decrypt(crypto,privkey).decode('utf-8')
    return message


# keys = GenerateKeys()
# message = 'hello Bob! 你好'.encode('utf8')
# crypto = rsa.encrypt(message, keys[1])
# with open('tem.txt','wb') as f:
#     f.write(crypto)


# keys = LoadKeys()
# with open('tem.txt','rb') as f:
#     crypto = f.read()
# message2 = rsa.decrypt(crypto, keys)
# print(message2.decode('utf8'))

