import qrcode

import qrcode

# Dados a serem codificados no QR code
data = "https://www.example.com"

# Cria um objeto QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Cria a imagem do QR code
img = qr.make_image(fill_color="black", back_color="white")

# Salva a imagem
img.save("qrcode.png")