import socket
import threading

ip = input("IP adresini giriniz: ")
open_ports = []
threads = []
def port_scan(ip,p):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5) # I've increased timeout
        try:
            s.connect((ip,p))
            print(f"{p} AÇIK!")
            open_ports.append(p)
        except:
            pass
        finally:
            s.close()
# I've added Threading
for p in range(1,1001):
    thread = threading.Thread(target=port_scan,args=(ip,p))
    threads.append(thread)
    thread.start()
for thread in threads:
     thread.join()
print("AÇIK PORTLAR: ", sorted(open_ports)) # I've sorted all ports

