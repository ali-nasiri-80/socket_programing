#Write a program that displays the name and IP of the computer
"""import socket
def printmachineinfo():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: %s"%host_name)
    print("ip address: %s"%ip_address)
    
printmachineinfo()
"""
#---------------------------------------------------
#A program that finds and displays the service name of specific ports
"""import socket 
def find_service_name(list,protocolname):
    for port in list:
        print("port: %s =>service name: %s"%(port,socket.getservbyport(port,protocolname)))
        print("port %s =>service name:%s"%(53,socket.getservbyport(53,'udp')))
        
protocolname = 'tcp'
list = [25,80]
find_service_name (list, protocolname)
"""