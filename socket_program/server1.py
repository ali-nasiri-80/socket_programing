import socket
sock = socket.socket()
hostName = socket.gethostname()
port = 21000
sock.bind((hostName,port))
sock.listen(10)
while True:
    con, address = sock.accept()
    print("i,m now connected to",address)
    msg = "python networkinnng"
    con.send(msg.encode("UTF-8"))
con.close()