import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('169.234.47.26', 8006))
if result == 0:
   print ("Port is open")
else:
   print ("Port is not open")
