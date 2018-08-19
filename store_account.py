def store_account(accounts):
    f = open('accounts.txt', 'r')
    while True:
        name = f.readline().strip('\n')
        if name == '':
            break
        else:
            accounts[name] = [f.readline().strip('\n'), f.readline().strip('\n'), f.readline().strip('\n')]
    return accounts
    f.close()
