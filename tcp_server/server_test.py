from server import server
def main():
    server_ip = 192.168.1.13
    sensor_port = 8005
    video_port = 8006
    s = server()
if __name__ == '__main__':
    main()
    print('server test completed')
