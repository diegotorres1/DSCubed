from server import server
def main():
    # server_ip = '192.168.1.13'
    server_ip = '169.234.47.26'
    sensor_port = 8005
    video_port = 8006
    s = server(server_ip, video_port, sensor_port)
if __name__ == '__main__':
    main()
    print('server test completed')
