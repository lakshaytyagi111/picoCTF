import base64
import codecs

fp = [line.strip() for line in open("enc_flag")]

t = "".join(fp)
print(t)
print("--------------------------------")

res = base64.b64decode(t)
print(res)

ATTEMPTS = 5

for i in range(0, ATTEMPTS):
    res = base64.b64decode(res)
    print(res)

