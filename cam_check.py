import os,subprocess,time
cams_c = 'v4l2-ctl --list-devices | grep camera'
res_me = 'sudo systemctl restart motioneye'
a=0
while True:
    try:
        check_cam = subprocess.Popen(cams_c,shell=True,stdout=subprocess.PIPE).communicate()
        check_cam = check_cam[0]
        # print(check_cam.decode())
        if check_cam.decode() == '':
            print('camera disconnect')            
            while True:
                try:
                    re_check_cam = subprocess.Popen(cams_c,shell=True,stdout=subprocess.PIPE).communicate()
                    re_check_cam = re_check_cam[0]
                    if not re_check_cam.decode() == '':
                        print('camera connect again, restarting motioneye')
                        time.sleep(1)
                        os.system(res_me)
                        time.sleep(1)
                        break
                    time.sleep(1)
                except:
                    pass
        time.sleep(1)
    except:
        pass