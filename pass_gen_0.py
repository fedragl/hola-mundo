from random import *

def login_access(password, generated_password):
    if password == generated_password:
        return('success')
    else:
        return('wrong password')

def generate_password():
    gen_password_fun=randint(0000,9999)
    print(gen_password_fun)
    return(gen_password_fun)

def login():
    generated_password=generate_password()
    password = input('input password:')
    password=int(password)
    status=login_access(password,generated_password)
    return(status)

x=''
while x != 'success':
    x=login()

#mmake it a while without reloading the password
