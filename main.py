import qrcode
from PIL import Image, ImageOps

def make_qr(url, name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Get the QR code image as a PIL Image object
    img = qr.make_image(fill_color="white", back_color="black")

    # Convert the image to RGBA mode
    img = img.convert("RGBA")

    # Create a solid color image with the desired foreground color
    fg_color = (31, 81, 255)
    fg_img = Image.new("RGBA", img.size, fg_color)

    # Create a mask for the QR code image
    mask_img = ImageOps.invert(img.convert("L"))

    # Composite the QR code image and the foreground image using the mask
    img = Image.composite(fg_img, img, mask_img)

    img.save(name.replace(" ", "_") + ".png")

a = str(input("Please provide a URL: "))
b = str(input("Please provide a Name: "))

make_qr(a, b)
