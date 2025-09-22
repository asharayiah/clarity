
(function(){
  try{
    var pref=(navigator.language||'en').toLowerCase();
    var map={'en':'EN','ar':'AR','es':'ES','fr':'FR','pt':'PT','de':'DE','tr':'TR','id':'ID','hi':'HI','ur':'UR','sw':'SW','ru':'RU','zh':'ZH','zh-cn':'ZH','zh-tw':'ZH'};
    var lang=map[pref]||map[pref.split('-')[0]]||'EN';
    var target='pages/clarity_landing_'+lang+'.html';
    if(!location.pathname.includes('/pages/')){ window.location.href=target; }
  }catch(e){}
})();
