import qrcode
url = input("Enter the URL: ").strip()
file_path = "C:\\Users\\SATYA DEV\\Downloads\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)

print("QR code saved as qrcode.png")