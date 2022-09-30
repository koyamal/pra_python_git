import base64

s = input()
title = input()

#sb = s[23:].encode()
#sb = s.split(',')[1]

img = base64.b64decode(s.split(',')[1])
with open("./ebi/" + title + ".jpg", 'wb') as f4:
    f4.write(img)
