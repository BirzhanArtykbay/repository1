
 import shutil 

 shutil.copy('C:\Users\Бакен\Desktop\Новая папка\File.txt', 'C:\Users\Бакен\Desktop\Новая папка\File.txt')

with open('C:\Users\Бакен\Desktop\Новая папка\File.txt', 'r') as f1:
    with open('C:\Users\Бакен\Desktop\Новая папка\File.txt', 'w') as f2:
        f2.write(f1.read())
        # for i in f1: f2.write(i)