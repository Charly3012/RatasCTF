# 📝 Writeup – This is NOT the flag


## 🛠️ Tools Used / Herramientas Utilizadas

- Python3 - [Script](script.py)
- Base64
- XOR


## 🔎 Step by Step / Paso a Paso

1. **ES:** Paso 1 – El texto `nZyenIuZhMiXtoygzoygyJfMoJmTnsaC` estaba en Base64.  
Con `base64.b64decode(encoded_str)` obtuvimos los **bytes originales cifrados**.    

   **EN:** Step 1 – The string `nZyenIuZhMiXtoygzoygyJfMoJmTnsaC` was Base64-encoded.  
Using `base64.b64decode(encoded_str)` we recovered the **original encrypted bytes**.

1. **ES:** Paso 2 – El reto sugería que los bytes resultantes estaban cifrados con un **XOR de un solo byte**.  
Esto significa que cada byte del texto original fue combinado con la misma clave de 1 byte mediante la operación XOR. 

   **EN:** Step 2 – The challenge hinted that the decoded bytes were encrypted using a **single-byte XOR**.  
Each original byte was XORed with the same 1-byte key.

1. **ES:** Paso 2 – Como la clave tiene un solo byte, se probó **cada valor de 0 a 255**. Se buscó si el resultado contenía la cadena "ratasCTF{", típica de una flag.

   **EN:** Step 2 – Because the key is only one byte, we brute-forced all values from 0 to 255. We checked if the output contained the substring "ratasCTF{", a common flag prefix.

2. **ES:** La flag obtenida tras el XOR correcto aparece en la salida del script, con el formato ratasCTF{...}.

    **EN:** The flag retrieved after applying the correct XOR key appears in the script output, formatted as ratasCTF{...}.

``` Python
import base64

# string from the NOTflag.txt
encoded_str = "WEteS1lpfmxRchp4dUtETnVoHh8ZHB51TF9EVw=="
decoded_bytes = base64.b64decode(encoded_str)

def xor_characters(s, key):
    return ''.join(chr(ord(char) ^ key) for char in s)

for key in range(256):
    xored = xor_characters(decoded_bytes.decode('latin1'), key)
    if "ratasCTF{" in xored:
        print(f"XOR {key}: {xored}")
```


## 🚩 Flag
`ratasCTF{X0R_and_B45364_fun}`  
