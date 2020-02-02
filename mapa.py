import socket
from threading import Thread
import os
import matplotlib.pyplot as plt
from matplotlib import interactive
from vpython import *




box(pos=vector(-50,-3.5,0),
        size=vector(5.5,1.5,1.6),
        color=color.red)

box(pos=vector(0, 0, 0),
    size=vector(100, 10, 0), 
    color = color.gray(2))

box(pos=vector(0, 0, 0),
    size=vector(10, 100, 0), 
    color = color.gray(2))

box(pos=vector(25, 25, 0),
    size=vector(45, 50, 0), 
    color = color.green)

#box(pos=vector(0, 50, 0),
 #   size=vector(50, 50, 0), 
  #  color = color.green)

def carro():
    box(pos=(-500, -50, 0),
        size=(15.5,7.6,6.6),
        color=color.red)



def receive():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        exibe(data)
        print("received message:", data) 

def exibe(data):
    message = data.split("/")
    
    carro = message[0]
    pos_x = message[1] 
    pos_y = message[2]

    plt.scatter(pos_x, pos_y, s=10, color='yellow')
    plt.text(pos_x+0.3, pos_y, carro, fontsize=9)

def plot_map(): 
    plt.plot(4.5, 0, color='grey')
    plt.plot(5.5, 0, color='grey')
    plt.plot(0, 4.5, color='grey')     
    plt.plot(0, 5.5, color='grey')
 

threads = []

for i in range(10):
    t = threading.Thread(target=receive)
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join() 