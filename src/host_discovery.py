import socket

network = "10.0.2."

for i in range(1, 255):
    ip = network + str(i)

    try:
        socket.gethostbyaddr(ip)
        print(ip, "is alive")
    except:
        pass
