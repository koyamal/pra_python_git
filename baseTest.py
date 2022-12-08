import base64
print("Start!")
with open("test.jpg", "rb") as f:
    img = f.read()

img_base64 = base64.b64encode(img)

with open("test_new.jpg", "wb") as f:
    f.write(base64.b64decode(img_base64))

print("Done")
print("base64")
