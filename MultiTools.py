import os 
required_imports = [
    'getpass','colorama', 'pypresence'
]

missing_imports = []

for module in required_imports:
    try:
        __import__(module)
    except ImportError:
        missing_imports.append(module)

if missing_imports:
    print("The following required imports are missing and will be installed:")
    for module in missing_imports:
        os.system(f"pip install {module}")
    print("Missing imports installed successfully!")
else:
    print("All required imports are already installed.")
import time
import getpass
user = getpass.getuser()
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import random
from pypresence import Presence

colorama_init()

# {Style.RESET_ALL}
# {Fore.CYAN}

thec = fr"C:\Users\{user}"


t1 = f"{Fore.WHITE}================================="
t2 = f"         {Fore.RED}R B N"
t3 = f"         MultiTools"
t4 = f"{Fore.WHITE}================================={Fore.WHITE}"
t5 = "Sections 1 - 4"
t6 = "1 = File Maker"
t7 = "2 = Discord RPC"
t8 = "3 = Play A Game"
t9 = "4 = print(hello)"
for char in t1:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()
print()
for char in t2:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()
print()
for char in t3:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()
print()
for char in t4:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()
for char in t5:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()
for char in t6:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()
for char in t7:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()
for char in t8:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()
for char in t9:
    print(char, end="", flush=True)
    time.sleep(0.02)
print()    
print()    
print()    
print()    

def start():
    RPC.update(
    state="Using MultiTools By R B N",
    details=f"The User Reading The Tools",
    large_image="1",
    large_text="R B N's Camry",
    small_image="2",
    small_text="Engima"
    )
    sc = input("section?: ")
    try:
        scn = int(sc)

        print(f"Ok. Section: {scn}\n\n")
        return scn
    except ValueError:
        print("Numbers Only")
        return None


def file(thec):
    pathh = input("Path?: ")
    FileName = input("Soo The File Name?: ")
    user = getpass.getuser()

    if pathh.startswith(thec):
        os.makedirs(f"{pathh}/{FileName}", exist_ok=True)
    else:
        os.makedirs(f"C:\\Users\\{user}\\{pathh}\\{FileName}", exist_ok=True)

def hi():
    iad = input("Bot Id: ")
    RPC = Presence(iad)
    RPC.connect()
    s = input("State: ")
    d = input("Details: ")
    l = input("Large Image: ")
    lt = input("Large Text: ")
    si = input("Small Image: ")
    st = input("Small Text: ")
    RPC.update(
    state=s,
    details=d,
    large_image=l,
    large_text=lt,
    small_image=si,
    small_text=st
    )
    print(f"{Fore.RED}Ctrl + C To Close And Stops RPC{Fore.WHITE}")
    while True:
        pass
def hoi():
    tx = f"{Fore.WHITE}The Game Will Be {Fore.CYAN} Guess The Number 1 - 5 {Fore.WHITE} IF It's Wrong Ur Pc Will {Fore.RED}ShutDown {Fore.WHITE}"
    for char in tx:
        print(char, end="", flush=True)
    time.sleep(0.02)
    print()
    r = random.randint(1,5)
    g = input("You're Guess?: ")
    ga = int(g)
    if ga != r:
        os.system("shutdown /s /t 1")
    

def hello():
    print("hello")


if __name__ == "__main__":
    RPC = Presence(1362297930404335717)
    RPC.connect()
    RPC.update(
    state="Using MultiTools By R B N",
    details=f"The User Reading The Tools",
    large_image="1",
    large_text="R B N's Camry",
    small_image="2",
    small_text="Engima"
    )
    while True:
        section_result = start()
        if section_result == 1:
            RPC.update(
            state="Using MultiTools By R B N",
            details=f"The User Using FileMaker",
            large_image="1",
            large_text="R B N's Camry",
            small_image="2",
            small_text="Engima"
            )
            file(thec)
        elif section_result == 2:
            RPC.update(
            state="Using MultiTools By R B N",
            details=f"The User Editing Discord RPC",
            large_image="1",
            large_text="R B N's Camry",
            small_image="2",
            small_text="Engima"
            )
            print("Just Wait 5 Sec")
            time.sleep(5)
            RPC.close()
            hi()
        elif section_result == 3:
            RPC.update(
            state="Using MultiTools By R B N",
            details=f"The User Using Play A Game",
            large_image="1",
            large_text="R B N's Camry",
            small_image="2",
            small_text="Engima"
            )
            hoi()
        elif section_result == 4:
            RPC.update(
            state="Using MultiTools By R B N",
            details=f"Saying Hello To User",
            large_image="1",
            large_text="R B N's Camry",
            small_image="2",
            small_text="Engima"
            )
            hello()
        elif section_result is None:
            pass
        else:
            print("Bro Just Cohice 1 - 4 ...")


        continue_program = input(f"\n\nAnother Section? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}): ").lower()
        if continue_program != 'y':
            break
