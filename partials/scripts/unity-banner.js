<script>
async function loadUnityBanner(title, intent, targetId='unityBanner'){
  try{
    const res = await fetch('/partials/unity-banner.html', {cache:'no-cache'});
    const tpl = await res.text();
    const html = tpl.replace(/\{\{PAGE_TITLE\}\}/g, title)
                    .replace(/\{\{PAGE_INTENT\}\}/g, intent);
    const host = document.getElementById(targetId);
    if(host) host.innerHTML = html;
  }catch(e){ console.error('Unity banner load failed:', e); }
}
</script>
