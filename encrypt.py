from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

output_file = 'encrypted.bin'
data = b'bruhh'
key = b'OSTO'


cipher = AES.new(pad(key, AES.block_size), AES.MODE_CBC) 
ciphered_data = cipher.encrypt(pad(data, AES.block_size))

file_out = open(output_file, "wb")
file_out.write(cipher.iv)
file_out.write(ciphered_data)
file_out.close()
