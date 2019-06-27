from mymods.JiaMi.AES import *
from mymods.JiaMi.RSA import *

# 待加密内容
mes = '在返回的@#$%!^&响应内容（html）中<>?，会带有css、js、图片等url地址，以及ajax代码，浏览器按照响应内容中的顺序依次发送其他的请求，并获取相应的响应'

# aes_key---aes加密密钥，iv---自动生成的参数，和aes_key一起用于加密
aes_key,iv = GenerateAESKeys()
# pr_key---RSA私钥，pu_key---RSA公钥，公钥加密私钥解密
pr_key,pu_key = GenerateRSAKeys()

# AES用于加密数据，s_mes---加密后的数据
s_mes = AES_en(aes_key,iv,mes)

# RSA用于加密AES的密钥，s_aes_key---加密后的AES密钥
s_aes_key = RSA_en(aes_key,pu_key)

# 发送 加密后的信息和加密后的AES密钥（s_mes,s_aes_key） 给对方


# 对方解密
# 先用私钥解密得到原来的AES密钥
o_aes_key = RSA_de(s_aes_key,pr_key)
print('aes密钥为：',o_aes_key)

# 再用AES密钥解密得到原来的数据
o_mes = AES_de(o_aes_key,s_mes)
print('加密的消息为：',o_mes)