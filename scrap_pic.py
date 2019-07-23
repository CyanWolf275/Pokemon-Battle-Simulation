import re, requests, shutil
lnk = requests.get("https://bulbapedia.bulbagarden.net/wiki/File:Spr_6x_001.png")
url1 = "http://" + re.findall(r'cdn\.bulbagarden\.net\/upload.*?Spr_6x_001\.png', lnk.text)[0]
url2 = "http://" + re.findall(r'cdn\.bulbagarden\.net\/upload.*?Spr_b_6x_001\.png', lnk.text)[0]
r1 = requests.get(url1, stream = True)
with open("Spr_6x_001.png", 'wb') as f:
    r1.raw.decode_content = True
    shutil.copyfileobj(r1.raw, f)