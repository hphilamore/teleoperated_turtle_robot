#!/usr/bin/env python3
# https://realpython.com/python-sockets/
# https://www.explainingcomputers.com/rasp_pi_robotics.html

"""
#----------------------------------------------------------

Tracks hand position in image from web-cam. 

Chooses a command based on hand position.

Sends command to raspberry pi robot over wifi. 

#----------------------------------------------------------
"""


import socket
import socket
import time
import curses

HOST = "192.168.0.100" #"192.168.167.253" # "192.168.0.101" ## "192.168.0.42" #"192.168.167.253"  # The raspberry pi's hostname or IP address
PORT = 65443              # The port used by the server

flag_no_hand = False 

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

command = 'stop'

while(True):
    char = screen.getch()

    # if char == curses.KEY_UP:
    #     print("up")
    #     command = 'forward'
    if char == ord('q'):
        break
    elif char == curses.KEY_UP:
        print("up")
        command = 'forward'
    elif char == curses.KEY_DOWN:
        print("down")
        command = 'backward'
    elif char == curses.KEY_RIGHT:
        print("right")
        command = 'right'
    elif char == curses.KEY_LEFT:
        print("left")
        command = 'left'
    elif char == ord('s'): #10:
        print("stop")
        command = 'stop' 

    # Send command to server socket on raspberry pi
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allow reuse of address
        s.connect((HOST, PORT))
        s.sendall(command.encode())
        # data = s.recv(1024)


# stop the motors
command = 'stop' 
# Send command to server socket on raspberry pi
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allow reuse of address
    s.connect((HOST, PORT))
    s.sendall(command.encode())

#Close down curses properly, inc turn echo back on!
curses.nocbreak(); screen.keypad(0); curses.echo()
curses.endwin()
