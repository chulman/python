import socket

def print_mynetwork_info():
    host = socket.gethostname()
    ip_addr = socket.gethostbyname(host)
    print('HOST:' + host)
    print("ip Address:" + ip_addr)    

def print_remoteNetwork_info():
    remote_host = 'www.naver.com'
    remote_ip = socket.gethostbyname(remote_host)
    try:
        print(remote_host)
        print(remote_ip)
    except socket.error as identifier:
        #예외 무시
        pass
    except:
        print('all eror')
        #예외 무시
        pass    
    finally:
        print('end')


if __name__ == '__main__':
    print_mynetwork_info()
    print_remoteNetwork_info()