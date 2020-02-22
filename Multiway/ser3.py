#	---Multiway Communication---

import socket
if __name__ == '__main__':
	try:
		server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print('Server socket created.')

		ip_addr = 'localhost'
		port_no = 6002
		address = (ip_addr,port_no)
		server_sock.bind(address)
		print(f'socket binded to ip_addr {ip_addr} running on port_no {port_no}')

		backlog = 3
		server_sock.listen(backlog)
		print(f'listening...')

		client_access,(client_ip, port_no) = server_sock.accept()
		print('Server ready to accept')

		for i in range(3):
			bufsize = 1024
			data = client_access.recv(bufsize).decode('utf-8')
			print(f'From GF: {data}')

			data1 = input('To GF: ')
			client_access.send(data1.encode('utf-8'))

	except socket.error as msg:
		print(msg)
	finally:
		client_access.close()
		print('You are blocked...!')
