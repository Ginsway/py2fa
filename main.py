import json
import time
import pyotp
import pyperclip

if __name__ == "__main__":
    
    try:
        with open("token.json","r") as f:
            token:str = json.load(f)[0]
    except FileNotFoundError:
        print("请输入你的token")
        token =input()
        with open("token.json","w") as f:
            json.dump([token],f)
            
    totp = pyotp.TOTP(pyotp.random_base32())
    while(True):
        try:
            time.sleep(1)
            print(totp.now())
            pyperclip.copy(totp.now())
        except KeyboardInterrupt:
            exit(0)
