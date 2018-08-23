import sys
import shutil
import psutil
import time
from _datetime import datetime

# SAVE_PATH = "D:\\a"

def get_disk_path(disk_num):
    path = chr(66+disk_num)+":\\"
    # print(os.path.isdir(path))
    return path

def get_disk_num():
    return len(psutil.disk_partitions())

'''
 # dp：the list of the computer disk
   we can get the symbol of the disk by the length of it
   var char(66+len(list)),C,D,E and so on 
'''
def main(argv):
    if len(argv)>1:
        SAVE_PATH = argv[1]
        print("change SAVE_PATH")
    else:
        SAVE_PATH = "D:\\a\\"
        print("no change SAVE_PATH")
    num_former_disk = get_disk_num()
    while(1):
        num_now_disk=get_disk_num()
        if num_former_disk==num_now_disk-1 :
            usb_path = get_disk_path(num_now_disk)
            try:
                print("start work")
                shutil.copytree(usb_path, SAVE_PATH+datetime.now().strftime("%Y%m%d"))
            except IOError as e:
                print(e.args)
            break
        else:
            time.sleep(10)

    print('work done')


if __name__ == "__main__":
    main(sys.argv)