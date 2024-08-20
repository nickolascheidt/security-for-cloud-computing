from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from Crypto.Util import Counter
from binascii import unhexlify, hexlify

def unhex(k,iv,c):
    key = unhexlify(k)
    iv = unhexlify(iv) 
    ciphertext = unhexlify(c)
    return key, iv, ciphertext

def getData():
    print("please, type your key")
    key_hex = input()

    print("now your IV")
    iv_hex = input()

    print("finally, type your text")
    ciphertext_hex = input()
    return key_hex, iv_hex, ciphertext_hex

def deCBC(k, iv, c):  
    cipher = AES.new(k, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(c), AES.block_size)
    plaintext_utf8 = plaintext.decode('utf-8')
    print("\n")
    print(plaintext_utf8)

def deCTR(k, iv, c):
    ctr = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
    cipher = AES.new(k, AES.MODE_CTR, counter=ctr)
    plaintext = cipher.decrypt(c)
    plaintext_utf8 = plaintext.decode('utf-8')
    print("\n")
    print(plaintext_utf8)

def enCTR(k, iv, c):
     ctr = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
     cipher = AES.new(k, AES.MODE_CTR, counter=ctr)
     ciphertext = cipher.encrypt(c)
     hexad = hexlify(ciphertext).decode('utf-8')
     print("\n")
     print(hexad.upper())

def enCBC(k, iv, c):
     cipher = AES.new(k, AES.MODE_CBC, iv)
     padded_c = pad(c, AES.block_size)
     ciphertext = cipher.encrypt(padded_c)
     hexad = hexlify(ciphertext).decode('utf-8')
     print("\n")
     print(hexad.upper())

def textToHex():
        print("\nplease, type the text you want to turn into hex: ")
        text = input()
        hex_text = text.encode('utf-8')
        result = hexlify(hex_text).decode('utf-8')
        return result.upper()

def use():
        key_hex, iv_hex, ciphertext_hex = getData()
        key, iv, ciphertext = unhex(key_hex, iv_hex, ciphertext_hex)
        return key, iv, ciphertext

def menu():
    while True:
        print("\nselect your type of operation: ")
        print("1 - decypt")
        print("2 - encrypt")
        print("3 - text to hex")
        print("0 - exit")
        
        choiceMain = input("\ntype the number: ")
        
        if choiceMain == '1':
            while True:
                print("\n1 - CBC")
                print("2 - CTR")
                print("0 - exit")
                choice = input("\ntype the number: ")
                if choice == '1':
                    key, iv, ciphertext = use()
                    deCBC(key, iv, ciphertext)
                elif choice == '2':
                    key, iv, ciphertext = use()
                    deCTR(key, iv, ciphertext)
                elif choice == '0':
                    print("returning to the main menu..")
                    break
                else:
                    print("invalid option, please try again")

        elif choiceMain == '2':
            while True:
                print("\n1 - CBC")
                print("2 - CTR")
                print("0 - exit")
                choice = input("\ntype the number: ")
                if choice == '1':
                    key, iv, ciphertext = use()
                    enCBC(key, iv, ciphertext)
                elif choice == '2':
                    key, iv, ciphertext = use()
                    enCTR(key, iv, ciphertext)
                elif choice == '0':
                    print("returning to the main menu..")
                    break
                else:
                    print("invalid option, please try again")
        elif choiceMain == '3':
            answer = textToHex()
            print(answer)
        elif choiceMain == '0':
            print("exiting the program..")
            break
        else:
            print("invalid option, please try again")

menu()








