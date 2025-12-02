from colorama import init, Style, Fore
import random
import time
import keyboard

init()

print(f"{Fore.CYAN}escriba bien un numero, osino el programa puede fallar.{Style.RESET_ALL}")
cuantas_ips = int(input("¿Cuántas IPs falsas deseas generar? "))

if cuantas_ips <= 0:
    print(f"{Fore.RED}Por favor, ingresa un número válido mayor que cero.")
    print("vuelva a correr el programa.")
    exit()

if cuantas_ips > 16384:
    print(f"{Fore.RED}Número demasiado grande. Por favor, ingresa un número menor o igual a 16384.")
    print("vuelva a correr el programa.")
    exit()
    
for _ in range(cuantas_ips):
    ip1 = random.randint(0, 255)
    ip2 = random.randint(0, 255)
    ip3 = random.randint(0, 255)
    ip4 = random.randint(0, 255)
    delay = random.uniform(0.02, 0.4)
    print(f"{Fore.GREEN}{ip1}.{ip2}.{ip3}.{ip4}")
    time.sleep(delay)
    if keyboard.is_pressed('esc'):
        print(f"{Fore.RED}Proceso terminado por el usuario.")
        break
    