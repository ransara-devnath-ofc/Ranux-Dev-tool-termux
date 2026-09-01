import os
import sys
import time
import socket
import platform
import requests
from colorama import Fore, Style, init

init(autoreset=True)

class Colors:
    CYAN = Fore.CYAN
    GREEN = Fore.LIGHTGREEN_EX
    RED = Fore.LIGHTRED_EX
    YELLOW = Fore.YELLOW
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL

def typewriter(text, speed=0.015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def spinner_animation(duration, message):
    spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    idx = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{Colors.CYAN}[{spinner_chars[idx]}] {Colors.WHITE}{message}")
        sys.stdout.flush()
        idx = (idx + 1) % len(spinner_chars)
        time.sleep(0.1)
    sys.stdout.write(f"\r{Colors.GREEN}[✔] {message} - Complete!      \n")
    sys.stdout.flush()

def progress_bar():
    total_blocks = 30
    sys.stdout.write(f"{Colors.CYAN}Loading Core Modules: [")
    for i in range(total_blocks):
        sys.stdout.write(f"{Colors.GREEN}█")
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write(f"{Colors.CYAN}]{Colors.RESET}\n")

def boot_sequence():
    os.system('clear' if os.name == 'posix' else 'cls')
    typewriter(f"{Colors.GREEN}[+] Initializing Target Sockets...")
    typewriter(f"{Colors.GREEN}[+] Bypassing Gateway Protocols...")
    spinner_animation(2, "Establishing Secure Connection")
    progress_bar()
    time.sleep(0.5)

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner_art = f"""{Colors.RED}
  _   _  ______ __  __ _    _  _____ 
 | \\ | ||  ____|\\ \\/ /| |  | |/ ____|
 |  \\| || |__    \\  / | |  | | (___  
 | . ` ||  __|   /  \\ | |  | |\\___ \\ 
 | |\\  || |____ / /\\ \\| |__| |____) |
 |_| \\_||______/_/  \\_\\\\____/|_____/ 
    """
    print(banner_art)
    print(f"{Colors.CYAN}┌──────────────────────────────────────────┐")
    print(f"{Colors.CYAN}│ {Colors.YELLOW}👑 DEVELOPER : RANUX DEV                 {Colors.CYAN}│")
    print(f"{Colors.CYAN}├──────────────────────────────────────────┤")
    print(f"{Colors.CYAN}│ {Colors.GREEN}STATUS  : {Colors.WHITE}ACTIVE / SECURE              {Colors.CYAN}│")
    print(f"{Colors.CYAN}│ {Colors.GREEN}HOST IP : {Colors.WHITE}{get_local_ip():<26} {Colors.CYAN}│")
    print(f"{Colors.CYAN}│ {Colors.GREEN}SYSTEM  : {Colors.WHITE}{platform.system()[:26]:<26} {Colors.CYAN}│")
    print(f"{Colors.CYAN}└──────────────────────────────────────────┘\n")

def recon_module():
    show_banner()
    print(f"{Colors.CYAN}┌───[{Colors.WHITE} TARGET RECONNAISSANCE {Colors.CYAN}]")
    target = input(f"│\n└──► {Colors.YELLOW}Enter Target Domain (eg: domain.com): {Colors.WHITE}").strip()
    
    if not target:
        print(f"\n{Colors.RED}[✖] Invalid Target.")
        time.sleep(2)
        return

    print(f"\n{Colors.GREEN}[+] Target Locked: {target}")
    spinner_animation(3, "Querying crt.sh public transparency logs")

    url = f"https://crt.sh/?q=%.{target}&output=json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Nexus/1.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.json()
            subdomains = set()
            for entry in data:
                name_value = entry.get('name_value', '')
                for sub in name_value.split('\n'):
                    sub = sub.strip().lower()
                    if '*' not in sub and sub != target:
                        subdomains.add(sub)
            
            sub_list = sorted(list(subdomains))
            print(f"\n{Colors.CYAN}┌──────────────────────────────────────────┐")
            print(f"{Colors.CYAN}│ {Colors.GREEN}FOUND {len(sub_list)} SUBDOMAINS{Colors.CYAN}")
            print(f"{Colors.CYAN}├──────────────────────────────────────────┤")
            for sub in sub_list[:15]: 
                print(f"{Colors.CYAN}│ {Colors.WHITE}► {sub}")
            if len(sub_list) > 15:
                print(f"{Colors.CYAN}│ {Colors.YELLOW}... and {len(sub_list) - 15} more.")
            print(f"{Colors.CYAN}└──────────────────────────────────────────┘")
        else:
            print(f"{Colors.RED}[✖] Failed to retrieve data. Status: {response.status_code}")
    except Exception as e:
        print(f"{Colors.RED}[✖] Connection Error: {e}")
    
    input(f"\n{Colors.YELLOW}Press [ENTER] to return to Main Node...")

def network_module():
    show_banner()
    print(f"{Colors.CYAN}┌───[{Colors.WHITE} TACTICAL NETWORK SCANNER {Colors.CYAN}]")
    target_ip = input(f"│\n└──► {Colors.YELLOW}Enter Target IP Address: {Colors.WHITE}").strip()
    
    if not target_ip:
        print(f"\n{Colors.RED}[✖] Invalid IP.")
        time.sleep(2)
        return

    print(f"\n{Colors.GREEN}[+] Initializing Nmap-style stealth scan...")
    spinner_animation(2, "Mapping network topology")
    
    ports = [21, 22, 23, 53, 80, 111, 135, 139, 443, 445, 3306, 8080, 8443]
    open_ports = []

    print(f"\n{Colors.CYAN}┌───[ {Colors.WHITE}SCAN RESULTS : {target_ip} {Colors.CYAN}]")
    for port in ports:
        sys.stdout.write(f"│ {Colors.YELLOW}Scanning Port {port}... ")
        sys.stdout.flush()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"{Colors.GREEN}OPEN [✔]")
                open_ports.append(port)
            else:
                print(f"{Colors.RED}CLOSED")
            s.close()
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}[!] Scan aborted by user.")
            break
        except Exception:
            print(f"{Colors.RED}ERROR")
            
    print(f"{Colors.CYAN}├──────────────────────────────────────────┤")
    if open_ports:
        print(f"{Colors.CYAN}│ {Colors.GREEN}Total Open Ports Found: {len(open_ports)}")
    else:
        print(f"{Colors.CYAN}│ {Colors.YELLOW}No critical open ports detected.")
    print(f"{Colors.CYAN}└──────────────────────────────────────────┘")

    input(f"\n{Colors.YELLOW}Press [ENTER] to return to Main Node...")

