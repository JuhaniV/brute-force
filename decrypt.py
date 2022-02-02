import bitarray
from bs4 import BeautifulSoup
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad


def decrypt(key):
    iv, ciphered_data = read_encrypted()

    cipher = AES.new(pad(key, AES.block_size), AES.MODE_CBC, iv=iv)  
    try:
        original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) 
        str = original_data.decode('utf-8')

        print("Decrypted data: ", end="") 
        print(str)
        print("Encryption key: ", end="")
        print(key.decode('utf-8'))
    except:
        print('', end="")

def read_encrypted():
    input_file = 'encrypted.bin'

    file_in = open(input_file, 'rb') 
    iv = file_in.read(AES.block_size) 
    ciphered_data = file_in.read() 
    file_in.close()

    return iv, ciphered_data

def get_key():
    with open('./kotus-sanalista_v1/kotus-sanalista_v1.xml', 'r') as f:
        data = f.read()

    BSdata = BeautifulSoup(data, "lxml")
    sana = BSdata('s')
    
    for p in sana:
        decrypt(bytes(p.text.upper(), 'utf-8'))

if __name__ == "__main__":
    get_key()
