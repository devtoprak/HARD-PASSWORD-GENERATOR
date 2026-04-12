from datetime import datetime
import string
import secrets
import pyperclip
import os
from colorama import init, Fore, Style
init(autoreset=True)

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(FILE_PATH, "password_log.txt")

print(Style.BRIGHT + Fore.CYAN + "PASSWORD GENERATOR")
def generate_password(length=20):
    zmn = datetime.now()
    char1 = string.ascii_letters
    char2 = string.digits
    char3 = string.punctuation
    all_chars = char1 + char2 + char3
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    print(Style.BRIGHT + Fore.GREEN + "Press Enter to generate a password...")
    print(Style.BRIGHT + Fore.MAGENTA + "1. Letters: " + (length - 7) * char1)
    print(Style.BRIGHT + Fore.MAGENTA + "2. Digits: " + (length - 7) * char2)
    print(Style.BRIGHT + Fore.MAGENTA + "3. Punctuation: " + (length - 6) * char3)
    print(Style.BRIGHT + Fore.BLUE + "Generated Password: " + password)
    input(Style.BRIGHT + Fore.GREEN + "Press Enter to copy the password to the clipboard...")
    pyperclip.copy(password)
    print(Style.BRIGHT + Fore.GREEN + "Password copied to clipboard!") 

    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"{zmn}: Generated password: {password}\n")
        
generate_password()
input(Style.BRIGHT + Fore.YELLOW + "Press Enter to exit...")