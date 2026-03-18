# Use this code for educational purposes, please!

import socket
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from time import time
lock = Lock() # I've added Lock object
port_degerler = {21: "FTP",
                 22: "SSH",
                 23: "Telnet",
                 53: "DNS",
                 80: "HTTP",
                 443: "HTTPS",
                 3306: "MySQL"}
open_ports = []
def port_scan(ip,p):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout) 
        try:
            s.connect((ip,p))
            print(f"{p} AÇIK!")
            with lock:
                open_ports.append(p)
            banner_grab(s,ip,p) # I've done banner grabbing. 😊😊
        except (TimeoutError, ConnectionRefusedError):
            pass
        except Exception as e:
            print("Hata: ", e)
        finally:
            s.close()
def banner_grab(sock,ip,p):
    if p == 21 or p == 22:
        try:
            banner = sock.recv(1024).decode(errors="ignore").strip()
            print(f"Banner: {banner}")
        except:
            print("Banner bulunamadı.")
    if p == 80:
        request = f"HEAD / HTTP/1.1\r\nHost:{ip}\r\nConnection: close\r\n\r\n"
        sock.send(request.encode())
        try:
            response = sock.recv(4096).decode(errors="ignore").strip()
            for line in response.split("\r\n"):
                if "Server" in line:
                    print(line)
        except:
            print("Banner bulunamadı.")
while True:
    try:
        ip = input("IP adresini giriniz: ")
        timeout = float(input("Timeout'ı giriniz(Varsayılan 1): ")) # User enters timeout number
        baslangic_port = int(input("Başlangıç portunu giriniz(minimum: 1):")) # I've added user input for start port
        son_port = int(input("Bitiş portunu giriniz(maximum: 65535):")) # Also I've added user input for end port
    except ValueError:
        print("Lütfen tam sayı ya da ondalık sayı girin.\n")
        continue
    
    if timeout > 0 and baslangic_port > 0 and son_port > 0 and son_port < 65536:
        baslangic = time() # I've added time measurement
         # I've added ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=50) as executor:
            for p in range(baslangic_port, son_port+1):
                executor.submit(port_scan, ip, p)
        break
    else:
        print("Değerleri girerken hata yaptınız. Lütfen baştan giriniz.")
        continue
bitis = time()
print(f"Toplam süre: {round(bitis-baslangic)} saniye.\n")
siralanmis = sorted(open_ports)  # I've sorted all ports at one valueable
print("AÇIK PORTLAR: ", siralanmis) 
with open("scan_results.txt","w",encoding="utf-8") as file: # I'm writing .txt file. 😃
    for port in siralanmis:
        servis = port_degerler.get(port, "Bilinmeyen Değer") # I've made simply this list
        if servis:
            print(f"Port: {port} --- Servis: {servis}")
            file.write(f"Port: {port}\nServis: {servis}\n\n")
open_ports.clear()
