def encrypt(message, key):
    """
    Verilen mesajı, verilen anahtar ile şifreleyen fonksiyon.
    """
    encrypted = ""
    for char in message:
        encrypted += chr(ord(char) + key)
    return encrypted

def decrypt(message, key):
    """
    Verilen şifreli mesajı, verilen anahtar ile çözen fonksiyon.
    """
    decrypted = ""
    for char in message:
        decrypted += chr(ord(char) - key)
    return decrypted

# Kullanım örneği
message = "Merhaba, bu bir sifreli mesajdir!"
key = 3
encrypted_message = encrypt(message, key)
print("Şifreli mesaj: ", encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print("Çözülmüş mesaj: ", decrypted_message)
