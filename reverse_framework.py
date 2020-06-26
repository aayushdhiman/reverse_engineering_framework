import os
import binascii


# dire = input("directory: ")
dire = "C:\\Users\\aayus\\Documents\\hexcompare"
bca_files = []
hex_bca = []

for root, dirs, file in os.walk(dire):
    for f in file:
        if f.endswith(".bca"):
            # print(f)
            bca_files.append(f)

for filename in bca_files:
    with open(("C:\\Users\\aayus\\Documents\\hexcompare\\" + filename), 'rb') as f:
        content = f.read()
    hex_bca.append(binascii.hexlify(content))
    # print(hex_bca)
    # print(binascii.hexlify(content))


hex_check = []
for h in hex_bca:
    hex_check.append(h[:32])

for hexf in hex_check:
    a = hexf.decode("utf-8")
    # print(bytes.fromhex(a).decode("utf-8"))
    if bytes.fromhex(a).decode("utf-8") != "JeticoEncryptArc":
        hex_check.remove(hexf)
