from client import client
def main():
    server_ip = 192.168.1.13
    server_port = 8000
    sensor_port = 8005
    video_port = 8006
    s = client()
if __name__ == '__main__':
    main()
    print('server test completed')
