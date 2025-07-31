# -*- coding:utf8 -*-
import os
import glob
import shutil
import whatimage
import pillow_heif
from PIL import Image as pilImage
import argparse
 
gSrcPath=None
gDestPath=None
gShowInfo=False
 
def getPicFromDir(picPath):
    '''获取指定目标下的所有picture文件列表'''
    if not os.path.isdir(picPath):
        return None
    ext_names = ['.jpg', '.png', '.jpeg','*.webp','*.bmp','*.gif','.HEIC']
    allImgs=[]
    for ext in ext_names:
        filenams=os.path.abspath(os.path.join(picPath,"./*%s" % ext))
        allImgs.extend(glob.glob(filenams))
    if len(allImgs)!=0 :
        return allImgs
    else:
        return None
   
 
 
def convert_heic_jpg(src_img_path):
    dest_img_path=os.path.join(gDestPath,os.path.basename(src_img_path))
    with open(src_img_path, 'rb') as f:
        heic_img = f.read()
    # 获取图征文件格式
    img_format = whatimage.identify_image(heic_img)
    if gShowInfo:
        print(f'{os.path.basename(src_img_path)} Image format:{img_format}')
    if img_format in ['heic']:
        img = pillow_heif.read_heif(heic_img)
        pi = pilImage.frombytes(mode=img.mode, size=img.size, data=img.data)
        fn,_=os.path.splitext(dest_img_path)
        pi.save(fn+'.jpg', format="jpeg")
    else:
        try:
            shutil.copyfile(src_img_path,dest_img_path)
        except Exception as e:
            print("复制文件发生错误：", str(e))
        
if __name__ == '__main__':
  
    argp=argparse.ArgumentParser(description='heif格式图片转换成jpeg格式')
    argp.add_argument('--src_path',default=r'F:\LNG\2',help='指定源图片文件所在文件目录')
    argp.add_argument('--dest_path',default=r'F:\LNG\2-2',help='指定保存转换后图片文件目录')
    argp.add_argument('-V','--verbose',action='store_true',help='显示详细信息')
    try:
        args=argp.parse_args()
    except:
        exit(2)
    
    gSrcPath=args.src_path
    gDestPath=args.dest_path
    gShowInfo=args.verbose
    
    if os.path.isdir(gSrcPath) and os.path.isdir(gDestPath):
        pics=[]
        pics=getPicFromDir(gSrcPath)
        if pics:
            for f in pics:
                convert_heic_jpg(f)
        else:
            print(f'{gSrcPath}目录中没有包含图片文件,请确保其中包含jpg, png, jpeg等后缀的图片文件。')
            exit(1)
    else:
        print(f'{gSrcPath} 或 {gDestPath} 目录指定不正确。')
        exit(1)
