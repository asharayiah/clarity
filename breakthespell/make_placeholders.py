# make_placeholders_fixed.py
from PIL import Image, ImageDraw, ImageFont

names = [("factory.png","FACTORY"),("spell.png","SPELL"),("crack.png","CRACK"),("truelight.png","TRUE LIGHT")]
for fname, label in names:
    w,h = 1600,1600
    img = Image.new("RGB",(w,h),(28,34,40))
    d = ImageDraw.Draw(img)
    # try to load a system font, fallback to default
    try:
        f = ImageFont.truetype("arial.ttf", 80)
    except:
        try:
            f = ImageFont.truetype("Segoe UI.ttf", 80)
        except:
            f = ImageFont.load_default()
    # compute text size robustly
    try:
        bbox = d.textbbox((0,0), label, font=f)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
    except AttributeError:
        # older Pillow fallback
        try:
            tw, th = f.getsize(label)
        except Exception:
            tw, th = (len(label) * 20, 60)
    d.text(((w-tw)/2,(h-th)/2), label, fill=(240,230,200), font=f)
    d.rectangle([10,10,w-11,h-11], outline=(200,200,200))
    # small caption with filename
    try:
        caption = fname
        cbbox = d.textbbox((0,0), caption, font=f)
        cw = cbbox[2]-cbbox[0]
    except Exception:
        cw = len(fname)*8
    d.text((20,h-60), fname, fill=(200,200,200), font=f)
    img.save(fname, "PNG", optimize=True)
print("Created placeholder images:", ", ".join(n for n,_ in names))
