import os

key = os.urandom(32)
with open("key.bin", "wb") as f:
    f.write(key)
