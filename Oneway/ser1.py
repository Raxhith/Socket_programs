#   ---One way Communication---

import socket
if __name__ == '__main__':
    try:
    	server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    	print('Server socket created.')

    	ip_addr = 'localhost'
    	port_no = 6000
    	address = (ip_addr,port_no)
    	server_sock.bind(address)
    	print(f'socket binded to ip_addr {ip_addr} running on port_no {port_no}')

    	backlog = 10
    	server_sock.listen(backlog)
    	print(f'Server listening to {backlog} requests')
    	client_access,(client_ip, port_no) = server_sock.accept()
    	print('Server ready to accept')
    	data = 'Client got connected'
    	client_access.send(data.encode('utf-8'))

    except socket.error as msg:
    	print(msg)
    finally:
    	client_access.close()
    	print('client_access is closed')
