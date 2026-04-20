import qrcode

QR_URL = "https://verinexis.ai"
QR_NAME = "test"

_qr_image_name = ".".join([QR_NAME, "png"])
_qr_name_string = "/".join(["qr_codes", _qr_image_name])
qrcode.make(QR_URL).save(str(_qr_name_string))