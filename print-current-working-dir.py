import os

print('Want to know your current working directory ?')
ch = input('Y/n : ')
if (ch == 'Y' or 'y'):
    print(f'This is your current working directory - {os.getcwd()}')
else:
    pass