#!/bin/usr/python3

import socket
import sys
import time


class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD='\033[1m'
    END = '\033[0m'
    LIGHTBLUE='\033[34m'

HOST = input(Colors.GREEN + Colors.BOLD + "Provide host's IP address:\n> " + Colors.END)

class Connector:
    def __init__(self):
        print(f"{Colors.GREEN}{Colors.BOLD}[+] Initiating Banner Grabber...{Colors.END}")

        try:
            self.ports_range = input(f"{Colors.GREEN}{Colors.BOLD}Provide the range of ports to check:\nFormat eg. 1-1000 or 100-65535\n> {Colors.END}")
            self.values = self.ports_range.split("-")
            self.initial = int(self.values[0])
            self.final = int(self.values[1]) + 1
            self.mode = int(input(f"{Colors.GREEN}{Colors.BOLD}1 - Silent mode: display just the retrieved banner\n2 - Display all additional information\n > {Colors.END}"))

        except:
            print(f"{Colors.RED}{Colors.BOLD}The provided values could not be recognized as valid. Quitting!{Colors.END}")
            sys.exit(0)

        if self.final > 65536:
            print(f"{Colors.RED}{Colors.BOLD}Final value out of range!{Colors.END}")
            sys.exit(0)

    def checkConnection(self):
        print(f"{Colors.RED}{Colors.BOLD}Starting the scan!{Colors.END}")
        try:
            for port in range(connector.initial,connector.final):
                self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                self.sock.settimeout(3)
                self.is_open = self.sock.connect_ex((HOST,port))
                if self.is_open == 0:
                    if connector.mode == 1:
                        try:
                            self.res = self.sock.recv(1024).decode()
                            print(Colors.GREEN + self.res + Colors.END)
                        except:
                            continue
                    else:
                        try:
                            self.res = self.sock.recv(1024).decode()
                        except socket.error as socketerror:
                            print(Colors.LIGHTBLUE + Colors.BOLD + "\n" + "[ + ] OPEN: " + str(port) + "\n[ i ] BANNER:\n" + Colors.END)
                            print(Colors.RED + Colors.BOLD + "[ ! ] Could not obtain banner!\n" + "[ i ] REASON: No response from host - " + str(socketerror) + Colors.END)
                            continue
                        print(Colors.LIGHTBLUE + Colors.BOLD + "\n" + "[ + ] OPEN: " + str(port) + "\n[ i ] BANNER:\n" + Colors.END)
                        print(Colors.GREEN + self.res + "\n" +  Colors.END)
                else:
                    continue
                connector.sock.close()
        except ValueError as e:
            return ValueError


if __name__ == '__main__':
    connector = Connector()
    connector.checkConnection()
