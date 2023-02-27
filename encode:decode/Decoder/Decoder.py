from PIL import Image


def decode_image(image_path):
    image = Image.open(image_path)

    binary_message = ""
    for y in range(image.height):
        for x in range(image.width):
            # Get RGB values of pixel
            r, _, _ = image.getpixel((x, y))

            # Get the least significant bit of the red value this was where our message was hidden
            bit = r & 0x01

            # Add the bit to the binary message
            binary_message += str(bit)

    # Convert binary message to text
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))

    return message

image_path=input("Please enter the filepath of the encoded image")
print("Decoding!")
message = decode_image(image_path)
print(message)
