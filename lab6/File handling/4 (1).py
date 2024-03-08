

import os 

path = "C:\Users\Бакен\Desktop\Новая папка\File.txt"
with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))