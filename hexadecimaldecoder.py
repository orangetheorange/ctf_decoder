while True:
    try:
        hex_string = input("encoded: ")
        decoded_bytes = bytes.fromhex(hex_string)
        print(decoded_bytes)
    except ValueError:
        print("Insert a valid string")
