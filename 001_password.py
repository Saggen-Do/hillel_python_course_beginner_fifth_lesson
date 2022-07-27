initial_password: str = input('Come up with password: ')
entered_password: str = ''
while entered_password != initial_password:
    entered_password = input('Enter password to enter: ')
    if entered_password != initial_password:
        print('Wrong password. Try agin.')
        continue
    else:
        print('Welcome home!')
