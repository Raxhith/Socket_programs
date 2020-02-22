#	client pgm wrt to server using internet....Networking.

import socket
if __name__ == '__main__':
	try:
		client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print('Socket created at client side')

		host = 'data.pr4e.org'
		port_no = 80
		address = (host, port_no)
		client_sock.connect(address)
		print(f'Socket connected to host {host} running on port_no {port_no}')

		data = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0 \r\n\r\n'
		client_sock.send(data.encode())

		bufsize = 1024
		while True:
			data = client_sock.recv(bufsize).decode()
			if len(data)<1:
				break
			print(data)

	except socket.error as msg:
		print(f'Exception cause: {msg}')
	finally:
		client_sock.close()
		print('client_sock is closed.')