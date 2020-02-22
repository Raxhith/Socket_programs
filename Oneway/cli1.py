#   ---One way Communication---

import socket
if __name__ == '__main__':
    try:
    	client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    	print('Client socket created.')

    	ip_addr = 'localhost'
    	port_no = 6000
    	address = (ip_addr,port_no)
    	client_sock.connect(address)
    	print(f'socket binded to ip_addr {ip_addr} running on port_no {port_no}')

    	bufsize = 1024
    	data = client_sock.recv(bufsize).decode('utf-8')
    	print(f'msg from server is {data}')

    except socket.error as msg:
    	print(msg)
    finally:
    	client_sock.close()
    	print('client_sock is closed')