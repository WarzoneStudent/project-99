import os,shutil,time

path = input("Path of folder to clean: ")
days = int(input("minimum date of the files to keep: "))
seconds = time.time() - (days * 24 * 60 * 60)

checking = os.path.exists(path)

if checking == 'true':
   lis = os.walk(path)
   
print(lis)

for f in lis:
    pathname = os.path.join(path,f)
    ctime = os.stat(pathname).st_ctime

    if ctime < seconds:
        os.remove(pathname)
    else:
        continue