import base64

# Prompt the user for the base64-encoded string
base64_encoded_string = input("Enter the base64-encoded string: ")

try:
    # Decode the base64-encoded string
    decoded_bytes = base64.b64decode(base64_encoded_string)

    # Convert the bytes to a string
    decoded_string = decoded_bytes.decode('utf-8')

    # Display the decoded string
    print("Decoded string:")
    print(decoded_string)

except Exception as e:
    print("Error decoding the input:", str(e))
