import socket
s = socket.socket(); s.settimeout(1)
print("Port 50030:", "Open" if s.connect_ex(('127.0.0.1', 50030)) == 0 else "Closed")
s.close()
