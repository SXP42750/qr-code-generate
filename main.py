import qrcode

# Data to encode
data = input("Enter the data/link to generate QR code: ")

# Create QR Code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code (1 to 40)
    box_size=10,  # size of each box in pixels
    border=4  # thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="blue", back_color="orange")

# Save the image
img.save("custom_qr.png")

print("QR code generated and saved as custom_qr.png!")

