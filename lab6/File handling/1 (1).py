import os
path = '"C:\Users\Бакен\Desktop\Новая папка\File.txt"'

dirs = os.listdir(path)

print(f'folders and files in path - "{path}":\n', dirs)