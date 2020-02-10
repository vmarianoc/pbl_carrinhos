import socket
import threading
from threading import Thread
import os
from vpython import *



#Criando um mapa
#Via H
box(pos=vector(0, 0, 0),
    size=vector(110, 10, 0), 
    color = color.gray(2))

#Via V
box(pos=vector(0, 0, 0),
    size=vector(10, 110, 0), 
    color = color.gray(2))

#Faixas H
box(pos=vector(0, 0, 0),
    size=vector(1, 110, 0), 
    color = color.yellow)

#Faixas V
box(pos=vector(0, 0, 0),
    size=vector(110, 1, 0), 
    color = color.yellow)

#Jardins
box(pos=vector(30, 30, 0),
    size=vector(50, 50, 0), 
    color = color.green)
box(pos=vector(-30, 30, 0),
    size=vector(50, 50, 0), 
    color = color.green)
box(pos=vector(30, -30, 0),
    size=vector(50, 50, 0), 
    color = color.green)
box(pos=vector(-30, -30, 0),
    size=vector(50, 50, 0), 
    color = color.green)

#Posicoes inicias de cada carro
carro1 = box(pos=vector(-50,2.5,0),
             size=vector(5.5,1.5,1.6),
             color=color.red)
             
carro2 = box(pos=vector(50,-2.5,0),
             size=vector(5.5,1.5,1.6),
             color=color.yellow)
             
carro3 = box(pos=vector(-2.5,50,0),
             size=vector(1.5,5.5,1.6),
             color=color.blue)  
             
carro4 = box(pos=vector(2.5,-50,0),
             size=vector(1.5,5.5,1.6),
             color=color.black)
          

def exibe(data):
    #As Informacoes recebidas sao tratadas, divididas e apresentadas na tela
    message = data.split("/")
    
    carro = message[0]
    pos_x = message[1] 
    pos_y = message[2]
    size_x = message[3]
    size_y = message[4]

    if carro == 1:
        carro1.pos.x = pos_x
        carro1.pos.y = pos_y
        carro1.size.x = size_x
        carro1.size.y = size_y
    if carro == 2:
        carro2.pos.x = pos_x
        carro2.pos.y = pos_y
        carro2.size.x = size_x
        carro2.size.y = size_y
    if carro == 3:
        carro3.pos.x = pos_x
        carro3.pos.y = pos_y
        carro3.size.x = size_x
        carro3.size.y = size_y
    if carro == 4:
        carro4.pos.x = pos_x
        carro4.pos.y = pos_y
        carro4.size.x = size_x
        carro4.size.y = size_y

 

def receive():
    #Funcao para receber as mensagens
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, [UDP_IP, UDP_PORT] = sock.recvfrom(1024) # buffer size is 1024 bytes
        exibe(data)
        print("received message:", data) 


threads = []

for i in range(10):
    t = threading.Thread(target=receive)
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join() 