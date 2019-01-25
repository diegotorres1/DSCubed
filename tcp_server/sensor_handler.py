class sensor_handler(socketserver.BaseRequestHandler):
    def handle(self):
        recv_size = 1024
        stream_bytes = b''
        print('sensor_handler : HANDLE YES')
        try:
            print('Connection')
            while True:
                #need to read posted data
                stream_bytes += self.rfile.read(recv_size)
                #identify the tags in the data being sent for the image jpeg
                first = stream_bytes.find(b'sensor_start')
                last =  stream_bytes.find(b'sensor_end')
                if (first != -1 and last != -1):
                    #the plus 2 is from the '<2'

                    i = stream_bytes[first:last + 2]
                    stream_bytes = stream_bytes[last + 2:]
                    values = np.fromstring(i,dtype = np.uint8)

                    try:
                        print('Voltage_1:' + values[0])
                    except Exception as e:
                        print(e)
                        print('Voltage_1 was incorrectly read, ' + str(values))
                    if(cv2.waitKey(33) == 27):
                        print('Stream stopped')
                        break

        except Exception as e:
            print(e)
        finally:
            print('Windows Destroyed')
            cv2.destroyAllWindows()
            return 0
