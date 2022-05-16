import time
import os
import random
from colorama import init, Fore
import webbrowser

init()

reklamaImage = ["family_hairdress.jpg", "pornhub.jpg", "hren.jpg", "oldSpice.jpg", "leather.jpg"]
reklamaURl = ["https://haircutexpress.eu/ru/", "https://rt.pornhub.com", "https://abcfood.net/ru/product-category/hren-gorchica/hren/", "https://oldspice.com/", "https://www.tavro-kozha.ru/catalog/all/"]

x = 1

while True:
	os.system('cls||clear')

	y = x % 5

	x += 1

	if y == 0:
		rIndex = random.randrange(5)

		#получение дериктории с кодом и подальшей обработкой

		direcrory = os.path.abspath(__file__)
		imageDir = direcrory.replace( 'main.py', "images\\" )
		reklamaImg = imageDir + reklamaImage[rIndex]

		os.startfile( reklamaImg )

		print("5...")
		time.sleep(1)
		print("4...")
		time.sleep(1)
		print("3...")
		time.sleep(1)
		print("2...")
		time.sleep(1)
		print("1...")
		time.sleep(1)
		os.system('cls||clear')

		print('\n\n       1-skip           2-перейти')
		try:
			reklamaInput = int(input("\n\n       Сделай выбор: "))
		except:
			print("Ты даун ЕБУЧИЙ")

		while True:
			if reklamaInput == 1:
				break
			elif reklamaInput == 2:
				webbrowser.open(reklamaURl[rIndex], new=0, autoraise = False)
				input()
				break
			else:
				print("ТЫ ДАУН ЕБУЧИЙ")
				continue
		

	else:
		print(Fore.RED, '\n\n\n     ██╗  ███████╗██╗░░░██╗░█████╗░██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗██████╗░')
		time.sleep(0.2)
		print(Fore.GREEN,'    ██║  ██╔════╝██║░░░██║██╔══██╗██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║██╔══██╗')
		time.sleep(0.2)
		print(Fore.YELLOW,'    ██║  █████╗░░██║░░░██║██║░░╚═╝█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║██████╔╝')
		time.sleep(0.2)
		print(Fore.BLUE,'    ██║  █████╗░░██║░░░██║██║░░╚═╝█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║██████╔╝')
		time.sleep(0.2)
		print(Fore.MAGENTA,'    ██║  █████╗░░██║░░░██║██║░░╚═╝█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║██████╔╝')
		time.sleep(0.2)
		print(Fore.CYAN,'    ██║  █████╗░░██║░░░██║██║░░╚═╝█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║██████╔╝')
		time.sleep(0.2)
		print(Fore.RESET,'    ██║  █████╗░░██║░░░██║██║░░╚═╝█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║██████╔╝')
		time.sleep(0.2)
		print(Fore.RED,'    ██║  ██║░░░░░╚██████╔╝╚█████╔╝██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝██║░░██║')
		time.sleep(0.2)
		print(Fore.GREEN,'    ╚═╝  ╚═╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝')
		time.sleep(0.2)
		print('')
		time.sleep(0.2)
		print(Fore.YELLOW,'    ░██████╗████████╗███████╗██████╗░██████╗░░█████╗░██████╗░')
		time.sleep(0.2)
		print(Fore.BLUE,'    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗')
		time.sleep(0.2)
		print(Fore.MAGENTA,'    ╚█████╗░░░░██║░░░█████╗░░██████╔╝██║░░██║███████║██║░░██║')
		time.sleep(0.2)
		print(Fore.CYAN,'    ░╚═══██╗░░░██║░░░██╔══╝░░██╔═══╝░██║░░██║██╔══██║██║░░██║')
		time.sleep(0.2)
		print(Fore.RESET,'    ██████╔╝░░░██║░░░███████╗██║░░░░░██████╔╝██║░░██║██████╔╝')
		time.sleep(0.2)
		print(Fore.RED,'    ╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═════╝░╚═╝░░╚═╝╚═════╝░')
		time.sleep(2)