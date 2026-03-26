''' To create an qr code firstly you need to downlode these two module in your terminal
 first one is qrcode:pip install qrcode
 Second one is pillow:pip insatll pillow'''

import qrcode
qr = qrcode.make("https://open.spotify.com/track/32yIEFS62uS5ryhr2Xlooj?si=e54c1b58ff8646ae")
qr.save("my_fav_music.jpg")
