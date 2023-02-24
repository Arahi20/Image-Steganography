from PIL import Image

#Image encoder function
image_path="/Users/ahmedrahi/myrepo/encode:decode/image.JPEG"

userinp=input("What message do you want to hide in an image")
def encode_image(image_path, message):
    image = Image.open(image_path)

    # Convert message to binary
    binary_message = ''.join(format(ord(i), '08b') for i in message)

    # checking if the message can fit in the image comparing binary values
    if len(binary_message) > image.width * image.height:
        raise ValueError("Message too large for image")
    # creating a copy of the image 
    encoded_image = image.copy()
    # encode message in the image O^2
    index = 0
    for y in range(encoded_image.height):
        for x in range(encoded_image.width):
            #rgb values of each pixel in the image
            r, g, b = encoded_image.getpixel((x, y))

            # next bit of the image
            if index < len(binary_message):
                bit = int(binary_message[index])
            else:
                bit = 0

            # Encode the bit in the least significant bit of the red value 
            r = (r & 0xfe) | bit

            # update the pixels with new rgb values
            encoded_image.putpixel((x, y), (r, g, b))
            index += 1
    encoded_image.save("/Users/ahmedrahi/myrepo/encode:decode/image2.JPEG")

encode_image(image_path,userinp)
print("Completed succesfully!")

