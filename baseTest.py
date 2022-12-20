import base64
print("Start!")
with open("test.jpg", "rb") as f:
    img = f.read()
print("Second point")
img_base64 = base64.b64encode(img)
print('Third point')

with open("test_new.jpg", "wb") as f:
    f.write(base64.b64decode(img_base64))

print('4th point')

data = [1, 3, 4, 5, 6, 7, 9]

print("before for roop")

for d in data:
    print("before print d")
    print(d, "test")
    print("for point")


print("5th point")

print("Done")
print("base64")

print("Final point")
