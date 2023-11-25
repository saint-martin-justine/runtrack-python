def chiffrement_cesar(message, decalage):
    return ''.join([chr((ord(lettre) - 65 + decalage) % 26 + 65) if lettre.isupper() else chr((ord(lettre) - 97 + decalage) % 26 + 97) if lettre.islower() else lettre for lettre in message])

message_original = "Bonjour, César !"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)
print("Message original:", message_original)
print("Message chiffré:", message_chiffre)
