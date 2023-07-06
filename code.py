from textwrap import fill
import qrcode
import image

qrCode = qrcode.QRCode(
    version=13,
    box_size=9,
    border=2

)

link = "https://www.linkedin.com/in/sneha-gharal-a62a11244/?trk=public-profile-join-page"

qrCode.add_data(link)
qrCode.make(fit=True)
image=qrCode.make_image(fill="black",back_color ="white")
image.save("Linkedln.png")