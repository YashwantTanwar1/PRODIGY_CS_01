from PIL import Image

def encrypt_image(image, secret_key):
    # Get pixel data
    pixels = image.load()
    width, height = image.size

    # Encrypt each pixel using XOR with the secret key
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r ^= secret_key
            g ^= secret_key
            b ^= secret_key
            pixels[x, y] = (r, g, b)

    return image

def main():
    # Load an image (replace 'your_image.png' with the actual image file)
    input_image_path = 'yyy.png'
    original_image = Image.open(input_image_path)

    # Set a secret key (you can choose any integer value)
    secret_key = 42

    # Encrypt the image using XOR
    encrypted_image = encrypt_image(original_image, secret_key)

    # Save the encrypted image
    encrypted_image.save('encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'.")

if __name__ == "__main__":
    main()
