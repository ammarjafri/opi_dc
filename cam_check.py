import os,subprocess,time
com = 'v4l2-ctl --list-devices | grep camera'
com_1 = 'sudo systemctl restart motioneye'
a=0
#while True:
#    try:
check_cam = subprocess.Popen(com,shell=True,stdout=subprocess.PIPE).communicate()
check_cam = check_cam[0]
print(check_cam.decode())
#        for fi in check_cam:
    #         if a==0:
    #             pass
    #     if a==1:
    #         while True:
    #             check_cam = subprocess.Popen(com,shell=True,stdout=subprocess.PIPE).communicate()
    #             if a==0:
    #                 os.system(com_1)
    #                 time.sleep(1)
    #                 break
    #     time.sleep(1)
    # except:
    #     pass