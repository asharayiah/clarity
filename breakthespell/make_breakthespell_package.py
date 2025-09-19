#!/usr/bin/env python3
import os, json, zipfile, csv, shutil
from datetime import datetime, timedelta
from PIL import Image, ImageOps

REPO_URL = "https://github.com/asharayiah/clarity.git"
OUT_DIR = "breakthespell_package_local"
SOURCE_FILES = {
    'factory': 'factory.png',
    'spell': 'spell.png',
    'crack': 'crack.png',
    'truelight': 'truelight.png'
}
langs = [('en','English'),('es','Español'),('fr','Français'),('de','Deutsch'),
         ('ru','Русский'),('zh','中文'),('ar','العربية'),('hi','हिन्दी'),('el','Ελληνικά')]

if os.path.exists(OUT_DIR):
    shutil.rmtree(OUT_DIR)
os.makedirs(OUT_DIR)

images_dir = os.path.join(OUT_DIR, 'images')
os.makedirs(images_dir, exist_ok=True)

print("Generating image variants...")
for key, src in SOURCE_FILES.items():
    if not os.path.exists(src):
        raise FileNotFoundError(f"Missing source image: {src} — please place it in the script folder.")
    img = Image.open(src).convert('RGB')
    key_dir = os.path.join(images_dir, key)
    os.makedirs(key_dir, exist_ok=True)
    ImageOps.fit(img, (1080,1080)).save(os.path.join(key_dir, f'{key}_ig_1080x1080.jpg'), quality=95)
    ImageOps.fit(img, (1080,1920)).save(os.path.join(key_dir, f'{key}_story_1080x1920.jpg'), quality=95)
    ImageOps.fit(img, (1500,500)).save(os.path.join(key_dir, f'{key}_banner_1500x500.jpg'), quality=95)
    ImageOps.fit(img, (4960,7016)).save(os.path.join(key_dir, f'{key}_A2_4960x7016.jpg'), quality=90)

captions = {
 'factory': {
  'en':'They build our idols. See the machine — not the myth.',
  'es':'Fabrican nuestros ídolos. Ve la máquina — no el mito.',
  'fr':'Ils fabriquent nos idoles. Regarde la machine — pas le mythe.',
  'de':'Sie bauen unsere Idole. Schau die Maschine — nicht den Mythos.',
  'ru':'Они создают наших кумиров. Смотри на машину — не на миф.',
  'zh':'他们打造我们的偶像。看清机器——别被神话蒙蔽。',
  'ar':'هم يصنعون أصنامنا. انظر إلى الآلة — ليس إلى الأسطورة.',
  'hi':'वे हमारे بت बनाते हैं। मशीन देखो — मिथक नहीं.',
  'el':'Φτιάχνουν τα είδωλά μας. Δες τη μηχανή — όχι το μύθο.'
 },
 'spell': {
  'en':'The feed is the altar. What keeps you scrolling keeps you captive.',
  'es':'El feed es el altar. Lo que te mantiene desplazando te mantiene cautivo.',
  'fr':'Le fil est l’autel. Ce qui te fait scroller te maintient captif.',
  'de':'Der Feed ist der Altar. Was dich scrollen hält, hält dich gefangen.',
  'ru':'Лента — это алтарь. То, что заставляет тебя листать, держит тебя в плену.',
  'zh':'信息流即祭坛。让你不停刷屏的就是你的枷锁。',
  'ar':'الخلاصة هي المذبح. ما يجعلك تتصفح يبقِيك أسيراً.',
  'hi':'फ़ीड ही वेदी है। जो आपको स्क्रोल कराता है, वही आपको बँधक बनाता है。',
  'el':'Το feed είναι ο βωμός. Αυτό που σε κρατά να σκρολάρεις σε κρατά δέσμιο.'
 },
 'crack': {
  'en':'One crack breaks the illusion. The rest is choice.',
  'es':'Una grieta rompe la ilusión. El resto es elección.',
  'fr':'Une fissure brise l’illusion. Le reste est un choix.',
  'de':'Ein Riss bricht die Illusion. Der Rest ist eine Wahl.',
  'ru':'Одна трещина разрушает иллюзию. Остальное — выбор.',
  'zh':'一道裂缝击碎幻象。其余由你选择。',
  'ar':'شق واحد يكسر الوهم. الباقي اختيارك.',
  'hi':'एक दरार भ्रम तोड़ देती है। बाकी तुम्हारे फैसले पर है।',
  'el':'Μια ρωγμή σπάει την ψευδαίσθηση. Τα υπόλοιπα είναι επιλογή.'
 },
 'truelight': {
  'en':'When the gaze rises, the idols collapse. Choose the light.',
  'es':'Cuando la mirada se eleva, los ídolos colapsan. Elige la luz.',
  'fr':'Quand le regard s’élève, les idoles s’effondrent. Choisis la lumière.',
  'de':'Wenn der Blick aufsteigt, stürzen die Idole. Wähle das Licht.',
  'ru':'Когда взгляд поднимается — идолы рушатся. Выбери свет.',
  'zh':'当目光抬起，偶像便崩塌。选择光明。',
  'ar':'عندما يرتفع البصر تنهار الأصنام. اختر النور.',
  'hi':'जब नज़र उठेगी, بت ढह जाएंगे। प्रकाश चुनें।',
  'el':'Όταν το βλέμμα ανεβαίνει, τα είδωλα καταρρέουν. Διάλεξε το φως.'
 }
}
with open(os.path.join(OUT_DIR,'captions.json'),'w',encoding='utf-8') as f:
    json.dump(captions, f, ensure_ascii=False, indent=2)

