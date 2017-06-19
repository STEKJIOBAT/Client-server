import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('127.0.0.1', 8080))
while True:
    try:
        s.send(input().encode())
    except KeyboardInterrupt:
        s.close()