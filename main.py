def Input(text):
    return input(text)
def EncryptFile(path, key):
    Output=Input("Output file:")
    with open(path,'r')as file:
            encrypted=[EncryptText(line.strip(),key) for line in file]
    with open(Output,'w')as file:
        for i in encrypted:
            file.write(i+'\n')
    return encrypted
def DecryptFile(path, key):
    Output = Input("Output file:")
    with open(path, 'r') as file:
        decrypted = [DecryptText(line.strip(), key) for line in file]
    with open(Output, 'w') as file:
        for line in decrypted:
            file.write(line+'\n')

    return decrypted


def EncryptChar(char, key):
    base = 32
    end = 126
    encrypted_char = chr(base + (ord(char) - base + (key % (end - base + 1))) % (end - base + 1))
    return encrypted_char
def DecryptChar(char, key):
    base = 32
    end = 126
    decrypted_char = chr(base + (ord(char) - base - (key % (end - base + 1)) + (end - base + 1)) % (end - base + 1))
    return decrypted_char

def EncryptText(text,key):
    return ''.join([EncryptChar(i, key) for i in text])

def DecryptText(text, key):
    return ''.join([DecryptChar(i,key) for i in text])
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