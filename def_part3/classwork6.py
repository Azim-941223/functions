
def encrypteds(func):
    def inner():
        for letter in login and password:
            if letter == "":
                encrypted += ""
            else:
                encrypted += chr(ord(letter) + 5)
            return encrypted
    return inner

@encrypteds
def logpass():
    login = input("Enter login: ")
    password = input("Enter password: ")
    encrypted = ""

print(encrypteds)




