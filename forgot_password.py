from login_create import accounts
from store_account import *

def forgot_password():
    store_account(accounts)

    print('''
    Account name:
    Email:
    Pin number:
    ''')

    name = input()
    email = input()
    pin = input()
    if name in accounts.keys():
        for key in accounts:
            if email == (accounts[key])[1] and pin == (accounts[key])[2]:
                print('Your password is %s.' % (accounts[key])[0])
    else:
        print('Something\'s wrong')
