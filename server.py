import socket


server_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 8080))
clients = []
while True:
    try:
        data, addr = server_socket.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
        print('From IP {}, port {}: {}'.format(addr[0], addr[1], data.decode()))
        # for client in clients:
        #     server_socket.sendto(data, client)
    except KeyboardInterrupt:
        server_socket.close()
