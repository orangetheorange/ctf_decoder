import binascii

while True:
    try:
        inp = input("encoded: ")
        print(binascii.unhexlify(inp))
    except ValueError:
        print("Insert a valid string")
