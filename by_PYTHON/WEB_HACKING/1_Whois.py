import whois
import socket

url="changwon.ac.kr"

try:
    url_info=whois.whois(url)
    ip=socket.gethostbyname(url)
    print("IP: ",ip)
    print("URL: ",url)
    print("Name: ",url_info.name)
    print("Email: ",url_info.email)
    print("Expiration date: ",url_info.expiration_date)
    print("Creation date: ",url_info.creation_date)
    print("Updated date: ",url_info.updated_date)
    print("Registrar: ",url_info.registrar)
    print("Name servers: ",url_info.name_servers)
    print("1차 domain server ip: ",socket.gethostbyname(url_info.name_servers))
    print("Status: ",url_info.status)
    print("Country: ",url_info.country)
except:
    print("존재하지 않는 URL인듯...")
