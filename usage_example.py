# install module in system:
# python setup.py install

import edbd

with open('key_example', 'r') as file:
    key = file.read()

with open('text_example', 'r') as file:
    text = file.read()

# Encryption
e = edbd.edbd(key, text)
e.encrypt_text()
print(e.return_encrypted_text())

# Decryption
d = edbd.edbd(key, e.return_encrypted_text())
d.decrypt_text()
print(d.return_decrypted_text())