import socket
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-svip',default = '192.168.0.13',type = str, dest = 'server_ip',help = 'server_ip string')
parser.add_argument('-svp',default='8000',type = int, dest = 'server_port',help='server port integer')
parser.add_argument('-vp',default = '8006',type = int, dest = 'video_port',help='video port integer')
parser.add_argument('-sp',default = '8005',type = int, dest = 'sensor_port',help='sensor port integer')

args = parser.parse_args()
server_ip = args.server_ip
video_port = args.video_port


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((server_ip, video_port))
if result == 0:
   print ("Port is open")
else:
   print ("Port is not open")
