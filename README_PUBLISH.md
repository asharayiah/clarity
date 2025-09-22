# Clarity — c‑l‑a‑r‑i‑t‑y.info

This folder is a complete static website in 13 languages with all visuals.

## Structure
- `index.html` — auto‑detects language and redirects to the right landing page
- `pages/clarity_landing_<LANG>.html` — per‑language pages (EN, AR, ES, FR, PT, DE, TR, ID, HI, UR, SW, RU, ZH)
- `pages/clarity_counterfactual_1918.html` — thought experiment page
- `images/zakah_visuals/*.png` — layman visuals
- `images/counterfactual_1918/*.png` — counterfactual visuals
- `images/og/og_<LANG>.png` — social share images
- `assets/style.css`, `assets/lang.js`
- `.nojekyll`, `CNAME`, `robots.txt`, `sitemap.xml`

## Publish to your Git repository

### Option A — GitHub Pages (fast)
1. Create a repo, e.g. **clarity-website**.
2. Put the contents of this folder in the repo **root** (do not nest under another folder).
3. Commit & push:
   ```bash
   git init
   git add .
   git commit -m "Publish Clarity site"
   git branch -M main
   git remote add origin https://github.com/<YOU>/clarity-website.git
   git push -u origin main
   ```
4. In GitHub → Settings → **Pages**:
   - Source: **Deploy from a branch**
   - Branch: **main** / **root**
5. Custom domain: set **c-l-a-r-i-t-y.info** in GitHub Pages → Custom domain, and add DNS **CNAME** for `@` (root) pointing to `<your-username>.github.io`.
6. The provided `CNAME` file ensures the domain sticks on deploy.

### Option B — Netlify (drag‑and‑drop)
1. Go to Netlify → New site from Git → connect your repo.
2. Framework: None (static). Build command: none. Publish directory: `/`.
3. Set custom domain to **c-l-a-r-i-t-y.info** in Netlify and add the DNS records it shows (CNAME or A/AAAA).

### Option C — Vercel
1. Import the repo into Vercel.
2. Project: static. Output directory: `/`.
3. Set custom domain to **c-l-a-r-i-t-y.info** and verify DNS.

## Local preview
You can serve locally to test:
```bash
python3 -m http.server 8080
# then open http://localhost:8080
```

Bismillah — may this be a lens of mercy and justice for all.
