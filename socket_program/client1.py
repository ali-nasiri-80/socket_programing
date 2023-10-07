import socket
sock = socket.socket()
hostName = socket.gethostname()
port = 21000
sock.connect((hostName,port))
r = sock.recv(1024)
print(r)
