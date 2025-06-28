import time 
import os 
import locale

locale.setlocale(locale.LC_TIME,"pt_BR.UTF-8")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    dia = time.strftime("%A, %D ,%H:%M:%S")
    time.sleep(1)
    limpar_tela()
    print(dia)
    
    