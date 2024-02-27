import requests
import pyfiglet
from colorama import Fore,Style,init

logo = pyfiglet.figlet_format("DİRSEARCH")
print(Fore.RED + logo + Style.RESET_ALL)


def search():
    site = input(Fore.GREEN + "Hedef Web Sitesini Girin:" + Style.RESET_ALL)
    liste = 'liste.txt'
    
    with open(liste , 'r',encoding='utf-8') as file:
        dosyalar = file.readlines()
        for dosya in dosyalar:
            ful_url = site + dosya.strip()
            response = requests.get(ful_url)

            if response.ok:
                print(Fore.GREEN + F"\n[✓] Dizin Bulundu-->{ful_url}\n" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Dizin Bulunamadı:-->{ful_url} " + Style.RESET_ALL)

search()