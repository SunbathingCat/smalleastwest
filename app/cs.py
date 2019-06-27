from Cryptodome.Cipher import AES
from Cryptodome import Random
from mymods.random_str import randstr
key = randstr(16,'sz')
iv = Random.new().read(AES.block_size)
with open('mima.txt','w') as f:
    f.write('key:{}\niv:{}'.format(key,iv))