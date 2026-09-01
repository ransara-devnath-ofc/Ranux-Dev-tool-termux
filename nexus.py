import os
import sys
import time
import socket
import platform
import requests
import phonenumbers
from phonenumbers import geocoder, carrier
from colorama import Fore, Style, init

init(autoreset=True)

class C:
    C = Fore.CYAN
    G = Fore.LIGHTGREEN_EX
    R = Fore.LIGHTRED_EX
    Y = Fore.YELLOW
    W = Fore.WHITE
    M = Fore.MAGENTA
    B = Fore.LIGHTBLUE_EX
    X = Style.RESET_ALL

def type_text(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def rainbow_banner():
    art = """
  _   _  ______ __  __ _    _  _____ 
 | \ | ||  ____|\ \/ /| |  | |/ ____|
 |  \| || |__    \  / | |  | | (___  
 | . ` ||  __|   /  \ | |  | |\___ \ 
 | |\  || |____ / /\ \| |__| |____) |
 |_| \_||______/_/  \_\\\\____/|_____/ 
    """
    colors = [C.R, C.Y, C.G, C.C, C.B, C.M]
    lines = art.split("\n")
    for i, line in enumerate(lines):
        print(colors[i % len(colors)] + line)
    print(C.X)

def spinner(dur, msg):
    chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end = time.time() + dur
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r{C.C}[{chars[i]}] {C.W}{msg}")
        sys.stdout.flush()
        i = (i + 1) % len(chars)
        time.sleep(0.1)
    sys.stdout.write(f"\r{C.G}[✔] {msg} - Done!      \n")
    sys.stdout.flush()

def boot():
    os.system('clear' if os.name == 'posix' else 'cls')
    type_text(f"{C.G}[+] Starting System...")
    type_text(f"{C.G}[+] Loading Modules...")
    spinner(2, "Connecting to Network")
    time.sleep(0.5)

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def header():
    os.system('clear' if os.name == 'posix' else 'cls')
    rainbow_banner()
    print(f"{C.C}╭──────────────────────────────────────────╮")
    print(f"{C.C}│ {C.Y}👑 DEVELOPER : RANUX DEV                 {C.C}│")
    print(f"{C.C}├──────────────────────────────────────────┤")
    print(f"{C.C}│ {C.G}STATUS  : {C.W}ACTIVE                       {C.C}│")
    print(f"{C.C}│ {C.G}HOST IP : {C.W}{get_ip():<26} {C.C}│")
    print(f"{C.C}│ {C.G}SYSTEM  : {C.W}{platform.system()[:26]:<26} {C.C}│")
    print(f"{C.C}╰──────────────────────────────────────────╯\n")

def mod_domain():
    header()
    print(f"{C.C}╭───〔 𝗗𝗼𝗺𝗮𝗶𝗻 𝗥𝗲𝗰𝗼𝗻𝗻𝗮𝗶𝘀𝘀𝗮𝗻𝗰𝗲 〕")
    target = input(f"{C.C}│\n╰──► {C.Y}Enter Web Domain: {C.W}").strip()
    if not target:
        return
    print(f"\n{C.G}[+] Target: {target}")
    spinner(2, "Finding web data")
    subs = set()
    try:
        res = requests.get(f"https://api.hackertarget.com/hostsearch/?q={target}", timeout=10)
        if res.status_code == 200 and "error" not in res.text.lower():
            for line in res.text.split('\n'):
                if ',' in line:
                    sub = line.split(',')[0].strip().lower()
                    if sub and '*' not in sub:
                        subs.add(sub)
    except Exception:
        pass
    try:
        res = requests.get(f"https://crt.sh/?q=%.{target}&output=json", timeout=10)
        if res.status_code == 200:
            for item in res.json():
                for sub in item.get('name_value', '').split('\n'):
                    sub = sub.strip().lower()
                    if sub and '*' not in sub:
                        subs.add(sub)
    except Exception:
        pass
    print(f"\n{C.C}╭───〔 𝗥𝗲𝘀𝘂𝗹𝘁𝘀 〕")
    if subs:
        sub_list = sorted(list(subs))
        for s in sub_list[:15]:
            print(f"{C.C}├─ {C.W}{s}")
        if len(sub_list) > 15:
            print(f"{C.C}├─ {C.Y}And {len(sub_list) - 15} more...")
    else:
        print(f"{C.C}├─ {C.R}Nothing found")
    print(f"{C.C}╰────────────────────────────")
    input(f"\n{C.Y}Press ENTER to go back...")

def mod_network():
    header()
    print(f"{C.C}╭───〔 𝗧𝗮𝗰𝘁𝗶𝗰𝗮𝗹 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 𝗔𝗻𝗮𝗹𝘆𝘇𝗲𝗿 〕")
    target = input(f"{C.C}│\n╰──► {C.Y}Enter IP Address: {C.W}").strip()
    if not target:
        return
    print(f"\n{C.G}[+] Scanning Network...")
    ports = [21, 22, 23, 53, 80, 443, 8080]
    print(f"\n{C.C}╭───〔 𝗦𝗰𝗮𝗻 𝗥𝗲𝘀𝘂𝗹𝘁𝘀 〕")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((target, port)) == 0:
                print(f"{C.C}├─ {C.W}Port {port:<4} : {C.G}OPEN")
            else:
                print(f"{C.C}├─ {C.W}Port {port:<4} : {C.R}CLOSED")
            s.close()
        except Exception:
            pass
    print(f"{C.C}╰────────────────────────────")
    input(f"\n{C.Y}Press ENTER to go back...")

def mod_system():
    header()
    print(f"{C.C}╭───〔 𝗟𝗼𝗰𝗮𝗹 𝗡𝗼𝗱𝗲 𝗠𝗼𝗻𝗶𝘁𝗼𝗿 〕")
    print(f"{C.C}│")
    spinner(2, "Checking System")
    print(f"\n{C.C}╭───〔 𝗦𝘆𝘀𝘁𝗲𝗺 𝗛𝗲𝗮𝗹𝘁𝗵 〕")
    print(f"{C.C}├─ 𝗢𝗦       : {C.W}{platform.system()}")
    print(f"{C.C}├─ 𝗩𝗲𝗿𝘀𝗶𝗼𝗻  : {C.W}{platform.release()}")
    print(f"{C.C}├─ 𝗠𝗮𝗰𝗵𝗶𝗻𝗲  : {C.W}{platform.machine()}")
    try:
        cpu = os.cpu_count()
        print(f"{C.C}├─ 𝗖𝗣𝗨 𝗖𝗼𝗿𝗲𝘀: {C.W}{cpu}")
    except Exception:
        pass
    print(f"{C.C}╰────────────────────────────")
    input(f"\n{C.Y}Press ENTER to go back...")

def mod_phone():
    header()
    print(f"{C.C}╭───〔 𝗣𝗵𝗼𝗻𝗲 𝗡𝘂𝗺𝗯𝗲𝗿 𝗢𝗦𝗜𝗡𝗧 〕")
    num = input(f"{C.C}│\n╰──► {C.Y}Enter Phone Number (with +): {C.W}").strip()
    if not num:
        return
    print(f"\n{C.C}╭───〔 𝗣𝗵𝗼𝗻𝗲 𝗥𝗲𝘀𝘂𝗹𝘁𝘀 〕")
    try:
        p_obj = phonenumbers.parse(num, None)
        is_valid = phonenumbers.is_valid_number(p_obj)
        if is_valid:
            print(f"{C.C}├─ 𝗩𝗮𝗹𝗶𝗱    : {C.G}YES")
            print(f"{C.C}├─ 𝗖𝗼𝘂𝗻𝘁𝗿𝘆  : {C.W}{geocoder.description_for_number(p_obj, 'en')}")
            print(f"{C.C}├─ 𝗡𝗲𝘁𝘄𝗼𝗿𝗸  : {C.W}{carrier.name_for_number(p_obj, 'en')}")
            print(f"{C.C}├─ 𝗪𝗵𝗮𝘁𝘀𝗔𝗽𝗽 : {C.W}https://wa.me/{num.replace('+', '')}")
            print(f"{C.C}├─ 𝗦𝗰𝗮𝗺 𝗖𝗵𝗲𝗰𝗸: {C.B}https://www.google.com/search?q=%22{num.replace('+', '')}%22+scam")
        else:
            print(f"{C.C}├─ 𝗩𝗮𝗹𝗶𝗱    : {C.R}NO")
    except Exception:
        print(f"{C.C}├─ {C.R}Invalid format. Please use + country code.")
    print(f"{C.C}╰────────────────────────────")
    input(f"\n{C.Y}Press ENTER to go back...")

def mod_ip():
    header()
    print(f"{C.C}╭───〔 𝗜𝗣 𝗧𝗮𝗿𝗴𝗲𝘁 𝗚𝗲𝗼𝗹𝗼𝗰𝗮𝘁𝗶𝗼𝗻 〕")
    ip = input(f"{C.C}│\n╰──► {C.Y}Enter IP Address: {C.W}").strip()
    if not ip:
        return
    spinner(2, "Finding location")
    print(f"\n{C.C}╭───〔 𝗟𝗼𝗰𝗮𝘁𝗶𝗼𝗻 𝗥𝗲𝘀𝘂𝗹𝘁𝘀 〕")
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if res.get("status") == "success":
            print(f"{C.C}├─ 𝗖𝗼𝘂𝗻𝘁𝗿𝘆  : {C.W}{res.get('country')}")
            print(f"{C.C}├─ 𝗖𝗶𝘁𝘆     : {C.W}{res.get('city')}")
            print(f"{C.C}├─ 𝗜𝗦𝗣      : {C.W}{res.get('isp')}")
            print(f"{C.C}├─ 𝗠𝗮𝗽𝘀     : {C.B}https://www.google.com/maps?q={res.get('lat')},{res.get('lon')}")
        else:
            print(f"{C.C}├─ {C.R}Location not found")
    except Exception:
        print(f"{C.C}├─ {C.R}Connection Error")
    print(f"{C.C}╰────────────────────────────")
    input(f"\n{C.Y}Press ENTER to go back...")

def mod_url():
    header()
    print(f"{C.C}╭───〔 𝗠𝗮𝗹𝗶𝗰𝗶𝗼𝘂𝘀 𝗨𝗥𝗟 𝗦𝗰𝗮𝗻𝗻𝗲𝗿 〕")
    url = input(f"{C.C}│\n╰──► {C.Y}Enter Link: {C.W}").strip()
    if not url:
        return
    spinner(2, "Scanning Link")
    print(f"\n{C.C}╭───〔 𝗦𝗰𝗮𝗻 𝗥𝗲𝘀𝘂𝗹𝘁𝘀 〕")
    try:
        data = {'url': url}
        res = requests.post("https://urlhaus-api.abuse.ch/v1/url/", data=data, timeout=5).json()
        if res.get('query_status') == 'ok':
            print(f"{C.C}├─ 𝗦𝘁𝗮𝘁𝘂𝘀   : {C.R}DANGER (Malware Found)")
            print(f"{C.C}├─ 𝗧𝗵𝗿𝗲𝗮𝘁   : {C.W}{res.get('threat')}")
        else:
            print(f"{C.C}├─ 𝗦𝘁𝗮𝘁𝘂𝘀   : {C.G}SAFE (No records found)")
    except Exception:
        print(f"{C.C}├─ {C.R}Error scanning link")
    print(f"{C.C}╰────────────────────────────")
    input(f"\n{C.Y}Press ENTER to go back...")

def mod_crypto():
    header()
    print(f"{C.C}╭───〔 𝗖𝗿𝘆𝗽𝘁𝗼 𝗪𝗮𝗹𝗹𝗲𝘁 𝗔𝗻𝗮𝗹𝘆𝘇𝗲𝗿 〕")
    wallet = input(f"{C.C}│\n╰──► {C.Y}Enter BTC Address: {C.W}").strip()
    if not wallet:
        return
    spinner(2, "Checking Blockchain")
    print(f"\n{C.C}╭───〔 𝗪𝗮𝗹𝗹𝗲𝘁 𝗥𝗲𝘀𝘂𝗹𝘁𝘀 〕")
    try:
        res = requests.get(f"https://blockchain.info/rawaddr/{wallet}", timeout=5)
        if res.status_code == 200:
            data = res.json()
            btc = data.get('final_balance', 0) / 100000000
            print(f"{C.C}├─ 𝗕𝗮𝗹𝗮𝗻𝗰𝗲  : {C.G}{btc} BTC")
            print(f"{C.C}├─ 𝗧𝗿𝗮𝗻𝘀𝗳𝗲𝗿𝘀: {C.W}{data.get('n_tx')}")
        else:
            print(f"{C.C}├─ {C.R}Wallet not found or invalid")
    except Exception:
        print(f"{C.C}├─ {C.R}Error connecting to blockchain")
    print(f"{C.C}╰────────────────────────────")
    input(f"\n{C.Y}Press ENTER to go back...")

def main_loop():
    boot()
    while True:
        header()
        print(f"{C.C}╭───〔 𝗠𝗔𝗜𝗡 𝗢𝗣𝗘𝗥𝗔𝗧𝗜𝗢𝗡𝗦 〕")
        print(f"{C.C}│")
        print(f"{C.C}│ {C.G}❶ {C.C}𝗗𝗼𝗺𝗮𝗶𝗻 𝗥𝗲𝗰𝗼𝗻𝗻𝗮𝗶𝘀𝘀𝗮𝗻𝗰𝗲")
        print(f"{C.C}│    └─ {C.W}Web Scanner")
        print(f"{C.C}│")
        print(f"{C.C}│ {C.G}❷ {C.C}𝗧𝗮𝗰𝘁𝗶𝗰𝗮𝗹 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 𝗔𝗻𝗮𝗹𝘆𝘇𝗲𝗿")
        print(f"{C.C}│    └─ {C.W}LAN Ports")
        print(f"{C.C}│")
        print(f"{C.C}│ {C.G}❸ {C.C}𝗟𝗼𝗰𝗮𝗹 𝗡𝗼𝗱𝗲 𝗠𝗼𝗻𝗶𝘁𝗼𝗿")
        print(f"{C.C}│    └─ {C.W}System Health")
        print(f"{C.C}│")
        print(f"{C.C}│ {C.G}❹ {C.C}𝗣𝗵𝗼𝗻𝗲 𝗡𝘂𝗺𝗯𝗲𝗿 𝗢𝗦𝗜𝗡𝗧")
        print(f"{C.C}│    └─ {C.W}Scam & Digital Footprint")
        print(f"{C.C}│")
        print(f"{C.C}│ {C.G}❺ {C.C}𝗜𝗣 𝗧𝗮𝗿𝗴𝗲𝘁 𝗚𝗲𝗼𝗹𝗼𝗰𝗮𝘁𝗶𝗼𝗻")
        print(f"{C.C}│    └─ {C.W}Trace IP")
        print(f"{C.C}│")
        print(f"{C.C}│ {C.G}❻ {C.C}𝗠𝗮𝗹𝗶𝗰𝗶𝗼𝘂𝘀 𝗨𝗥𝗟 𝗦𝗰𝗮𝗻𝗻𝗲𝗿")
        print(f"{C.C}│    └─ {C.W}Link Analysis")
        print(f"{C.C}│")
        print(f"{C.C}│ {C.G}❼ {C.C}𝗖𝗿𝘆𝗽𝘁𝗼 𝗪𝗮𝗹𝗹𝗲𝘁 𝗔𝗻𝗮𝗹𝘆𝘇𝗲𝗿")
        print(f"{C.C}│    └─ {C.W}Blockchain Analysis")
        print(f"{C.C}│")
        print(f"{C.C}│ {C.R}❽ {C.C}𝗗𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁 & 𝗘𝘅𝗶𝘁")
        print(f"{C.C}│")
        print(f"{C.C}╰────────────────────────────")
        choice = input(f"\n{C.Y}Select Option: {C.W}").strip()
        if choice == '1':
            mod_domain()
        elif choice == '2':
            mod_network()
        elif choice == '3':
            mod_system()
        elif choice == '4':
            mod_phone()
        elif choice == '5':
            mod_ip()
        elif choice == '6':
            mod_url()
        elif choice == '7':
            mod_crypto()
        elif choice == '8':
            print(f"\n{C.R}[!] Closing Tool...")
            time.sleep(1)
            type_text(f"{C.C}Thanks for using Project NEXUS - {C.Y}Ranux Dev")
            break

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print(f"\n\n{C.R}[!] Force Quit. Exiting...{C.X}")
        sys.exit(0)
