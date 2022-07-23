from bypy import ByPy
import os
import datetime

# 百度云存放文件的文件夹名
dir_name = "nft"

# 获取一个bypy对象，封装了所有百度云文件操作的方法
bp = ByPy()
# 百度网盘创建远程文件夹
bp.mkdir(remotepath=dir_name)

# 获取文件的大小,结果保留两位小数，单位为MB
def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)

def upload(path):
    file = open(path)
    start = datetime.datetime.now()  # 计时开始
    # bp.upload(localpath=file, remotepath=dir_name, ondup='newcopy')
    print("正在上传文件:" + file.name)
    uploadres = bp.upload(path, dir_name, 'newcopy')
    print("文件发送完成：" + file.name + " 远程文件夹：" + dir_name)
    end = datetime.datetime.now()  # 计时结束
    print("上传文件总大小为" + str(os.path.getsize(path)/1024/1024) + "MB")
    print("花费时间(s)：" + str((end - start).seconds))
    return "/我的应用数据/bypy/"+dir_name+"/"