def node_module():
    show_banner()
    print(f"{Colors.CYAN}┌───[{Colors.WHITE} LOCAL NODE MONITOR {Colors.CYAN}]")
    print(f"│")
    spinner_animation(2, "Analyzing System Metrics")
    
    print(f"\n{Colors.CYAN}┌───[ {Colors.WHITE}SYSTEM HEALTH & INFO {Colors.CYAN}]")
    print(f"{Colors.CYAN}│ {Colors.YELLOW}Architecture : {Colors.WHITE}{platform.machine()}")
    print(f"{Colors.CYAN}│ {Colors.YELLOW}Processor    : {Colors.WHITE}{platform.processor() or 'ARM/Unknown'}")
    print(f"{Colors.CYAN}│ {Colors.YELLOW}OS Release   : {Colors.WHITE}{platform.release()}")
    
    try:
        mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
        mem_gb = mem_bytes / (1024.**3)
        print(f"{Colors.CYAN}│ {Colors.YELLOW}Total Memory : {Colors.WHITE}{mem_gb:.2f} GB")
    except:
        print(f"{Colors.CYAN}│ {Colors.YELLOW}Total Memory : {Colors.WHITE}Access Denied (Termux Restricted)")

    print(f"{Colors.CYAN}├──────────────────────────────────────────┤")
    print(f"{Colors.CYAN}│ {Colors.GREEN}Node Integrity Check: SECURE")
    print(f"{Colors.CYAN}└──────────────────────────────────────────┘")
    
    input(f"\n{Colors.YELLOW}Press [ENTER] to return to Main Node...")

def main_loop():
    boot_sequence()
    while True:
        show_banner()
        print(f"{Colors.CYAN}┌───[ {Colors.WHITE}MAIN OPERATIONS {Colors.CYAN}]")
        print(f"{Colors.CYAN}│")
        print(f"{Colors.CYAN}│ {Colors.WHITE}[{Colors.GREEN}1{Colors.WHITE}] {Colors.YELLOW}Reconnaissance & Subdomain Scan")
        print(f"{Colors.CYAN}│ {Colors.WHITE}[{Colors.GREEN}2{Colors.WHITE}] {Colors.YELLOW}Tactical Network Scanner")
        print(f"{Colors.CYAN}│ {Colors.WHITE}[{Colors.GREEN}3{Colors.WHITE}] {Colors.YELLOW}Local Node Monitor")
        print(f"{Colors.CYAN}│ {Colors.WHITE}[{Colors.RED}4{Colors.WHITE}] {Colors.RED}Disconnect & Exit")
        print(f"{Colors.CYAN}│")
        
        choice = input(f"└──► {Colors.WHITE}Select Option: {Colors.GREEN}").strip()
        
        if choice == '1':
            recon_module()
        elif choice == '2':
            network_module()
        elif choice == '3':
            node_module()
        elif choice == '4':
            print(f"\n{Colors.RED}[!] Disconnecting Node...")
            time.sleep(1)
            typewriter(f"{Colors.CYAN}Thanks for using Project NEXUS - {Colors.YELLOW}Ranux Dev")
            break
        else:
            print(f"\n{Colors.RED}[✖] Invalid Command Sequence. Try Again.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[!] Force Quit Detected. Shutting down securely...{Colors.RESET}")
        sys.exit(0)
