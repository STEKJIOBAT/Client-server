import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(1)
sock, client=s.accept()
data=sock.recv(1024).decode()
sock.close()
s.close()
print (data)