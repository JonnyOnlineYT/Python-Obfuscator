#<==========Imports Starting==========>
import os
import time
import sys
import base64
import random
import string
import requests
#<==========Imports Ending==========>
try:
    kill = requests.get('https://pastebin.com/raw/CfcS71MC').text
    if kill == "0X72PROTECTOR":
        pass
    else:
        print('[0X72PROTECTOR] Protector is off, try again later.')
        time.sleep(2)
        os._exit(0) 
except:
    print('[0X72PROTECTOR] Something went wrong, try again later.')
    time.sleep(2)
    os._exit(0)
os.system('title 0X72PROTECTOR by 0x72#0001')
#<==========Path Select Starting==========>
try:
    filepath = sys.argv[1]
    if filepath[-3:] == ".py":
        pass
    else:
        print('File Must be only with extension .py')
        time.sleep(2)
        os._exit(0)
    try:
        file = open(filepath, "r", encoding='utf-8', errors='ignore')
        file.close()
    except:
        print('Invalid Path')
        time.sleep(2)
        os._exit(0)
except:
    print('Drag and Drop file like de4dot')
    time.sleep(10)
    os._exit(0)
print('[0X72PROTECTOR] Press enter to protect your file!\n')
input()
time.sleep(1)
#<==========Path Select Ending==========>
if not os.path.exists("Obfuscated"):
    os.makedirs(f"Obfuscated")
#<==========Obfuscation Starting==========>
def id_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))
open('Obfuscated/Protected.py', 'w', encoding='utf-8', errors='ignore').close()
lista = ['https://robert832.me/', 'https://github.com/robert169', 'https://discord.gg/6zTFat6', 'Discord: 0x72#0001 (698265602573336653)', "Telegram: @roberth832", "Telegram: @robertmarket", "Telegram: @robertreps"]

with open(filepath, "r", encoding='utf-8', errors='ignore') as main_file:

    with open(f'Obfuscated/Protected.py', "a", encoding='utf-8', errors='ignore') as obf_file:
        obf_file.write(f'# Protected by 0x72\n\nimport base64\nimport os\nimport time\nimport random\n')
        code = """\n_0x72_IS_COOL_STRING_ = ''\ndef _0x72_PROTECTOR(_0x72_IS_COOL_):\n    global _0x72_IS_COOL_STRING_\n    if _0x72_IS_COOL_ != '_0x72_IS_COOL_':\n        _0x72_IS_COOL_STRING_ = f'{_0x72_IS_COOL_.decode("utf-16")}'\n        exec(u'\u0023\u0020\u0070\u0072\u006f\u0074\u0065\u0063\u0074\u0065\u0064\u0020\u0062\u0079\u0020\u0030\u0078\u0037\u0032')\n    else:\n        time.sleep(50000)\n        os._exit(0)"""
        obf_file.write(f"{code}\n")
        print('[0X72PROTECTOR] String Encryption added')
        time.sleep(2)
        print('[0X72PROTECTOR] Method Encryption added')
        time.sleep(2)
        numar = random.choice(range(20, 100))
        numar_random1 = random.choice(range(25, 100))
        numar1 = "_0x72_Protector_"+id_generator(numar)
        read_entire_file = main_file.read()
        s = 0
        for each in range(0, 5):
            s+=1
            print(f'[0X72PROTECTOR] Junk number {s} added')
            numar_ = random.choice(range(20, 100))
            numar2 = "_0x72_Protector_"+id_generator(numar_)
            coderob = f"# Protected by 0x72#1337 - {random.choice(lista)}   "*numar_
            coderob = base64.b64encode(bytes(coderob, 'utf-8')).decode('utf-8')
            obf_file.write(f'try:\n    {numar2} = {coderob.encode("utf-16")}\n    _0x72_PROTECTOR({numar2})\n    exec(_0x72_IS_COOL_STRING_.strip())\nexcept Exception as e:\n    pass\n')
        obf_file.write(f"\ntry:\n    {numar1} = {read_entire_file.encode('utf-16')}\n    _0x72_PROTECTOR({numar1})\n    exec(_0x72_IS_COOL_STRING_.strip())\nexcept Exception as e:\n    pass\n")
        for each in range(0, 5):
            s+=1
            print(f'[0X72PROTECTOR] Junk number {s} added')
            numar__ = random.choice(range(20, 100))
            numar3 = "_0x72_Protector_"+id_generator(numar__)
            coderob = f"# Protected by 0x72#1337 - {random.choice(lista)}   "*numar__
            coderob = base64.b64encode(bytes(coderob, 'utf-8')).decode('utf-8')
            obf_file.write(f'try:\n    {numar3} = {coderob.encode("utf-16")}\n    _0x72_PROTECTOR({numar3})\n    exec(_0x72_IS_COOL_STRING_.strip())\nexcept Exception as e:\n    pass\n')
#<==========Obfuscation Ending==========>
time.sleep(1)
input('[0X72PROTECTOR] Done')
os._exit(0)
