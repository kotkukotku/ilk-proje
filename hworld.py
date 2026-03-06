# Use this code for educational purposes, please!
# I created this code with AI helping.
import socket
from concurrent.futures import ThreadPoolExecutor

ip = input("IP adresini giriniz: ")
timeout = int(input("Timeout'ı giriniz(Varsayılan 1): ")) # User enters timeout number
open_ports = []
threads = []
def port_scan(ip,p):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout) 
        try:
            s.connect((ip,p))
            print(f"{p} AÇIK!")
            open_ports.append(p)
        except (TimeoutError, ConnectionRefusedError):
            pass
        except Exception as e:
            print("Hata: ", e)
        finally:
            s.close()
# I've added ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=50) as executor:
    for p in range(1,1001):
        executor.submit(port_scan, ip, p)
print("AÇIK PORTLAR: ", sorted(open_ports)) # I've sorted all ports

