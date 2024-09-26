import string

class Caesar:    

    def __init__(self):
        self._key = 0
    
    def get_key(self):
        return self._key

    def set_key(self, x):
        self._key = x


    def encrypt(self, plaintext):
            
        text = plaintext.lower()     

        final_output = ""
        key_position = 0

        for i in range (len(text)):
            if 97 <= ord(text[i]) <= 122:
                initial_output = ord(text[i]) - 97 + self._key
                transition = initial_output % 26 + 97
                final_output += chr(transition)
                key_position += 1
            elif ord(text[i]) != 32:
                initial_output = ord(text[i]) + self._key
                final_output += chr(initial_output)
                key_position += 1
            else:
                final_output += text[i]

        return (final_output)


    def decrypt(self, ciphertext):
            
        text = ciphertext.lower()     

        final_output = ""
        key_position = 0

        for i in range (len(text)):
            if 97 <= ord(text[i]) <= 122:
                initial_output = ord(text[i]) - 97 - self._key
                transition = initial_output % 26 + 97
                final_output += chr(transition)
                key_position += 1
            elif ord(text[i]) != 32:
                initial_output = ord(text[i]) - self._key
                final_output += chr(initial_output)
                key_position += 1
            else:
                final_output += text[i]

        return (final_output)


cipher = Caesar()
cipher.set_key(6)
cipher.get_key()

print(cipher.encrypt("zzz"))
print(cipher.decrypt("FFF"))
