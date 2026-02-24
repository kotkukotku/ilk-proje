import socket

ip = input("IP adresini giriniz: ")
open_ports = []
for p in range(1,1001):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip,p))
        print(f"{p} AÇIK!")
        open_ports.append(p)
    except:
        pass
    finally:
        s.close()
print("AÇIK PORTLAR: ", open_ports)

