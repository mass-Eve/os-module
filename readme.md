# os Module Python

First, import os Module using the `import` keyword
```python
import os
```

## 1 - Print The Current Working Directory ~

```python
import os

print('Want to know your current working directory ?')
ch = input('Y/n : ')
if (ch == 'Y' or 'y'):
    print(f'This is your current working directory - {os.getcwd()}')
else:
    pass
```

## 2 - Change The Current Working Directory ~

```python
import os

print(f"This is your current working directory -- {os.getcwd}")

print('Want to change the current working directory ?')
ch = input('Y/n : ')
if (ch == 'Y' or 'y'):
    dir_path = input('Enter the new directory path: ')
    os.chdir(dir_path)
    print('Directory Changed')
else:
    pass

print(f"This is your current working directory -- '{os.getcwd()}'")
```