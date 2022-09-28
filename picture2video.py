import numpy as np
import cv2
import os

showDir1=r"E:\img_out"
files=os.listdir(showDir1)
s=[]
for file in files:
    if os.path.join(showDir1,file).endswith('.png'):
        s.append(os.path.join(showDir1,file))

size = (1080,1920)#这个是图片的尺寸，一定要和要用的图片size一致
#完成写入对象的创建，第一个参数是合成之后的视频的名称，第二个参数是可以使用的编码器，第三个参数是帧率即每秒钟展示多少张图片，第四个参数是图片大小信息
videowrite = cv2.VideoWriter(r'D:\test2.mp4',-1,30,size)#20是帧数，size是图片尺寸
img_array=[]
filelen=len(s)
for filename in s:#这个循环是为了读取所有要用的图片文件
    img = cv2.imread(filename)
    print(filename)
    if img is None:
        print(filename + " is error!")
        continue
    img_array.append(img)
for i in range(filelen):#把读取的图片文件写进去
    videowrite.write(img_array[i])
videowrite.release()
print('end!')
