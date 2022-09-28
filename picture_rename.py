# 用于批量修改图片文件的名字

import os
paths = os.listdir('D:\project\picture\data_1')
num= 0
for path in paths:
    num = num + 1
    name3 = str(num).zfill(6) + '.png'
    os.rename('D:\project\picture\data_1\\{0}'.format(path),'D:\project\picture\data_1\\{0}'.format(name3))