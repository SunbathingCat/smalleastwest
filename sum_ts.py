import os
# 合并ts文件为mp4
dir = 'tss'
path = 'F:\\' + dir + '\\' + '*.ts '
path2 = 'F:\\' + dir + '.mp4'
cmd = 'copy /b ' + path + path2
try:
    os.system(cmd)
except:
    print('gg')
else:
    print('ok')
