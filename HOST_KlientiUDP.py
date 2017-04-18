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
def zanoret(mesazhi):
     zanoret="ae"
     iterator=0
     mesazhi=' '.join(mesazhi.split()[1:])
     for char in mesazhi:
       if char in zanoret:
           iterator+=1
     return iterator
numriKerkesave=0
while True : 
   mesazhi , addresa=serverSocket.recvfrom(2024)
   tekst=mesazhi.decode("utf-8")
   try:
      if tekst == "HOST" :
          try:
            a=gethostname()
            serverSocket.sendto(a.encode("utf-8"),addresa)
          except :
            a="Emri i Hostit nuk u gjet "
            serverSocket.sendto(a.encode("utf-8"),addresa)
          numriKerkesave+=1    
   except :
            a="Programi nuk eshte ne rregull  "
            serverSocket.sendto(a.encode("utf-8"),addresa)