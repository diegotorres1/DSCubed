#test for the sensor client test
from client_control import client_control
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-svip',default = '192.168.1.18',type = str, dest = 'server_ip',help = 'server_ip string')
    parser.add_argument('-svp',default='8000',type = int, dest = 'server_port',help='server port integer')
    parser.add_argument('-vp',default = '8006',type = int, dest = 'video_port',help='video port integer')
    parser.add_argument('-sp',default = '8005',type = int, dest = 'sensor_port',help='sensor port integer')
    parser.add_argument('-sc',default = '8007',type = int, dest = 'control_port',help='control port integer')

    args = parser.parse_args()
    server_ip = args.server_ip
    control_port = args.control_port

    s = client_control(server_ip, control_port)
if __name__ == '__main__':
    main()
    print('server test completed')