with open(os.path.join(OUT_DIR,'breakthespell.html'),'w',encoding='utf-8') as f:
    f.write("<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>Break the Spell</title></head><body><h1>Break the Spell — A Global Awakening</h1><p>Use /breakthespell/&lt;lang&gt;/ for localized pages.</p></body></html>")

for code,label in langs:
    dd = os.path.join(OUT_DIR,'breakthespell',code)
    os.makedirs(dd, exist_ok=True)
    caption_factory = captions['factory'].get(code, captions['factory']['en'])
    html = f"<!doctype html><html lang='{code}'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{label} - Break the Spell</title></head><body><h1>{caption_factory}</h1><p>Images in /images/</p></body></html>"
    with open(os.path.join(dd,'index.html'),'w',encoding='utf-8') as fh:
        fh.write(html)

with open(os.path.join(OUT_DIR,'_redirects'),'w',encoding='utf-8') as f:
    for code,_ in langs:
        f.write(f"/breakthespell/{code}    /breakthespell/{code}/    200\n")

start_date = (datetime.utcnow() + timedelta(days=1)).date()
rows = []
for i,key in enumerate(['factory','spell','crack','truelight']):
    post_date = start_date + timedelta(days=i)
    for code,_ in langs:
        rows.append({'date':post_date.isoformat(), 'time':'16:00', 'timezone':'Asia/Amman',
                     'language':code, 'text':f'[[{code.upper()} caption for {key}]] clarity.info/breakthespell #BreakTheSpell #WakeUp #LookUp #DigitalFreedom',
                     'media':f'images/{key}/{key}_ig_1080x1080.jpg'})
csv_path = os.path.join(OUT_DIR,'scheduling_template.csv')
with open(csv_path,'w',newline='',encoding='utf-8') as cf:
    w=csv.DictWriter(cf, fieldnames=['date','time','timezone','language','text','media'])
    w.writeheader()
    for r in rows:
        w.writerow(r)

deploy_sh = f"""#!/bin/bash
REPO="{REPO_URL}"
BRANCH="breakthespell/add-campaign-$(date +%Y%m%d%H%M)"
git clone "$REPO" tmp-clarity-repo
cd tmp-clarity-repo
git checkout -b "$BRANCH"
cp -r ../{OUT_DIR}/* ./
git add -A
git commit -m "Add BreakTheSpell campaign assets"
git push origin "$BRANCH"
echo "Now create PR: gh pr create --title 'Add BreakTheSpell campaign' --body 'Adds multilingual campaign assets' --base main --head $BRANCH"
"""
with open(os.path.join(OUT_DIR,'deploy_pr_instructions.sh'),'w',encoding='utf-8') as f:
    f.write(deploy_sh)

with open(os.path.join(OUT_DIR,'README.txt'),'w',encoding='utf-8') as f:
    f.write("BreakTheSpell local package created. Run deploy_pr_instructions.sh after editing REPO if needed.\n")

zip_name = "final_breakthespell_local.zip"
zip_path = os.path.join(".", zip_name)
with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED) as zf:
    for root,dirs,files in os.walk(OUT_DIR):
        for file in files:
            full = os.path.join(root,file)
            rel = os.path.relpath(full, OUT_DIR)
            zf.write(full, rel)

print("Done. Created:", zip_path)
