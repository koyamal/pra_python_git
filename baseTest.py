import base64

def print_code():
    print("this is print function")

print("Start!")
with open("test.jpg", "rb") as f:
    img = f.read()
print("Second point")
img_base64 = base64.b64encode(img)
print('Third point')

with open("test_new.jpg", "wb") as f:
    f.write(base64.b64decode(img_base64))

print('4th point')

data = [1, 3, 4, 5, 6, 7, 9, 11, 12, 15, 17, 18]
data2 = [1, 3, 4, 5, 6, 7, 9, 11, 12, 15, 17, 18,19, 20]
data02 = [1, 3, 4, 5, 6, 7, 9, 11, 12, 15, 17, 18,19, 20]
data3 = [15, 17, 18,19, 20, 22, 23]

dast = ["test", "pra", "Git"]
dasts = ["sstest", "pra", "Git"]
dasts= dast + ["test", "pra", "Git"]

print("before for roop")

for d in data:
    print("before print d")
    print(d, "test")
    print("for point")

for d in data:
    print("before print d")
    print(d, "test")
    print("for point")

for d in data3:
    print(d)

output = ""
for s in dast:
    output += s
print(s)

print("5th point")

print("Done")
print("base64")

print("Final point")
