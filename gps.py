import os, subprocess, threading, datetime, time
home_path = '/home/'+os.listdir('/home')[0]+'/'
logs = home_path+'logs/'
if not os.path.exists(logs):
    os.makedirs(logs)

def update():
    CAM_CONFIG_FILE="/etc/motioneye/camera-1.conf"
    while True:
        try:
            global lat,long,speed
            lat,long,speed=str(lat),str(long),str(speed)
            com = 'curl "http://localhost:7999/1/config/set?text_left='+lat+'%20'+long+'\n'+speed+'km/h"'
            out,_=subprocess.Popen(com,shell=True,stdout=subprocess.PIPE).communicate()
            time.sleep(1)
        except Exception as e:
            pass

def receive_data():
    pass

def log_data():
    while True:
        try:
            my_time = datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")
            global datas
            signal,lat,long,speed,alti,course,hdop=datas
            data_to_write = my_time + ' - NoS= ' + str(signal) + ',lat= ' + lat + ',long= ' + long + ',speed= ' + str(speed) + ',alti= ' +  alti + ',course= ' + course + ',HDOP= ' + hdop
            with open(logs+'gps_logger.txt','a+') as f:
                f.write(data_to_write)
            time.sleep(1)
        except:
            pass