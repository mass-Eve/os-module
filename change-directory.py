import os

print(f"This is your current working directory -- {os.getcwd}")

print('Want to change the current working directory ?')
ch = input('Y/n')
if (ch == 'Y' or 'y'):
    dir_path = input('Enter the new directory path: ')
    os.chdir(dir_path)
    print('Directory Changed')
else:
    pass

print(f"This is your current working directory -- '{os.getcwd()}'")