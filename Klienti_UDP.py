from socket import * 
port=9000 
server="localhost" 
clientSocket=socket(AF_INET,SOCK_DGRAM) 
mesazhi=input()
clientSocket.sendto(mesazhi.encode("utf-8"),(server,port)) 
mesazhi , adresa=clientSocket.recvfrom(2024) 
print(mesazhi.decode("utf-8"))