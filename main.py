import subprocess
import sys
import os

def ejecutar_script(nombre_archivo):
    """Función que usa subprocess para ejecutar el archivo dado y verifica su existencia."""
    
    # 1. Construir la ruta absoluta para el diagnóstico
    ruta_completa = os.path.join(os.getcwd(), nombre_archivo)
    
    # 2. Verificar si el archivo existe
    if not os.path.exists(ruta_completa):
        print(f"--- ERROR: ¡Archivo NO ENCONTRADO! ---")
        print(f"Buscando en: {ruta_completa}")
        print(f"Asegúrate de que '{nombre_archivo}' existe dentro de tu directorio de trabajo actual.")
        return # Termina la función si no se encuentra
        
    print(f"\n--- Iniciando '{nombre_archivo}' (Ruta: {ruta_completa}) ---")
    
    try:
        # Usa la ruta relativa y cwd=os.getcwd() para ejecutar
        subprocess.run([sys.executable, nombre_archivo], check=True, cwd=os.getcwd())
        print(f"--- '{nombre_archivo}' finalizado correctamente ---\n")
    except subprocess.CalledProcessError as e:
        print(f"--- ERROR: '{nombre_archivo}' falló. Código de salida: {e.returncode} ---\n")
    except Exception as e:
        print(f"--- ERROR Inesperado durante la ejecución: {e} ---\n")

print("1. hakeo falso 2.colores turbios 3. nose XD 4 cursor desapareciente 5.salir")
opcion_input = input("Que archivo deseas ejecutar? ")

try:
    opcion = int(opcion_input) # Intenta convertir la entrada a un número entero
except ValueError:
    print("Entrada no válida. Por favor, ingresa un número.")
    sys.exit()

if opcion == 1:
    ejecutar_script("hakeo falso/main.py")
elif opcion == 2:
    ejecutar_script("colores y cosas turbias/main.py")
elif opcion == 3:
    ejecutar_script("no se XD/main.py")
elif opcion == 4:
    ejecutar_script("cursor desapareciente/main.py")
elif opcion == 5:
    print("Saliendo del programa.")
    sys.exit()
else:
    print("Opción fuera de rango. Por favor, selecciona un número del 1 al 5.")