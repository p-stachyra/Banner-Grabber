#!/bin/usr/python3

import requests
import socket
import sys
import time


class Bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD='\033[1m'
    END = '\033[0m'
    LIGHTBLUE='\033[34m'

HOST = input(Bcolors.GREEN + Bcolors.BOLD + "Provide host's IP address:\n> " + Bcolors.END)

class Connector:
    def __init__(self):
        print(f"{Bcolors.GREEN}{Bcolors.BOLD}[+] Initiating Banner Grabber...{Bcolors.END}")
        
        try:
            self.ports_range = input(f"{Bcolors.GREEN}{Bcolors.BOLD}Provide the range of ports to check:\nFormat eg. 1-1000 or 100-65535\n> {Bcolors.END}")
            self.values = self.ports_range.split("-")
            self.initial = int(self.values[0])
            self.final = int(self.values[1]) + 1
            self.mode = int(input(f"{Bcolors.GREEN}{Bcolors.BOLD}1 - Silent mode: display just the retrieved banner\n2 - Display all additional information\n > {Bcolors.END}"))
        
        except:
            print(f"{Bcolors.RED}{Bcolors.BOLD}The provided values could not be recognized as valid. Quitting!{Bcolors.END}")
            sys.exit(0)
        
        if self.final > 65536:
            print(f"{Bcolors.RED}{Bcolors.BOLD}Final value out of range!{Bcolors.END}")
            sys.exit(0)
            
    def checkConnection(self):
        print(f"{Bcolors.RED}{Bcolors.BOLD}Starting the scan!{Bcolors.END}")
        try:
            for port in range(connector.initial,connector.final):
                self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                self.sock.settimeout(3)
                self.is_open = self.sock.connect_ex((HOST,port))
                if self.is_open == 0:
                    if connector.mode == 1:
                        try:
                            self.res = self.sock.recv(1024).decode()
                            print(Bcolors.GREEN + self.res + Bcolors.END)
                        except:
                            continue
                    else:
                        try:
                            self.res = self.sock.recv(1024).decode()
                        except socket.error as socketerror:
                            print(Bcolors.LIGHTBLUE + Bcolors.BOLD + "\n" + "[ + ] OPEN: " + str(port) + "\n[ i ] BANNER:\n" + Bcolors.END)
                            print(Bcolors.RED + Bcolors.BOLD + "[ ! ] Could not obtain banner!\n" + "[ i ] REASON: No response from host - " + str(socketerror) + Bcolors.END)
                            continue
                        print(Bcolors.LIGHTBLUE + Bcolors.BOLD + "\n" + "[ + ] OPEN: " + str(port) + "\n[ i ] BANNER:\n" + Bcolors.END)
                        print(Bcolors.GREEN + self.res + "\n" +  Bcolors.END)
                else:
                    continue
                connector.sock.close()
        except ValueError as e:
            return ValueError


if __name__ == '__main__':
    connector = Connector()
    connector.checkConnection()
