import os
import compileall
import socket
import time
from datetime import *


def main():
    print('''\033[0;31m          ___  ___   _   _       ___       ___  ___       ___   _____  
    \033[0;31m     /   |/   | | | | |     /   |     /   |/   |     /   | |  _  \ 
    \033[0;31m    / /|   /| | | |_| |    / /| |    / /|   /| |    / /| | | | | | 
    \033[0;31m   / / |__/ | | |  _  |   / / | |   / / |__/ | |   / / | | | | | | 
    \033[0;31m  / /       | | | | | |  / /  | |  / /       | |  / /  | | | |_| | 
    \033[0;31m /_/        |_| |_| |_| /_/   |_| /_/        |_| /_/   |_| |_____/  \033[0;34m Muhamad ''')
    L12x = input("Enter Password :-")
    if L12x == '1234':
        def l0x():
            os.system('clear')
            os.system('figlet HAMA')
            print(' Welcome To My Python Script ')
            print("encoding      [1]")
            print("age checker   [2]")
            print("Web Ip Getter [3]")
            ch = input("Chose Number ===>")
#############################################################
            if ch == '1':
                os.system("toilet -f big 'encoding' -F gay")
                compileall.compile_dir(input("Type Your Folder Path : "))
                print("Press Enter for Restart")
                hama = input("")
                if hama == "":
                    l0x()
#############################################################
            elif ch == '2':
                print("Enter Your Birth Year")
                DOB=datetime.strptime(input("Enter Your Birth day −−−>"), "%Y")
                def calculate_age(born):
                    today = date.today()
                    return today.year - born.year
                age = calculate_age(DOB)
                print(age, "Year's Old")
                if age <= 19:
                   print("Small Age")
                elif age <= 39:
                    print('Middle Age')
                else:
                    print("you're So Old")
                    print("Press Enter for Restart")
                    wii = input("")
                    if wii == "":
                        l0x()
    #############################################################
            elif ch == '3':
                os.system("toilet -f big 'IP GETTER' -F gay")
                os.system("figlet Muhamad")
                print("Enter The WebAddress:- ")
                hostname = input()
                ip = socket.gethostbyname(hostname)
                print('Host Name is:- ', hostname, '\n' 'The Web IP is:- ', ip)
                print("Press Enter for Restart")
                wii = input("")
                if wii == "":
                    l0x()
#############################################################
            else:
                print("Please Chose Number Between 1-3")
                print("Press Enter for Restart")
                wii = input("")
                if wii == "":
                    l0x()
##############################################################

        l0x()
    else:
        print("Wrong Password Try Again   :(")
        print("Press Enter for Restart")
        restart = input("")
        if restart == "":
            main()


main()
