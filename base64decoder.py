import base64

while True:
    try: 
        encoded_string = input("Encoded: ")
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode("utf-8")
        print(decoded_string)
    except ValueError:
        print("Insert a valid string")
