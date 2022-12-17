import qrcode
"""
création d'un qrcode
"""
img= qrcode.make("https://fr.euronews.com/")
img.save("euronews.jpg")

qr= qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=3,
    border=5
)
qr.add_data('https://fr.euronews.com')
qr.make(fit=True)
img = qr.make_image(fill_color="blue",back_color="white")
img.save("euronews2.png")


"""
décodage du qrcode
"""
import cv2

d=cv2.QRCodeDetector()
val,points,straight_qrcode = d.detectAndDecode(cv2.imread("euronews.jpg"))
"""
affiche le contenu du qrcode
"""
print(val)