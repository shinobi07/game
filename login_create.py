from store_account import store_account

accounts = {}

def login_create():

    data = open('accounts.txt', 'a')

    store_account(accounts)

    def createaccount():
        print("Don't put spaces in account names, passwords, emails and pin numbers.")
        name = input('Account name: ')
        password = input('Password: ')
        email = input('Email: ')
        pin = input('PIN number (4 digits): ')
        info = [password, email, pin]
        accounts[name] = info
        for key in accounts:
            data.write(str(key) + '\n')
            for element in accounts[key]:
                data.write(str(element) + '\n')
        print('Account created successfully!')
        print('Logging in...')
        print('Log in successfully!')
        return True

    def loginaccount():
        name = input('Account name: ')
        password = input('Password: ')
        if name in list(accounts.keys()):
            if password == (accounts[name])[0]:
                print('Logging in...')
                print('Log in successfully!')
                return True
            else:
                print('Account name and password don\'t match!')
                return False
        else:
            print('Account name and password don\'t match!')
            return False

    print("Do you have an account? y/n/exit")
    answer = input()

    if answer == 'y':
        print('Log in!')
        if loginaccount() == False:
            return False
        else:
            return True

    elif answer == 'n':
        print('Create an account!')
        createaccount()
        return True

    elif answer == 'exit':
        return callable('exit')

    data.close()
