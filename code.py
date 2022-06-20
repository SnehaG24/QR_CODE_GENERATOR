from textwrap import fill
import qrcode
import image

qrCode = qrcode.QRCode(
    version=13,
    box_size=9,
    border=2

)

link = "https://replit.com/@sneha18"

qrCode.add_data(link)
qrCode.make(fit=True)
image=qrCode.make_image(fill="black",back_color ="white")
image.save("replit.png")



