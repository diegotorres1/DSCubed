#Author: Diego Torres
#Date Modification : 10/20/2018
#Description : Server is placed in computer
import socketserver
class video_stream_handler(socketserver.StreamRequestHandler):
    def handle(self):
        recv_size = 1024
        print('video_stream_handler : HANDLE YES')
        try:
            print('Connection')
            while True:
                #need to read posted data
                stream_bytes += self.rfile.read(recv_size)
                #identify the tags in the data being sent for the image
                first = stream_bytes.find(b'\xff\xd8')
                last =  stream_bytes.find(b'\xff\xd9')
                if (first != -1 and last != -1):
                    i = stream_bytes[first:(last + 2)]
                    #move the stream bytes to the next image
                    stream_bytes = stream_bytes[last + 2]
                    image = cv2.imdecode(np.fromstring(i,dtype = np.uint8),cv2.CV_LOAD_IMAGE_UNCHANGED)
                    cv2.imshow('stream',image)
                    if(cv2.waitKey(33) == 27):
                        print('Stream stopped')
                        break

        finally:
            cv2.destroyAllWindows()
            return 0
