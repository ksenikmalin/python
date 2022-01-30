from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = str.encode('Показания датчика № 10: нет сигнала')

key = get_random_bytes(16)
print("Сгенерированный ключ ", key)
cipher = AES.new(key, AES.MODE_EAX)

print("Шифр ", cipher)
ciphertext, tag = cipher.encrypt_and_digest(data)

print("Зашифрованное сообщение", ciphertext)

try:
    print(ciphertext.decode('utf-8'))
except Exception as ex:
    print("Не удалось сконвертировать сообщение в utf-8")


cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
restored_data = cipher.decrypt_and_verify(ciphertext, tag)

print("Восстановленное сообщение", restored_data.decode('utf-8'))


