import base64
import os

s = input()
name = input()

sb = s.split(',')[1].encode()

img = base64.b64decode(sb)

baseDir = "./ebi/"
listFile = os.listdir(baseDir)

maxN = 0

for fileName in listFile:
    if fileName.split('_')[0] == name:
        n = int(fileName.split('_')[1].split('.')[0])
        if n > maxN:
            maxN = n

maxN = "00" + str(maxN + 1)

filePath = baseDir + name + "_" + maxN[len(maxN) - 3:] + ".jpg"

with open(filePath, 'wb') as f4:
    f4.write(img)
