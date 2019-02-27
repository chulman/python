import socket

def convert_integer():
    data=1234
    # 32-bit long
    print ('original: %s -> long host byte order: %s, network byte order:%s' %(data,socket.ntohl(data),socket.htonl(data)))
    # 16-bit short
    print ('original: %s -> long host byte order: %s, network byte order:%s' %(data,socket.ntohs(data),socket.htons(data)))


convert_integer()





host_port = 0x3456
host_ip = 0x12345678

network_ip_order = socket.htonl(host_ip)
network_port_order = socket.htons(host_port)

print("CPU is Intel")
print("Host %x" %(host_ip))
print("Network Byte Order %x" %(network_ip_order))
print("Port %x" %(host_port))
print("Network Byte Order %x" %(network_port_order))


