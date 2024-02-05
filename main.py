from colorama import Fore
import requests, random, string, threading, os, ctypes

invalid = 0
valid = 0
name_length = input(f"[{Fore.BLUE}~{Fore.WHITE}] Length of the name → ")
os.system("cls" or "clear")

def changeTitleW():
    ctypes.windll.kernel32.SetConsoleTitleW(f"valid → {valid} invalid → {invalid}")

def getName(length: int):
    return ''.join(random.choice(string.ascii_letters + string.ascii_lowercase) for i in range(length))

def CheckName(name):
    global valid, invalid
    resp = requests.get(f"https://mcname.info/en/search?q={name}").text
    if 'Name currently in use' in resp:
        print(f'({Fore.BLUE}⁕{Fore.WHITE}) Name already in use → {name}')
        with open('output/invalid.txt', 'a') as f:
            f.write(name+"\n")
        invalid+=1
        changeTitleW()
        return 'someone already sucked it :C'

    print(f'({Fore.GREEN}✓{Fore.WHITE}) Found a valid name → {name}')
    with open('output/valid.txt', 'a') as f:
        f.write(name+"\n")
    valid+=1
    changeTitleW()
    return 'GG'

if __name__ == "__main__":
    while True:
        if threading.active_count() < 5:
            threading.Thread(target=CheckName, args=(getName(int(name_length)),)).start()