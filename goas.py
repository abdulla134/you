try:
   import sys
   import os
   import json
   from colorama import Fore,init
   import requests
   from time import sleep
   import pyshorteners
   from twocaptcha import TwoCaptcha
except Exception as F:
    print("[ModuleERROR]%s"%(F),"\n\nWait To Download The Modules It takes 1 or 2 minutes\nBe patient please\nDownloading...\n")
    os.system("pip3 install colorama")
    os.system("pip3 install json")
    os.system("pip3 install requests")
    os.system("pip3 install os")
    os.system("pip3 install sys")
    os.system("pip3 install time")
    os.system("pip3 install TwoCaptcha")
    os.system("pip3 install 2captcha-python")
    os.system("pip3 install pyshorteners")
    pass

os.system("clear")

green_color = "\033[1;32m"
red_color = "\033[1;31m"
detect_color = "\033[1;34m"
banner_color="\033[1;33;40m"
end_banner_color="\33[00m"

#https://2captcha.com/


sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

print(Fore.GREEN+'[*] OS: Unix/Linux/iphone/windows | (root@FaLaH)  ')
print(Fore.CYAN+'''                                                                                                                                         
                                         
 @@@@@@@@   @@@@@@    @@@@@@    @@@@@@   
@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
!@@        @@!  @@@  @@!  @@@  !@@       
!@!        !@!  @!@  !@!  @!@  !@!       
!@! @!@!@  @!@  !@!  @!@!@!@!  !!@@!!    
!!! !!@!!  !@!  !!!  !!!@!!!!   !!@!!!   
:!!   !!:  !!:  !!!  !!:  !!!       !:!  
:!:   !::  :!:  !:!  :!:  !:!      !:!   
 ::: ::::  ::::: ::  ::   :::  :::: ::   
 :: :: :    : :  :    :   : :  :: : :    
                                       

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢒⣩⣥⠡⠀⠀⠀⠀⠌⣬⣍⡒⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠫⣶⣿⣿⣿⣧⡑⢄⡠⢊⣼⣿⣿⣿⣦⠝⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⡅⣿⣦⡙⢿⣿⣿⣿⣦⣴⣿⣿⣿⡿⢋⣴⣿⢨⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⣼⡇⣿⣿⣿⣦⡹⣿⣿⣿⣿⣿⣿⢋⣴⣿⣿⣿⢸⣧⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠗⠛⠻⠿⣿⣷⡘⡿⠟⠻⢿⢃⣾⣿⠿⠟⠛⠺⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⠟⠀⣀⢀⣄⣀⠈⠙⡗⣰⠿⠿⣆⢺⠋⠁⣀⣤⡀⣀⠈⠻⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⢦⣍⡛⠶⣤⠤⠜⣀⣤⠀⣶⣶⠀⣤⣐⠣⢤⣤⠶⢛⣩⡶⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡙⢿⣷⡆⣶⣿⡿⢋⢸⣿⣿⡆⡙⢿⣿⣶⢰⣾⡿⢋⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⠦⣍⠰⣿⡟⣡⣿⢸⣿⣿⡇⣿⡌⢻⣿⠆⣩⠶⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢌⢷⢈⢳⣌⠁⣤⡌⢸⣿⣿⡇⢡⣤⠈⣡⡞⡁⡾⡡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡎⣧⡹⢰⣿⣷⣈⠛⠛⣡⣾⣿⡆⢏⣼⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣿⣇⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⣿⣿⣄⠙⢉⣩⣉⣉⣍⡉⠋⣨⣿⣿⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣄⠻⣿⣿⣷⡆⢀⣀⣀⡀⢰⣾⣿⣿⠟⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣌⠻⢋⡤⠉⠉⠉⠁⣤⡙⠟⣡⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣿⡇⠀⠀⠀⠀⢸⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
print(banner_color+'Photon runs only on Python 3.2 and above')
print(banner_color+"0xfff0800 - FaLaH 2.3v                      ")
print(end_banner_color+'__________________________________________________')
print(end_banner_color+"")
class report:
    def report(self):
        self.session = requests.Session()
        self.contents = open('config.json', 'r',encoding="latin-1",errors='ignore')
        self.data = json.load(self.contents)
        self.API_KEY = self.data['api_key'],self.data['key']
        print('بعد وضع الاميل سوف يتم التاخير في جلب البيانات الرجاء الانتظار')
        self.user = input(Fore.CYAN+'Email $ ')
        solver = TwoCaptcha(self.API_KEY)
        result = solver.recaptcha(sitekey='6LfJtWseAAAAAOR7CTpYOowRpoIN-zNtkJu_m-1z',url='https://tools.epieos.com',invisible=1)
        self.falah = str(result["code"])
        headers = {
'Host': 'tools.epieos.com',
'Cookie': '_pk_id.2.5d8d=9183d62054bd4953.1646032372.; _pk_ses.2.5d8d=1; _ga=GA1.2.502487668.1646032373; _gid=GA1.2.625109150.1646032373;',
'Content-Length': '592',
'Cache-Control':'max-age=0',
'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="98"',
'Sec-Ch-Ua-Mobile': '?0',
'Sec-Ch-Ua-Platform': '"Windows"',
'Upgrade-Insecure-Requests': '1',
'Origin': 'https://tools.epieos.com',
'Content-Type': 'application/json',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
'Accept': '*/*',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Dest': 'document',
'Referer': 'https://tools.epieos.com/?q=test%40gmail.com',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        }
        data ='''
{
    "search":"'''+self.user+'''",
    "captcha":"'''+self.falah+'''"
}
		'''
        url = 'https://tools.epieos.com/api/search'
        response = requests.request('POST', url ,data=data, headers=headers).text
        print(Fore.GREEN+'',response)
        print(red_color+'''
		
		> One more time to check Email {exit : Ctrl + C }
		
		
		''')
           
if __name__ == "__main__":
    while True:
        start = report()
        start.report()