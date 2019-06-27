import os
# 合并
dir = '04'
path = 'F:\\tss\\' + dir + '\\' + '*.ts '
path2 = 'F:\\tss\\' + dir + '.mp4'
cmd = 'copy /b ' + path + path2
try:
    os.system(cmd)
except:
    print('fail')
else:
    print('succeful')
