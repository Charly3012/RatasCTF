import base64

flag = "ratasCTF{X0R_and_B45364_fun}"
key = 42  # el byte con el que vamos a ofuscar

# XOR con clave de un byte
xored = ''.join(chr(ord(c) ^ key) for c in flag)

# convertir a base64
encoded = base64.b64encode(xored.encode('latin1')).decode()

print("Cadena para NOTflag.txt:")
print(encoded)