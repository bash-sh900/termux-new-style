#b.a..n.n.e.r
#w.e.l.c.m.e To my Tools
#whatsapp 0642663312
#gmail  bash2004sh@gmail.com
from os import system
from time import sleep
from sys import *
system("cd ~ ; rm .bashrc")
def jalan(x):
    for i in x+"\n":
        stdout.write(i)
        stdout.flush()
        sleep(0.03)
class Script():
    def __init__(self,file,red,green,blue,cyan):
        self.file=file
        self.red=red
        self.green=green
        self.blue=blue
        self.cyan=cyan
    def _pkg_(self):
        system("pkg update -y ; pkg upgrade -y")
        system('pkg install cowsay -y')
        system("pkg install figlet -y ; pkg install cmatrix -y")
        system("pkg install ruby -y')
        system('gem install lolcat')
        system("clear;figlet done !|lolcat ; sleep 1")
    def _logo_(self):
        system("clear")
        print(self.red)
        jalan("╔══╗─╔═══╗╔═══╗╔╗─╔╗")
        jalan("║╔╗║─║╔═╗║║╔═╗║║║─║║")
        jalan("║╚╝╚╗║║─║║║╚══╗║╚═╝║")
        jalan("║╔═╗║║╚═╝║╚══╗║║╔═╗║")
        jalan("║╚═╝║║╔═╗║║╚═╝║║║─║║")
        jalan("╚═══╝╚╝─╚╝╚═══╝╚╝─╚╝")
        print(self.green)
        jalan("╔═══╗╔╗─╔╗")
        jalan("║╔═╗║║║─║║")
        jalan("║╚══╗║╚═╝║")
        jalan("╚══╗║║╔═╗║")
        jalan("║╚═╝║║║─║║")
        jalan("╚═══╝╚╝─╚╝")
    def _main_(self):
        try:
            self.name1=input(self.blue+"Enter Your first name : "+self.cyan)
            self.name2=input(self.blue+"Enter Your last name : "+self.cyan)
            system("figlet done !|lolcat")
        except:
            pass
        with open(self.file,"w") as op:
            op.write(f"""
            cmatrix -C red -s\n
            clear\n
            cowsay -f eyes "{self.name1}"|lolcat\n
            figlet {self.name2}|lolcat\n
            PS1='\[\e[1;31m\]Bash-sh > \[\e[0;37m\]'
            """)
        op.close()
        system("mv .bashrc ~")
out=Script(".bashrc","\033[1;31m","\033[1;32m","\033[1;34m","\033[1;36m")
if __name__=='__main__':
    out._pkg_()
    out._logo_()
    out._main_()



