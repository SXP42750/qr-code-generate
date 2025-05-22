# qr-code-generate
Simple Python project that generates QR codes from text or URLs
## What I Learned
How to generate and customize QR codes using Python.
- The use of external libraries like `qrcode` and `PIL`.
- Saving images and understanding how data is encoded visually.

✅ Features:
Converts any input text or URL into a QR code.
Customizable version, box size, and border.
Saves the QR code as a .png image.

🛠️ Tech Stack:
Python
qrcode module
Pillow (PIL) for image handling

📄 Steps in the Code:
1. Import required libraries – qrcode, PIL, and os.

2. Create a QRCode object with:

    version=1: Smallest size (can hold ~25 characters).
    
    box_size=10: Size of each box in pixels.
    
    border=5: White border around the QR code.

3. Add your data (like a URL or text).

4. Generate the QR code with .make(fit=True).

5. Create and save the image with custom colors using .make_image() and .save().

Sample output:
![image](https://github.com/user-attachments/assets/937b8320-4ae2-45fc-99b1-093abf20c211)

How to Run:
  Install required modules:
    pip install qrcode[pil]

Run the Python script:
  python qr_generator.py





