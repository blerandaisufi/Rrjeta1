from socket import *
import time
from socket import *
import time
import random
import string
port=9000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(("",port))
print ("Server is running...")
rand=""
i=0
numriKerkesave=0
while True : 
   mesazhi , addresa=serverSocket.recvfrom(2024)
   tekst=mesazhi.decode("utf-8")
   try:
     if tekst.startswith("SaPerqindZeNumri1neNumrin2") :
          b=str(100*int(tekst.split()[1])/int(tekst.split()[2]))
          serverSocket.sendto(b.encode("utf-8"),addresa)
   except :
       a="Programi nuk eshte ne rregull  "
       serverSocket.sendto(a.encode("utf-8"),addresa) 