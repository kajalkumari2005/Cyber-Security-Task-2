import socket

target = "10.0.2.15"
port = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

try:
    sock.connect((target, port))
    sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")

    banner = sock.recv(1024).decode(errors="ignore")
    print("Banner/Response:")
    print(banner)

except Exception as e:
    print("Error:", e)

finally:
    sock.close()
