from colorama import Fore, Style, init
import time
import keyboard
init()

print("tu")
time.sleep(1)
print(Style.DIM + Fore.RED + "tu")
time.sleep(1)
print(Style.DIM + Fore.RED + "TU")
time.sleep(1)
print(Style.DIM + Fore.RED + "ME MATASTE")
time.sleep(1)
print(Style.BRIGHT + Fore.RED + "ME MATASTE")
time.sleep(1)
for i in range(10):
    print(Style.BRIGHT + Fore.RED + "ME MATASTE")
    time.sleep(0.5)
time.sleep(1)
print(f"{Style.RESET_ALL}te mereces {Style.BRIGHT + Fore.RED}EL INFIERNO")
print(Style.RESET_ALL + "para ¿eras vos?")
print(f"{Style.RESET_ALL}si=tecla s /{Style.BRIGHT + Fore.RED} no=tecla n")
while True: 
    if keyboard.is_pressed('s'):
        print("bienvenido al infierno")
        time.sleep(1)
        print(Style.BRIGHT + Fore.RED + "🔥🔥🔥🔥🔥🔥🔥🔥")
        time.sleep(1)
        print("CHQERGR RA RY VASVREAB")
        break
    elif keyboard.is_pressed('n'):
        print(Style.RESET_ALL + "bueno, me confundi de persona")
        time.sleep(1)
        print("era un tal claudio dobniewski")
        break