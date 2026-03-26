''' To create an qr code firstly you need to downlode these two module in your terminal
 first one is qrcode:pip install qrcode
 Second one is pillow:pip insatll pillow'''

import qrcode
my_name = qrcode.make("Stwik Singh Rajput")
my_name.save("my_name.jpg")