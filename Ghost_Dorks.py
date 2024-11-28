import os
import sys
import random
import requests
import re

W = "\033[0m"
G = "\033[92m"
R = "\033[91m"
Y = "\033[93m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"

class Dorker:
    def display_banner(self):
        banner = f'''
{R}
 ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗    ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗
██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝
██║  ███╗███████║██║   ██║███████╗   ██║       ██║  ██║██║   ██║██████╔╝█████╔╝ ███████╗
██║   ██║██╔══██║██║   ██║╚════██║   ██║       ██║  ██║██║   ██║██╔══██╗██╔═██╗ ╚════██║
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║       ██████╔╝╚██████╔╝██║  ██║██║  ██╗███████║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
⭐⭐⭐⭐⭐ {G}Ghost Dork{W} - {Y}Dorking Made Simple{W} || {BOLD}{CYAN}Author: Ghost Sec & Ghost Yemen{W} ⭐⭐⭐⭐⭐
        '''
        print(banner)

    def run(self):
        self.display_banner()
        print('   %s[%s1%s] Single Dork\n   %s[%s2%s] Dorks File' % (W, G, W, W, G, W))
        choice = input(f'\n{W}[{R}?{W}] Choose mode (1 for Single Dork, 2 for File): ')

        if choice == '1':
            self.dork = input('%s[%s?%s] Enter single dork: ' % (W, G, W))
            print()
            self.dorker(self.dork)
            self.filter_results()
            
        elif choice == '2':
            self.file = input('%s[%s?%s] Enter file path with dorks: ' % (W, G, W))
            try:
                with open(self.file, 'r') as f:
                    for self.dork in f.read().splitlines():
                        print('\n%s[%s!%s] %sDorking %s%s\n' % (W, Y, W, Y, self.dork, W))
                        self.dorker(self.dork)
                self.filter_results()
            except IOError:
                print('%s[%s×%s] File does not exist' % (W, R, W))
        else:
            exit('Invalid choice, exiting.')

    def dorker(self, search):
        liste = []
        page = 0
        while True:
            page += 10
            get_token = requests.get(
                'https://cse.google.com/cse.js?cx=partner-pub-2698861478625135:3033704849',
                headers={
                    'Referer': 'https://cse.google.com/cse?cx=partner-pub-2698861478625135:3033704849',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                                  '(KHTML, like Gecko) Chrome/69.0.' + str(random.randint(0, 3333)) + '.100 Safari/537.36'
                }
            ).text
            cse_token = re.findall(r'"cse_token": "(.*?)"', get_token)
            ngedork = requests.get(
                'https://cse.google.com/cse/element/v1?num=10&hl=en&cx=partner-pub-2698861478625135:3033704849'
                '&safe=off&cse_tok=%s&start=%s&q=%s&callback=x' % (cse_token[0], page, search),
                headers={
                    'Referer': 'https://cse.google.com/cse?cx=partner-pub-2698861478625135:3033704849',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                                  '(KHTML, like Gecko) Chrome/69.0.' + str(random.randint(0, 3333)) + '.100 Safari/537.36'
                }
            ).text
            results = re.findall(r'"unescapedUrl": "(.*?)"', ngedork)
            if results == []:
                break
            for url in results:
                dhon = url
                url = url.replace("https://", "").replace("http://", "").replace("www.", "")
                url = url.split("/")[0]
                if url not in liste:
                    liste.append(url)
                    print(f'{BOLD}{CYAN}{url}{W} ✅')
                    open('.dork', 'a+').write(dhon + '\n')

    def filter_results(self):
        print('\n%s[%s*%s] Result filter menu\n\n    %s[%s1%s] Full path\n    %s[%s2%s] Just domain' % (W, R, W, W, G, W, W, G, W))
        self.chc = input('\n%s[%s?%s] Choice : ' % (W, R, W))
        if self.chc == '1':
            self.podo('.dork')
            os.system('rm -rf .p && rm -rf .dork')
        elif self.chc == '2':
            self.get_domain()
            self.podo('.p')
            os.system('rm -rf .p && rm -rf .dork')
            lists = 'results.txt'
            url = open(lists, 'r').readlines()
            readsplit = open(lists).read().splitlines()
            self.giti(readsplit, url)
        else:
            self.podo('.dork')
            os.system('rm -rf .p && rm -rf .dork')
            exit('\n%s[%s✓%s] Done, saved in results.txt' % (W, G, W))

    def get_domain(self):
        for site in open('.dork').read().splitlines():
            try:
                _p = site.split('/')[0] + '//' + site.split('/')[2]
                open('.p', 'a+').write(_p + '\n')
            except:
                continue

    def podo(self, file):
        podo = []
        for site_ in open(file).read().splitlines():
            try:
                if any(x in site_ for x in ['pastebin', 'microsoft', 'exploit-db', 'wordpress.org', 'medium', 
                                            'packetstormsecurity', 'pinterest', 'facebook', 'youtube', 
                                            'wordfence', 'debian', 'bitnami', 'github', 'cxsecurity', 
                                            'reddit', 'portswigger', 'acunetix', 'slideshare', 
                                            'cvedetails', 'jetpack', 'stackoverflow', 'twitter']):
                    continue
                else:
                    podo.append(site_)
                    open('results.txt', 'a+').write(site_ + '\n')
            except:
                continue

if __name__ == "__main__":
    dorker = Dorker()
    dorker.run()
