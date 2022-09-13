# pyinstaller (Windows) #

1. Navigate to directory with py script 
2. make sure the pyinstaller.exe is in your directory 
   1. will first need to `pip install pyinstaller`
   2. see where the file path to the exe, can also use `pip uninstall pyinstaller` to see where it is 
   3. copy it into the folder with the following `cp <path to exe>`

3. now run the following:
```
.\pyinstaller.exe --onedir --icon=imagename.ico --windowed PyFileName.py
```
+ `--ondir` will make a folder of everything and can now make a shortcut or a pin to that exe
+ `--onefile` will make a single exe, its slower and doesn't have in-house files