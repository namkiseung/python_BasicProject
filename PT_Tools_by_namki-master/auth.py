import hashlib

for a in range(1,100000):
    digest = hashlib.sha256(a).hexdigest()
    if digest == "10e791503786fd498b532663cc43f2ac1aae7206e05d2f24ab06f9905a6878506abd9bc43c9e6e4547ff6077264f94ca4e233d241c21652500580872400ffbf59949c0f96a10b3c3e4ba0f9d00810a03cdc6f2d6e196d709b1cf233d3133241c216525110000T1689f2c2bfb":
p        print("[AUTH] {}".format(a))
        break