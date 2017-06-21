import time
import Oper
import OperKey

key = OperKey.OperKey(5, time.time())
source_text = 10011111111114333333404004040433333
cipher_text = Oper.Oper.encrypt(key, source_text)
plain_text = Oper.Oper.decrypt(key, cipher_text)

print("source: ", source_text)
print("cipher: ", cipher_text)
print("plain:  ", plain_text)
print("key: ", key)
