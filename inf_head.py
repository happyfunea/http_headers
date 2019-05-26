#!/usr/bin/python
#-*- coding:utf -8-*-

import requests
from subprocess import call
from multiprocessing import Process
from color import colors

class infoUrl:
    def __init__(self):
        self.typeng = str
    
    @property
    def prop(self):
        return self.typeng

    @prop.setter
    def prop(self, url):
        self.typeng = url
        #single url

class main:
    #staticmethod
    def single_pars(self,ar):
        try:
            self.gets_inf = requests.get(ar)
            if self.gets_inf.status_code == 200:
                print (f'{colors.colorku().magenta}----------------------------------')
                print (f'{colors.colorku().normal}[!]Get Headers Form: {colors.colorku().red}{ar}')
                print (f'{colors.colorku().magenta}----------------------------------')
                for c in self.gets_inf.headers:
                    if self.gets_inf.status_code == 200:
                        print (f'{colors.colorku().under} |_{c}: {colors.colorku().yellow}{self.gets_inf.headers[c]}')
                    else:
                        pass
        except requests.exceptions.MissingSchema:
            print (f'http://{ar} [BAD]')
            exit()

    #@staticmethod
    def mas_pars(self, arg):
        try:
            self.gets_inf = requests.get(arg)
            if self.gets_inf.status_code == 200:
                print (f'{colors.colorku().magenta}-----------------------------------')
                print(f'{colors.colorku().normal}[!]Get Headers From: {colors.colorku().red}{arg}')
                print (f'{colors.colorku().magenta}-----------------------------------')
            elif self.gets_inf.status_code != 200:
                pass
            else:
                pass
            for m in self.gets_inf.headers:
                if self.gets_inf.status_code == 200:
                    print (f'{colors.colorku().under} |_[**]{m}: {colors.colorku().yellow}{self.gets_inf.headers[m]}')
                else:
                    pass
        except requests.exceptions.MissingSchema:
            print (f'http://{arg} is [BAD]')
            pass

    #@staticmethod
    def thread(self, *args):
        try:
            with open(y,'r') as sebagai:
                self.red = sebagai.readlines()
                self.x = []
                for x in self.red:
                    self.lines = x.strip()
                    self.proc = Process(target=main().mas_pars, args=(self.lines,))
                    self.x.append(self.proc)
                    self.proc.start()
                    self.proc.join()
        except FileNotFoundError as er:
            print (f'{colors.colorku().green}[!]{colors.colorku().red} {er}')
            exit()

if __name__=='__main__':
    recursiv = lambda : f'''{colors.colorku().green}
██╗███╗   ██╗███████╗    █████╗ ███████╗██╗    ██╗
██║████╗  ██║██╔════╝   ██╔══██╗██╔════╝██║    ██║
██║██╔██╗ ██║█████╗     ███████║███████╗██║ █╗ ██║
██║██║╚██╗██║██╔══╝     ██╔══██║╚════██║██║███╗██║
██║██║ ╚████║██║███████╗██║  ██║███████║╚███╔███╔╝
╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ {colors.colorku().under}V.asw_aswan.1
{colors.colorku().under}--{colors.colorku().green}Author{colors.colorku().under}:{colors.colorku().green} Agung_sp{colors.colorku().under}--
{colors.colorku().under}[x]{colors.colorku().green}Information_Http_Headers{colors.colorku().under}[x]{colors.colorku().normal}

1. get single http_headers?
2. mass get http_headers?
3. exit


        '''
    thx_inf = True
    call(['clear'],shell=thx_inf)
    print (recursiv())
    while thx_inf:
        asker = input(f'{colors.colorku().normal}[*]choose: ')
        if asker == '1':
            fck = input('[Url]: ')
            url = infoUrl().prop(fck)
            main().single_pars(url)
            ask = input(f'{colors.colorku().normal}[!] [B]ack to menu {colors.colorku().red}(or){colors.colorku().normal} [E]xit: ').lower()
            if ask in 'b':
                call(['clear'], shell=thx_inf)
                print (recursiv())
            if ask != 'b':
                print (f'{colors.colorku().normal}[!] exit..')
                exit()
        elif asker == '2':
            y = input('[Path Url]: ')
            main().thread(y)
            ask = input(f'{colors.colorku().normal}[!] [B]ack to menu {colors.colorku().red}(or){colors.colorku().normal} [E]xit: ')
            if ask in 'b':
                call(['clear'],shell=True)
                print (recursiv())
            elif ask == 'e':
                print (f'{colors.colorku().normal}[!] exit..')
                exit()
            else:
                pass
        elif asker == '3':
            print (f'{colors.colorku().normal}[!] exit..')
            exit()
        else:
            print (f'{colors.colorku().normal}[!]{colors.colorku().red}the your put is not understand...')

