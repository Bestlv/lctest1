import pyotp

def  func(my_token):
    x=my_token
    print(x)

def get_token(my_secret):
    totp = pyotp.TOTP(my_secret)
    my_token = totp.now()
    print(my_token)
if __name__ == '__main__':
    get_token("BOK6AQMFCRISMLC6")

