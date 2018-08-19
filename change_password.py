from login_create import *

def change_password():
    print('''
    Account name:
    Current password:
    New password:
    Confirm New Password:
    ''')
    while True:
        name = input()
        current_pass = input()
        new_pass = input()
        confirm_pass = input()
        if current_pass != (accounts[name])[0] or new_pass != confirm_pass or name not in accounts.keys():
            print("Something's wrong here! Try again.")
        else:
            (accounts[name])[0] = new_pass
            break
    tk = open('accounts.txt', 'w')
    for name in accounts:
        tk.write(str(name) + '\n')
        for element in accounts[name]:
            tk.write(str(element) + '\n')
    tk.close()
