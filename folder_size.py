import sys
import os

try:
    directory = sys.argv[1]
except IndexError:
    sys.exit("Must provide an arguement")

dir_size = 0

fsizedicr = {
    'Bytes': 1,
    'Kilobytes': float(1) / 1024,
    'Megabytes': float(1) / (1024 * 1024),
    'Gigabytes': float(1) / (1024 * 1024 * 1024)
}

for (path, dirs, files) in os.walk(directory):
    for file in files:
        filename = os.path.join(path, file)
        dir_size += os.path.getsize(filename)

fsizeList = [str(round(fsizedicr[key] * dir_size, 2)) + " " + key for key in fsizedicr]

if dir_size == 0:
    print("File Empty")
else:
    for units in sorted(fsizeList)[::-1]: 
        print("Folder Size: " + units)