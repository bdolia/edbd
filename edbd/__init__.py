#!/usr/bin/env python

import secrets

class edbd(object):
    """
    An encryption class
    """
    def __init__(self, key, text):
        """
        Initializes a key file name, a text file name, a char position bucket
        """
        self.key = key
        self.text = text
        self.bucket = {}
        self.encrypted_text = []
        self.decrypted_text = []

        for i in range(len(self.key)):
            if ord(self.key[i]) in self.bucket:
                self.bucket[ord(self.key[i])].append(i)
            else:
                self.bucket[ord(self.key[i])] = []
                self.bucket[ord(self.key[i])].append(i)


    def encrypt_text(self):
        
        for i in range(len(self.text)):
            if ord(self.text[i]) in self.bucket:
                if self.bucket[ord(self.text[i])]:
                    self.encrypted_text.append(secrets.choice(self.bucket[ord(self.text[i])]))
                else:
                    self.encrypted_text.append(0)
            else:
                self.encrypted_text.append(0)

        return self.encrypted_text


    def return_encrypted_text(self):

        encrypted_text = ""
        for i in self.encrypted_text:
            encrypted_text = encrypted_text + str(i) + " "
        
        return encrypted_text[:-1]


    def decrypt_text(self):

        splited_text = self.text.split(" ")

        for i in range(len(splited_text)):

            found_char = False

            for char_unicode, position in self.bucket.items():
                if int(splited_text[i]) in position:
                    self.decrypted_text.append(chr(char_unicode))
                    found_char = True
            
            if not found_char:
                self.decrypted_text.append(32)

        return self.decrypted_text


    def return_decrypted_text(self):

        decrypted_text = ""
        for i in self.decrypted_text:
            decrypted_text = decrypted_text + str(i)
        
        return decrypted_text            
