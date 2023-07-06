import qrcode
import image

qrs = qrcode.QRCode(
    version = 14,
    box_size=10,
    border=2

)

data = "https://github.com/SnehaG24"
qrs.add_data(data)

qrs.make(fit=True)
image = qrs.make_image(fill="black",back_color = "white")
image.save("Github.png")