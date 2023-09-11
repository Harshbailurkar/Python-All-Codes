 # first download libraries just write pip install qrcode Image(here we already done this)

import qrcode

def generateQR(text):

    qr=qrcode.QRCode(

        version =1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img =qr.make_image(fill_colour ="red",black_color="blue")

    img.save("QR4img.png")

url=input("enter the link")
generateQR(url)