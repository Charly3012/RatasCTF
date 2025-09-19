import base64

plaintext = "This is an important secret, no one should know, do not go to the third floor of the social sciences library"
key = "" # I have lost the key!

def byte_xor(plaintext_bytes, key_bytes):
    output = []
    key_index = 0
    for b in plaintext_bytes:
        output.append(b ^ key_bytes[key_index])
        key_index = (key_index + 1) % len(key_bytes)
    return bytes(output)

ciphertext_b64 = base64.b64encode(byte_xor(plaintext.encode('utf-8'), key.encode('utf-8')))

ciphertext_decoded = base64.b64decode("JgkdElMqJ2YaNhA7MhlaLUQvXSsQFTouCzo4HHYLWl0dDxFBACs7Mxc8EDkxBkJzECpcf14JK20eMGxEOUVBFRdBAAkaMTBmHTRfPS1JWjkQOls6EBUwLhA+IBAlBlwYHAIRElMvPSQJOUIr")

print(ciphertext_decoded)