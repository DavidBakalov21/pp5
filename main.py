def Input(text):
    return input(text)


def EncryptFile(path, key):
    encryptLine=""
    encrypted = []
    Output=Input("Output file:")
    with open(path,'r')as file:
        for line in file:
            for char in line:
                base = 32
                end = 126
                encrypted_char = chr(base + (ord(char) - base + (key % (end - base + 1))) % (end - base + 1))
                encryptLine+=encrypted_char
            encrypted.append(encryptLine)
    with open(Output,'w')as file:
        for line in encrypted:
            file.write(line)




    return encrypted


def DecryptFile(path, key):
    decryptLine = ""
    decrypted = []
    Output = Input("Output file:")
    with open(path, 'r') as file:
        for line in file:
            for char in line:
                base = 32
                end = 126
                decrypted_char = chr(base + (ord(char) - base - (key % (end - base + 1)) + (end - base + 1)) % (end - base + 1))
                decryptLine += decrypted_char
            decrypted.append(decryptLine)
    with open(Output,'w')as file:
        for line in decrypted:
            file.write(line)

    return decrypted


def EncryptText(text, key):
    encryptLine = ''
    for char in text:
        base = 32
        end = 126
        encrypted_char = chr(base + (ord(char) - base + (key % (end - base + 1))) % (end - base + 1))
        encryptLine += encrypted_char
    return encryptLine


def DecryptText(text, key):
    decryptLine = ''
    for char in text:
        base = 32
        end = 126
        decrypted_char = chr(base + (ord(char) - base - (key % (end - base + 1)) + (end - base + 1)) % (end - base + 1))
        decryptLine += decrypted_char
    return decryptLine


def command():
    choice=input("File or console:")
    if choice=="File":
        choiceEnDe=input("Encrypt or decrypt:")
        if choiceEnDe=="Encrypt":
            return EncryptFile(Input("Input path:"),int(Input("Input key:")))
        else:
            return DecryptFile(Input("Input path:"), int(Input("Input key:")))
    else:
        choiceEnDe = input("Encrypt or decrypt:")
        if choiceEnDe == "Encrypt":
            text=Input("Input text:")
            key=int(Input("Input key:"))
            return EncryptText(text, key)
        else:
            return DecryptText(Input("Input text:"), int(Input("Input key:")))

while True:
    print(command())