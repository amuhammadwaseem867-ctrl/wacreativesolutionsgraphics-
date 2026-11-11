"""Crops project images out of the rendered PDF pages (pdftoppm output)."""
from PIL import Image
from pathlib import Path
import sys
SRC = Path(sys.argv[1]); OUT = Path(sys.argv[2])
def save(img, proj, name, maxw=1800):
    d = OUT/proj; d.mkdir(parents=True, exist_ok=True)
    if img.width > maxw: img = img.resize((maxw, round(img.height*maxw/img.width)), Image.LANCZOS)
    img.convert('RGB').save(d/f'{name}.jpg', quality=84, optimize=True, progressive=True)
def crop(f, box, proj, name, **k): save(Image.open(SRC/f).crop(box), proj, name, **k)

# AF7: full 16:9 guideline pages
for n, name in {1:'cover',5:'logo',7:'construction',9:'versions',10:'misuse',12:'colour',15:'type-montserrat',16:'type-poppins',19:'photography',21:'pattern',22:'icons',24:'dieline',25:'box',26:'boards',28:'polybag',30:'coveralls',31:'polos',37:'story',40:'stationery',41:'cards',43:'website',44:'app',45:'closing'}.items():
    save(Image.open(SRC/f'af7-{n:02d}.jpg'), 'af7', name, 1600)

# AERO serum box (1654x1170): trim the placeholder text on the left
crop('box-1.jpg',(330,0,1654,1170),'aero-serum','logo')
save(Image.open(SRC/'box-2.jpg'),'aero-serum','dieline')
crop('box-3.jpg',(330,0,1654,1170),'aero-serum','box-flat')
crop('box-4.jpg',(330,0,1654,1170),'aero-serum','bottle')
crop('box-5.jpg',(330,0,1654,1170),'aero-serum','label')

# AERO sportswear (1800x5634)
crop('ifti-1.jpg',(0,0,1800,435),'aero-sport','header')
crop('ifti-1.jpg',(0,435,1800,2370),'aero-sport','logo-colour')
crop('ifti-1.jpg',(0,3150,1800,4260),'aero-sport','bottles')

# 4K Brew (990x1650)
b1='brew-1.jpg'; b2='brew-2.jpg'
crop(b1,(0,0,990,580),'4k-brew','hero')
crop(b1,(10,585,985,850),'4k-brew','system')
crop(b1,(12,855,370,1122),'4k-brew','packaging')
crop(b1,(375,855,580,1122),'4k-brew','cup-front')
crop(b1,(583,855,787,1122),'4k-brew','cup-back')
crop(b1,(790,855,980,1122),'4k-brew','store-sign')
crop(b1,(12,1128,422,1396),'4k-brew','thank-you')
crop(b1,(426,1128,802,1396),'4k-brew','menu')
crop(b1,(806,1128,980,1396),'4k-brew','cup-holder')
crop(b1,(12,1402,305,1650),'4k-brew','social')
crop(b1,(310,1402,502,1650),'4k-brew','shirt')
crop(b1,(505,1402,712,1650),'4k-brew','cap')
crop(b2,(8,300,745,515),'4k-brew','variations')
crop(b2,(0,535,990,738),'4k-brew','pattern')
crop(b2,(0,0,560,260),'4k-brew','logo')

# FANI Coffee (1018x1754)
crop('fani-1.jpg',(0,0,1018,339),'fani','logos')
crop('fani-1.jpg',(0,0,400,330),'fani','logo')
crop('fani-1.jpg',(0,680,1018,880),'fani','palette')
crop('fani-2.jpg',(0,0,1018,935),'fani','uniforms')
crop('fani-2.jpg',(0,940,1018,1754),'fani','drinkware')
crop('fani-3.jpg',(14,1078,610,1664),'fani','app')
crop('fani-3.jpg',(600,1040,1018,1754),'fani','iced')
crop('fani-4.jpg',(0,0,1018,616),'fani','storefront')
crop('fani-4.jpg',(0,626,1018,1180),'fani','signage')
crop('fani-4.jpg',(0,1180,1018,1754),'fani','social')

# Discover Gilgit Baltistan (1529x1888)
g='gb-1.jpg'
crop(g,(38,15,627,612),'gilgit-baltistan','logo')
crop(g,(780,627,1292,803),'gilgit-baltistan','variations')
crop(g,(558,894,1529,1193),'gilgit-baltistan','merch')
crop(g,(38,1208,451,1705),'gilgit-baltistan','luggage')
crop(g,(451,1208,1208,1414),'gilgit-baltistan','pattern')
crop(g,(1208,1200,1529,1529),'gilgit-baltistan','hoodie')
crop(g,(1170,1598,1414,1850),'gilgit-baltistan','app-icon')
print('done')
