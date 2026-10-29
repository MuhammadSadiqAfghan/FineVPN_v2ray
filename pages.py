# FineVPN_v2ray — Login, dashboard, and public subscription pages.

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>FineVPN_v2ray — ورود امن</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#09090b;--panel:#121217;--border:rgba(255,255,255,.08);
  --accent:#10b981;--accent-hover:#059669;--text:#f4f4f5;--muted:#a1a1aa;
  --font:'Vazirmatn',sans-serif;
}
body{
  min-height:100vh;display:flex;align-items:center;justify-content:center;
  background:radial-gradient(ellipse at 50% 20%, rgba(16,185,129,0.15), transparent 45%), var(--bg);
  font-family:var(--font);color:var(--text);padding:20px;
}
.card{
  width:100%;max-width:400px;background:var(--panel);border:1px solid var(--border);
  border-radius:24px;padding:36px 28px;box-shadow:0 25px 60px rgba(0,0,0,0.5);
  backdrop-filter:blur(16px);
}
.brand{text-align:center;margin-bottom:28px}
.brand-logo{
  width:56px;height:56px;border-radius:16px;background:linear-gradient(135deg,#10b981,#047857);
  display:flex;align-items:center;justify-content:center;margin:0 auto 14px;
  color:#fff;font-size:26px;box-shadow:0 8px 24px rgba(16,185,129,0.3);
}
.brand-title{font-size:22px;font-weight:800;color:#fff;margin-bottom:4px}
.brand-sub{font-size:12px;color:var(--muted)}
.fg{margin-bottom:18px}
.fl{display:block;font-size:12px;font-weight:600;color:var(--muted);margin-bottom:7px}
.fi-wrap{position:relative;display:flex;align-items:center}
.fi-wrap i{position:absolute;right:14px;color:#71717a;font-size:18px;pointer-events:none}
.fi{
  width:100%;padding:12px 42px 12px 14px;background:rgba(255,255,255,0.04);
  border:1px solid var(--border);border-radius:12px;color:#fff;
  font-family:inherit;font-size:13.5px;outline:none;transition:all .2s;
}
.fi:focus{border-color:var(--accent);background:rgba(255,255,255,0.07);box-shadow:0 0 0 3px rgba(16,185,129,0.15)}
.btn-p{
  width:100%;padding:13px;border-radius:12px;border:none;background:linear-gradient(135deg,#10b981,#059669);
  color:#fff;font-family:inherit;font-size:14px;font-weight:700;cursor:pointer;
  display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 8px 20px rgba(16,185,129,0.3);
  transition:all .2s;margin-top:8px;
}
.btn-p:hover{transform:translateY(-1px);box-shadow:0 10px 25px rgba(16,185,129,0.4)}
.hint-box{
  margin-top:20px;padding:12px 14px;border-radius:12px;background:rgba(16,185,129,0.06);
  border:1px solid rgba(16,185,129,0.15);display:flex;align-items:center;justify-content:space-between;
  font-size:11.5px;color:var(--accent);cursor:pointer;transition:background .2s;
}
.hint-box:hover{background:rgba(16,185,129,0.12)}
.err-box{
  margin-top:14px;padding:10px 14px;border-radius:10px;background:rgba(239,68,68,0.12);
  border:1px solid rgba(239,68,68,0.25);color:#f87171;font-size:12px;display:none;align-items:center;gap:8px;
}
.vol-steps{display:flex;flex-direction:column;gap:10px}
.vol-step{display:flex;gap:12px;align-items:flex-start;padding:10px 12px;background:var(--card, #0d1c18);border:1px solid var(--line, rgba(255,255,255,.07));border-radius:12px}
.vs-n{flex:0 0 26px;height:26px;border-radius:50%;background:linear-gradient(135deg,#10B981,#047857);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px}
.vs-s{font-size:11.5px;color:var(--t3,#7d8b86);margin-top:2px}
.vol-step code{background:rgba(16,185,129,.14);color:#34d399;padding:1px 6px;border-radius:5px;font-size:11.5px}
.vol-note{margin-top:12px;font-size:11.5px;color:#93a59f;display:flex;gap:7px;align-items:flex-start;padding:10px;background:rgba(59,130,246,.08);border:1px solid rgba(59,130,246,.25);border-radius:10px}
.vol-note i{color:#60a5fa;margin-top:1px}
.cat-filter{width:auto;min-width:130px;font-size:11.5px;padding:6px 10px;border-radius:9px}
.cat-pill{display:inline-flex;align-items:center;gap:5px;font-size:10.5px;padding:2px 9px;border-radius:20px;font-weight:600;white-space:nowrap}
.cat-dot{width:7px;height:7px;border-radius:50%;flex:0 0 7px}
.cat-mgr{display:flex;flex-direction:column;gap:8px}
.cat-mgr-row{display:flex;gap:8px;align-items:center}
.cat-mgr-row input{flex:1}
.tel-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:10px}
.tel-tile{background:var(--card,#0d1c18);border:1px solid var(--line,rgba(255,255,255,.07));border-radius:12px;padding:12px}
.tel-tile .tt-l{font-size:10.5px;color:var(--t3,#7d8b86);display:flex;align-items:center;gap:5px}
.tel-tile .tt-v{font-size:17px;font-weight:700;color:var(--t1,#e8f5f0);margin-top:4px;direction:ltr}
.tel-tile .tt-s{font-size:10px;color:var(--t3,#7d8b86);margin-top:2px}
.tel-bar{height:5px;border-radius:3px;background:rgba(255,255,255,.08);margin-top:7px;overflow:hidden}
.tel-bar i{display:block;height:100%;border-radius:3px;background:linear-gradient(90deg,#10B981,#34d399);transition:width .5s}
.cat-del{padding:5px 10px;font-size:11px}
.badge.b-ok{background:rgba(16,185,129,.15);color:#34d399;border:1px solid rgba(16,185,129,.4)}
.badge.b-warn{background:rgba(245,158,11,.15);color:#fbbf24;border:1px solid rgba(245,158,11,.4)}

/* FineVPN_v2ray login — polished glass, starlight and gold */
:root{--bg:#030713;--panel:rgba(12,20,42,.72);--border:rgba(240,196,91,.22);--accent:#f0c45b;--accent-hover:#d4a333;--text:#f5f4ff;--muted:#a7b0d0}
html,body{min-height:100%;background-color:#030713}
body{background-color:#030713;background-image:
 radial-gradient(1px 1px at 17px 23px,rgba(255,255,255,.86) 55%,transparent 100%),
 radial-gradient(1.4px 1.4px at 71px 101px,rgba(255,225,164,.72) 55%,transparent 100%),
 linear-gradient(rgba(2,6,18,.78),rgba(2,6,18,.83)),url("https://i.ibb.co/39zWtJzS/1791731497906.jpg");
 background-size:109px 109px,173px 173px,100% 100%,min(66vw,680px) auto;background-position:0 0,35px 61px,center,center;
 background-repeat:repeat,repeat,no-repeat,no-repeat;background-attachment:fixed;font-family:'Vazirmatn',sans-serif}
.card{max-width:430px;background:linear-gradient(145deg,rgba(18,29,57,.83),rgba(6,12,29,.77));border:1px solid rgba(240,196,91,.26);border-radius:28px;box-shadow:0 30px 90px rgba(0,0,0,.48),0 0 36px rgba(240,196,91,.08);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px)}
.brand-logo{width:80px;height:80px;border-radius:50%;background:rgba(240,196,91,.1);border:1px solid rgba(255,220,125,.45);box-shadow:0 0 28px rgba(240,196,91,.2);overflow:hidden}
.brand-logo img{width:100%;height:100%;object-fit:cover;display:block}
.brand-title{color:#fff0bd;font-size:22px;letter-spacing:.02em}
.brand-sub{color:#b5bfdc;line-height:1.8}
.fl{color:#c9cde0}
.fi{background:rgba(4,9,24,.58);border-color:rgba(240,196,91,.2);color:#f5f4ff}
.fi:focus{border-color:#f0c45b;background:rgba(4,9,24,.78);box-shadow:0 0 0 3px rgba(240,196,91,.12)}
.fi-wrap i{color:#e4c36f}
.btn-p{background:linear-gradient(135deg,#fff0b8 0%,#f1ca62 42%,#bd8a25 100%);color:#211805;box-shadow:0 0 20px rgba(240,196,91,.18),0 8px 22px rgba(0,0,0,.24);border:1px solid rgba(255,233,164,.6)}
.btn-p:hover{background:linear-gradient(135deg,#fff6d6 0%,#ffe18a 45%,#d7a63a 100%);box-shadow:0 0 28px rgba(240,196,91,.3)}
.login-contact{border-top:1px solid rgba(240,196,91,.17);margin-top:22px;padding-top:17px;text-align:center}
.login-provider{font-size:11.5px;color:#c8cce0}
.login-provider strong{color:#ffe5a0;font-weight:800}
.login-signature{font-size:12px;color:#f4d98c;letter-spacing:.04em;margin-top:4px}
.login-links{display:flex;justify-content:center;gap:9px;flex-wrap:wrap;margin-top:13px}
.login-links a{display:inline-flex;align-items:center;gap:6px;padding:8px 10px;border:1px solid rgba(240,196,91,.23);border-radius:11px;background:rgba(240,196,91,.07);color:#ffe5a0;text-decoration:none;font-size:11px;font-weight:700}
.login-links a:hover{background:rgba(240,196,91,.16)}.login-links i{font-size:16px}
@media(max-width:420px){body{padding:12px}.card{padding:28px 19px;border-radius:22px}.brand-logo{width:72px;height:72px}}
</style>
</head>
<body>
<div class="card">
  <div class="brand">
    <div class="brand-logo"><img src="https://i.ibb.co/39zWtJzS/1791731497906.jpg" alt="FineVPN_v2ray"></div>
    <div class="brand-title">FineVPN_v2ray</div>
    <div class="brand-sub">ورود امن به پنل مدیریت FineVPN_v2ray</div>
  </div>
  <form id="lf">
    <div class="fg">
      <label class="fl">نام کاربری</label>
      <div class="fi-wrap"><input type="text" id="username" class="fi" placeholder="نام کاربری..." required autocomplete="username"><i class="ti ti-user"></i></div>
    </div>
    <div class="fg">
      <label class="fl">رمز عبور</label>
      <div class="fi-wrap"><input type="password" id="password" class="fi" placeholder="••••••••" autocomplete="current-password"><i class="ti ti-lock"></i></div>
    </div>
    <button type="submit" class="btn-p" id="lbtn"><i class="ti ti-login"></i> <span>ورود به پنل مدیریت</span></button>
    <div class="err-box" id="err-box"><i class="ti ti-alert-circle"></i><span id="err-text">ورود ناموفق</span></div>
  </form>
  <div class="login-contact">
    <div class="login-provider">ارائه‌دهنده: <strong>مـحـمـدصـادق افـغـان</strong></div>
    <div class="login-signature">𝑀𝑢ℎ𝑎𝑚𝑚𝑎𝑑𝒔𝒂𝒅𝒊𝒒</div>
    <div class="login-links"><a href="https://t.me/sadiq_AFG1" target="_blank" rel="noopener noreferrer"><i class="ti ti-brand-telegram"></i> پشتیبانی @sadiq_AFG1</a></div>
  </div>
</div>
<script>
document.getElementById('lf').addEventListener('submit',async(e)=>{
  e.preventDefault();
  const b=document.getElementById('lbtn'),eb=document.getElementById('err-box');
  eb.style.display='none';
  const password=document.getElementById('password').value.trim();
  if(!password){eb.style.display='flex';document.getElementById('err-text').textContent='رمز را وارد کنید';document.getElementById('password').focus();return;}
  b.disabled=true;b.innerHTML='<i class="ti ti-loader"></i> <span>در حال بررسی...</span>';
  try{
    const r=await fetch('/api/login',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({username:document.getElementById('username').value.trim(),password:document.getElementById('password').value.trim()})
    });
    const d=await r.json();
    if(d.ok){location.href='/dashboard';}
    else{
      eb.style.display='flex';
      document.getElementById('err-text').textContent=d.detail||'نام کاربری یا رمز عبور اشتباه است';
      b.disabled=false;b.innerHTML='<i class="ti ti-login"></i> <span>ورود به پنل مدیریت</span>';
    }
  }catch(err){
    eb.style.display='flex';
    document.getElementById('err-text').textContent='خطا در اتصال به سرور';
    b.disabled=false;b.innerHTML='<i class="ti ti-login"></i> <span>ورود به پنل مدیریت</span>';
  }
});
</script>
</body>
</html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FineVPN_v2ray</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#070d0b;--bg2:#0b1613;--bg3:#0f1f1a;
  --card:#0d1c18;--card-b:rgba(16,185,129,0.14);--card-bh:rgba(16,185,129,0.32);
  --accent:#10B981;--accent2:#34D399;--accent-d:rgba(16,185,129,0.12);
  --green:#10B981;--green-bg:rgba(16,185,129,0.1);--green-t:#34D399;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.1);--red-t:#F87171;
  --amber:#F59E0B;--amber-bg:rgba(245,158,11,0.1);--amber-t:#FCD34D;
  --purple:#10B981;--purple-bg:rgba(16,185,129,0.1);
  --t1:#E8F4FF;--t2:#7BAED4;--t3:#3D6B8E;
  --sidebar-w:248px;--radius:16px;
  --shadow:0 4px 24px rgba(0,0,0,0.35);
}
[data-theme="light"]{
  --bg:#F0FDF9;--bg2:#E1FBEF;--bg3:#D2F5E6;
  --card:#FFFFFF;--card-b:rgba(16,185,129,0.15);--card-bh:rgba(16,185,129,0.35);
  --accent:#10B981;--accent2:#047857;--accent-d:rgba(37,99,235,0.08);
  --green:#059669;--green-bg:rgba(5,150,105,0.08);--green-t:#065F46;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#991B1B;
  --amber:#D97706;--amber-bg:rgba(217,119,6,0.08);--amber-t:#92400E;
  --purple:#059669;--purple-bg:rgba(5,150,105,0.08);
  --t1:#0F172A;--t2:#334155;--t3:#64748B;
  --shadow:0 4px 20px rgba(0,0,0,0.1);
}
html,body{height:100%;overflow-x:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background .3s,color .3s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg2);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .25s cubic-bezier(.4,0,.2,1),background .3s,border-color .3s}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--card-b)}
.logo-img{width:38px;height:38px;border-radius:50%;overflow:hidden;border:1px solid var(--card-b);box-shadow:0 0 14px rgba(16,185,129,.35),0 0 8px rgba(16,185,129,.25);flex-shrink:0}
.logo-img img{width:100%;height:100%;object-fit:cover}
.logo-name{font-size:13.5px;font-weight:700;color:var(--t1)}
.logo-sub{font-size:10px;color:var(--t3);margin-top:1px}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;align-items:center;justify-content:center;cursor:pointer}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 14px 4px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .15s;margin:1px 6px}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--accent-d);color:var(--t2)}
.nav-it.on{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600}
.nav-badge{margin-right:auto;background:rgba(16,185,129,0.15);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.15s;margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:var(--t1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.2);cursor:pointer;width:100%;transition:.15s;margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.2)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:var(--bg2);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px;transition:background .3s}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:28px;height:28px;border-radius:50%;overflow:hidden;box-shadow:0 0 8px rgba(16,185,129,.35)}
.mob-logo img{width:100%;height:100%;object-fit:cover}
.mob-title{color:var(--t1);font-size:13px;font-weight:700}
.mob-right{display:flex;gap:6px}
.menu-btn{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;color:#fff;width:36px;height:36px;border-radius:10px;font-size:18px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;box-shadow:0 4px 14px rgba(16,185,129,.35)}
.menu-btn:hover{transform:scale(1.08);box-shadow:0 6px 18px rgba(16,185,129,.5)}
.menu-btn:active{transform:scale(.94)}
.menu-btn i{transition:transform .25s}
.menu-btn.open i{transform:rotate(90deg)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .25s}
.pg{display:none}
.pg.on{display:block;animation:fi .2s ease}
@keyframes fi{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:18px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:8px;letter-spacing:-.02em}
.tb-title i{color:var(--accent);font-size:20px}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-purple{background:var(--purple-bg);color:#34D399}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}
.metric{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:17px 17px 14px;transition:all .2s;position:relative;overflow:hidden;cursor:default}
.metric::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--accent);opacity:0;transition:.2s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.metric:hover::after{opacity:1}
.metric.suc::after{background:var(--green)}
.metric.dan::after{background:var(--red)}
/* ══════ صفحه ترافیک - ریدیزاین ══════ */
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:13px;margin-bottom:18px}
.traf-main-stat{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:20px;padding:22px 24px;position:relative;overflow:hidden}
.traf-main-stat::before{content:'';position:absolute;top:-50px;left:-50px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.traf-main-label{font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:10px;position:relative;z-index:1}
.traf-main-val{font-size:34px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;display:flex;align-items:baseline;gap:6px;position:relative;z-index:1}
.traf-main-val span{font-size:14px;font-weight:500;color:var(--t3)}
.traf-trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 10px;border-radius:20px;margin-top:12px;position:relative;z-index:1}
.traf-trend.up{background:var(--green-bg);color:var(--green-t)}
.traf-trend.down{background:var(--red-bg);color:var(--red-t)}
.traf-mini{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:18px 19px;display:flex;flex-direction:column;justify-content:space-between;transition:.2s}
.traf-mini:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.traf-mini-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:15px}
.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber)}
.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}
.traf-mini-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.traf-mini-val{font-size:21px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.traf-mini-sub{font-size:9.5px;color:var(--t3);margin-top:3px}

.traf-chart-card{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:22px 24px 18px;box-shadow:var(--shadow);margin-bottom:16px}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:10px}
.traf-chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.traf-chart-title i{color:var(--accent);font-size:18px}
.traf-chart-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.traf-legend{display:flex;gap:14px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:10.5px;color:var(--t2);font-weight:600}
.traf-legend-dot{width:8px;height:8px;border-radius:3px}
.traf-range-tabs{display:flex;gap:4px;background:var(--accent-d);padding:3px;border-radius:10px;border:1px solid var(--card-b)}
.traf-range-tab{padding:6px 13px;border-radius:8px;font-size:10.5px;font-weight:700;color:var(--t3);cursor:pointer;transition:.15s;border:none;background:transparent;font-family:inherit}
.traf-range-tab.on{background:var(--accent);color:#fff;box-shadow:0 2px 8px rgba(16,185,129,.35)}
.traf-chart-body{height:320px;margin-top:14px;position:relative}

@media(max-width:900px){.traf-hero{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.traf-hero{grid-template-columns:1fr}.traf-chart-body{height:260px}}
.m-icon{width:34px;height:34px;border-radius:8px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent);font-size:17px}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}
.vless-box{background:linear-gradient(135deg,var(--bg3) 0%,var(--bg2) 100%);border:1px solid var(--card-b);border-radius:18px;padding:20px 22px;margin-bottom:18px;box-shadow:var(--shadow);position:relative;overflow:hidden;transition:background .3s}
.vless-box::before{content:'';position:absolute;top:-50px;left:-50px;width:180px;height:180px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px}
.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--accent);font-size:15px}
.vl-code{background:rgba(0,0,0,.18);border:1px solid var(--card-b);border-radius:9px;padding:13px 15px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.8;letter-spacing:.01em}
[data-theme="light"] .vl-code{background:rgba(0,0,0,.04)}
.vl-actions{display:flex;gap:8px;margin-top:13px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:12px;font-weight:500;border-radius:9px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}
.btn i{font-size:13px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-o:hover{background:var(--accent-d);border-color:rgba(16,185,129,.3)}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(16,185,129,.15)}
.btn-g:hover{background:rgba(16,185,129,.22)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.2)}
.btn-d:hover{background:rgba(239,68,68,.2)}
.btn-pur{background:var(--purple-bg);color:#34D399;border:1px solid rgba(16,185,129,.2)}
.btn-pur:hover{background:rgba(16,185,129,.22)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,.2)}
.btn-amber:hover{background:rgba(245,158,11,.22)}
.btn-sm{padding:5px 9px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:5px}
.card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:border-color .2s,background .3s}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:12.5px;font-weight:700;color:var(--t1);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent)}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid rgba(16,185,129,0.05);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}
.ch{position:relative;height:230px}
.ch-lg{position:relative;height:330px}
.ch-sm{position:relative;height:185px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
.tog{width:19px;height:34px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;bottom:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on{background:var(--green)}
.tog.on::after{bottom:18px}
.form-row{display:flex;gap:9px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:5px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.fi,.fs{padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.15s;min-width:100px}
[data-theme="light"] .fi,[data-theme="light"] .fs{background:rgba(0,0,0,.04)}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:rgba(16,185,129,.45);background:rgba(0,0,0,.25);box-shadow:0 0 0 3px rgba(16,185,129,.08)}
.fs option{background:var(--bg2)}
[data-theme="light"] .fs option{background:#fff}
.cl{background:var(--accent-d);border:1px solid rgba(16,185,129,.15);border-radius:10px;padding:11px 13px;font-size:11px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(245,158,11,.2);color:var(--amber-t)}
/* ══════ پنل ساخت کانفیگ - طراحی جدید ══════ */
.create-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 55%);border:1px solid var(--card-b);border-radius:22px;padding:0;overflow:hidden;box-shadow:var(--shadow);margin-bottom:16px;position:relative}
.create-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:220px;height:220px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.cp-head{display:flex;align-items:center;gap:13px;padding:22px 24px 18px;position:relative;z-index:1}
.cp-head-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 18px rgba(16,185,129,.35)}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:2px}
.cp-body{padding:2px 24px 22px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:14px;padding:14px 16px}
[data-theme="light"] .cp-block{background:rgba(37,99,235,.03)}
.cp-block-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:11px}
.cp-block-label i{color:var(--accent);font-size:14px}
.cp-input-full{width:100%;padding:10px 13px;border-radius:10px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
[data-theme="light"] .cp-input-full{background:#fff}
.cp-input-full:focus{border-color:rgba(16,185,129,.5);box-shadow:0 0 0 3px rgba(16,185,129,.1)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:9px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.chip{font-size:10.5px;font-weight:700;padding:5px 12px;border-radius:8px;background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;white-space:nowrap}
.chip:hover{background:rgba(16,185,129,.18);color:var(--accent2)}
.chip.active{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 3px 10px rgba(16,185,129,.35)}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.proto-card{border:1.5px solid var(--card-b);border-radius:13px;padding:13px 12px;cursor:pointer;transition:.18s;text-align:center;position:relative;background:rgba(0,0,0,.1)}
[data-theme="light"] .proto-card{background:#fff}
.proto-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(16,185,129,.1)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-check{position:absolute;top:7px;left:7px;width:16px;height:16px;border-radius:50%;background:var(--accent);color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:.18s}
.proto-card-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;margin:0 auto 8px}
.proto-card.active .proto-card-icon{background:var(--accent);color:#fff}
.proto-card-title{font-size:11px;font-weight:800;color:var(--t1)}
.proto-card-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:15px;flex-shrink:0}
.cp-submit-btn{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;border-radius:13px;padding:13px 26px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px rgba(16,185,129,.35);transition:.18s;white-space:nowrap}
.cp-submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(16,185,129,.45)}
.cp-submit-btn:active{transform:translateY(0) scale(.98)}
@media(max-width:760px){
  .cp-row{grid-template-columns:1fr}
  .proto-cards{grid-template-columns:1fr}
  .cp-footer{flex-direction:column;align-items:stretch}
  .cp-submit-btn{justify-content:center}
}
/* ══════ پنل اطلاعات سرور ══════ */
.srv-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.srv-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.srv-hero{display:flex;align-items:center;gap:14px;padding:22px 24px;position:relative;z-index:1;border-bottom:1px solid var(--card-b)}
.srv-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(16,185,129,.35)}
.srv-hero-text{flex:1;min-width:0}
.srv-hero-domain{font-size:15px;font-weight:800;color:var(--t1);word-break:break-all}
.srv-hero-sub{font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:11px;padding:20px 22px 22px;position:relative;z-index:1}
.srv-tile{display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;transition:.18s}
[data-theme="light"] .srv-tile{background:rgba(37,99,235,.03)}
.srv-tile:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.srv-tile-icon{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.srv-tile-val{font-size:12px;font-weight:700;color:var(--t1);word-break:break-word}

/* ══════ پنل تغییر رمز ══════ */
.pw-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.pw-panel::before{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--purple-bg),transparent 70%);pointer-events:none}
.pw-hero{display:flex;align-items:center;gap:14px;padding:22px 24px 18px;position:relative;z-index:1}
.pw-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#047857);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(16,185,129,.35)}
.pw-hero-text{flex:1;min-width:0}
.pw-hero-title{font-size:15px;font-weight:800;color:var(--t1)}
.pw-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.pw-body{padding:2px 24px 22px;position:relative;z-index:1}
.pw-field{position:relative;margin-bottom:13px}
.pw-field label{display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}
.pw-input{width:100%;padding:11px 42px 11px 14px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
[data-theme="light"] .pw-input{background:#fff}
.pw-input:focus{border-color:rgba(16,185,129,.5);box-shadow:0 0 0 3px rgba(16,185,129,.1)}
.pw-eye{position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}
.pw-eye:hover{color:var(--purple)}
.pw-strength{height:4px;border-radius:3px;background:var(--accent-d);margin-top:8px;overflow:hidden;display:flex;gap:3px}
.pw-strength-seg{flex:1;height:100%;border-radius:3px;background:rgba(100,116,139,.2);transition:.25s}
.pw-strength-label{font-size:9.5px;color:var(--t3);margin-top:5px;display:flex;align-items:center;gap:5px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px;margin-bottom:16px}
.pw-req{font-size:9.5px;padding:4px 10px;border-radius:7px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.18s}
.pw-req.met{background:var(--green-bg);color:var(--green-t)}
.pw-submit{width:100%;justify-content:center;background:linear-gradient(135deg,var(--purple),#047857);color:#fff;border:none;border-radius:12px;padding:12px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 18px rgba(16,185,129,.32);transition:.18s}
.pw-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(16,185,129,.42)}
.pw-submit:active{transform:translateY(0) scale(.98)}

/* ══════ اتصالات فعال - نسخه پیشرفته ══════ */
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:18px}
.conn-hero-tile{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:16px 18px;position:relative;overflow:hidden;transition:.2s}
.conn-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.conn-hero-tile::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--green),transparent)}
.conn-hero-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;margin-bottom:10px}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--accent-d);color:var(--accent)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber)}
.conn-hero-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.conn-hero-val{font-size:21px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em}
.conn-hero-unit{font-size:11px;color:var(--t3);font-weight:500}

.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.conn-toolbar-title{font-size:12px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}
.conn-toolbar-title i{color:var(--green);font-size:15px}
.conn-live-badge{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:var(--green-t);background:var(--green-bg);padding:5px 12px;border-radius:20px;border:1px solid rgba(16,185,129,.2)}
.conn-live-dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite}

.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.conn-card-v2{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:0;overflow:hidden;transition:all .22s cubic-bezier(.4,0,.2,1);position:relative}
.conn-card-v2:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 14px 32px rgba(0,0,0,.22)}
.conn-card-v2-glow{position:absolute;top:-40px;left:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(16,185,129,.1),transparent 70%);pointer-events:none}
.conn-card-v2-top{display:flex;align-items:center;gap:12px;padding:16px 17px 13px;position:relative;z-index:1}
.conn-avatar{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--green),#0D9668);display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0;position:relative;box-shadow:0 4px 14px rgba(16,185,129,.3)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:16px;border:1.5px solid var(--green);opacity:.4;animation:breathe2 2.4s ease-in-out infinite}
@keyframes breathe2{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.12);opacity:0}}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2{font-family:ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.conn-ip-copy{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;display:flex;transition:.15s}
.conn-ip-copy:hover{color:var(--accent)}
.conn-label-v2{font-size:10.5px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-status-pill{font-size:9px;font-weight:800;padding:4px 9px;border-radius:20px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;gap:4px;white-space:nowrap;flex-shrink:0}
.conn-card-v2-divider{height:1px;background:linear-gradient(90deg,transparent,var(--card-b) 15%,var(--card-b) 85%,transparent);margin:0 17px}
.conn-card-v2-body{padding:14px 17px 16px}
.conn-proto-row{margin-bottom:12px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.conn-stat-box{display:flex;align-items:center;gap:8px}
.conn-stat-icon{width:26px;height:26px;border-radius:8px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.conn-stat-icon.time{background:var(--purple-bg);color:var(--purple)}
.conn-stat-text-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.conn-stat-text-val{font-size:11.5px;font-weight:700;color:var(--t1);margin-top:1px}
.conn-duration-track{height:5px;border-radius:4px;background:var(--accent-d);overflow:hidden;position:relative}
.conn-duration-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--green),#3FD79C);position:relative;overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);width:40%;animation:shimmer 1.8s linear infinite}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}

.conn-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:20px}
.conn-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--t3);margin:0 auto 16px}
.conn-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.conn-empty-v2-sub{font-size:11px;color:var(--t3)}

@media(max-width:760px){.conn-hero{grid-template-columns:1fr 1fr}}
@media(max-width:500px){.conn-grid-v2{grid-template-columns:1fr}}

@media(max-width:560px){.srv-tiles{grid-template-columns:1fr}}
.cl.amber i{color:var(--amber)}
.sub-box{background:rgba(16,185,129,.07);border:1px solid rgba(16,185,129,.2);border-radius:10px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:11px}
.sub-url{font-family:ui-monospace,monospace;font-size:10.5px;color:#34D399;word-break:break-all;flex:1}
.spbar{height:4px;border-radius:3px;background:var(--accent-d);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 1s}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty p{font-size:12.5px;margin-top:4px}
/* ══════ گروه‌های ساب - ریدیزاین کامل ══════ */
.subs-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{width:100%;padding:11px 40px 11px 15px;border-radius:12px;border:1px solid var(--card-b);background:var(--card);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
.subs-search input:focus{border-color:rgba(16,185,129,.5);box-shadow:0 0 0 3px rgba(16,185,129,.1)}
.subs-search i{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}

.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:18px}
.sub-card{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:0;overflow:hidden;transition:all .25s cubic-bezier(.4,0,.2,1);position:relative}
.sub-card:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:0 16px 36px rgba(0,0,0,.24)}
.sub-card-top{background:linear-gradient(155deg,var(--purple-bg) 0%,transparent 65%);padding:20px 20px 16px;position:relative}
.sub-card-top::before{content:'';position:absolute;top:-30px;left:-30px;width:130px;height:130px;background:radial-gradient(circle,rgba(16,185,129,.14),transparent 70%);pointer-events:none}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:13px;position:relative;z-index:1}
.sub-card-icon{width:46px;height:46px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#047857);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 16px rgba(16,185,129,.35)}
.sub-card-titles{flex:1;min-width:0}
.sub-card-name-v2{font-size:15.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-desc-v2{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sub-card-lock-badge{flex-shrink:0;width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px}
.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}

.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative;z-index:1;margin-top:16px;background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:13px;overflow:hidden}
[data-theme="light"] .sub-card-stats{background:rgba(5,150,105,.03)}
.sub-card-stat{padding:11px 8px;text-align:center;border-left:1px solid var(--card-b)}
.sub-card-stat:last-child{border-left:none}
.sub-card-stat-val{font-size:15px;font-weight:800;color:var(--t1);line-height:1.2}
.sub-card-stat-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-top:4px}

.sub-card-url-row{margin:14px 20px 0;background:rgba(16,185,129,.08);border:1px dashed rgba(16,185,129,.25);border-radius:11px;padding:9px 12px;display:flex;align-items:center;gap:8px}
.sub-card-url-text{font-family:ui-monospace,monospace;font-size:9.5px;color:#34D399;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-url-copy{background:none;border:none;color:var(--purple);cursor:pointer;font-size:13px;padding:3px;display:flex;flex-shrink:0;transition:.15s}
.sub-card-url-copy:hover{color:#34D399;transform:scale(1.1)}

.sub-card-bottom{padding:14px 20px 18px;display:flex;gap:7px;flex-wrap:wrap}
.sub-card-bottom .btn{flex:1;justify-content:center;min-width:fit-content}

.subs-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:20px;grid-column:1/-1}
.subs-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--purple-bg);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--purple);margin:0 auto 16px}
.subs-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.subs-empty-v2-sub{font-size:11px;color:var(--t3)}

/* ══════ مودال ساخت گروه - نسخه فشرده ══════ */
.modal-v2{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:0;max-width:430px;width:calc(100% - 32px);max-height:92vh;overflow-y:auto;position:relative;animation:fi .2s ease;box-shadow:0 24px 70px rgba(0,0,0,.5)}
.modal-v2-head{background:linear-gradient(155deg,rgba(16,185,129,.14) 0%,transparent 65%);padding:18px 22px 14px;position:relative;overflow:hidden}
.modal-v2-head::before{content:'';position:absolute;top:-50px;left:-50px;width:160px;height:160px;background:radial-gradient(circle,rgba(16,185,129,.2),transparent 70%);pointer-events:none}
.modal-v2-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:9px;font-size:15px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:.15s}
.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(239,68,68,.25)}
.modal-v2-icon{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--purple),#047857);display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;margin-bottom:10px;position:relative;z-index:1;box-shadow:0 8px 18px rgba(16,185,129,.4)}
.modal-v2-title{font-size:15.5px;font-weight:800;color:var(--t1);position:relative;z-index:1;letter-spacing:-.01em}
.modal-v2-sub{font-size:10.5px;color:var(--t3);margin-top:3px;position:relative;z-index:1;line-height:1.6}
.modal-v2-body{padding:16px 22px 20px;border-top:1px solid var(--card-b)}
.modal-v2-field{margin-bottom:11px}
.modal-v2-field label{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.modal-v2-field label i{color:var(--purple);font-size:13px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;right:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none;transition:.15s;z-index:1}
.modal-v2-input{width:100%;padding:9px 38px 9px 13px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
[data-theme="light"] .modal-v2-input{background:rgba(5,150,105,.04)}
.modal-v2-input::placeholder{color:var(--t3)}
.modal-v2-input:focus{border-color:rgba(16,185,129,.55);box-shadow:0 0 0 3px rgba(16,185,129,.12);background:rgba(0,0,0,.28)}
[data-theme="light"] .modal-v2-input:focus{background:#fff}
.modal-v2-input:focus~i{color:var(--purple)}
.modal-v2-hint{background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.18);border-radius:11px;padding:9px 12px;font-size:10px;color:var(--t2);display:flex;gap:7px;align-items:flex-start;line-height:1.6;margin-top:2px}
.modal-v2-hint i{font-size:14px;color:var(--accent);margin-top:1px;flex-shrink:0}
.modal-v2-footer{display:flex;gap:8px;margin-top:15px}
.modal-v2-btn-cancel{flex:.75;justify-content:center;padding:10px;border-radius:11px;background:transparent;border:1px solid var(--card-b);color:var(--t2);font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;transition:.15s;display:flex;align-items:center}
.modal-v2-btn-cancel:hover{background:var(--accent-d);color:var(--t1)}
.modal-v2-btn-submit{flex:1;justify-content:center;padding:10px;border-radius:11px;background:linear-gradient(135deg,var(--purple),#047857);color:#fff;border:none;font-family:inherit;font-size:12px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;box-shadow:0 6px 18px rgba(16,185,129,.4);transition:.18s}
.modal-v2-btn-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(16,185,129,.5)}
.modal-v2-btn-submit:active{transform:translateY(0) scale(.98)}

/* ══════ مودال انتخاب کانفیگ - نسخه پیشرفته ══════ */
.lmodal-head{background:linear-gradient(155deg,var(--accent-d) 0%,transparent 70%);padding:22px 24px 18px;position:relative;border-bottom:1px solid var(--card-b)}
.lmodal-icon-row{display:flex;align-items:center;gap:12px;position:relative;z-index:1}
.lmodal-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;flex-shrink:0;box-shadow:0 6px 16px rgba(16,185,129,.35)}
.lmodal-title-v2{font-size:14.5px;font-weight:800;color:var(--t1)}
.lmodal-sub-v2{font-size:10.5px;color:var(--t3);margin-top:2px}
.lmodal-search{margin-top:14px;position:relative}
.lmodal-search input{width:100%;padding:10px 38px 10px 13px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none}
[data-theme="light"] .lmodal-search input{background:#fff}
.lmodal-search input:focus{border-color:rgba(16,185,129,.5);box-shadow:0 0 0 3px rgba(16,185,129,.1)}
.lmodal-search i{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:11px;position:relative;z-index:1}
.lmodal-qbtn{font-size:10px;font-weight:700;padding:5px 11px;border-radius:8px;background:var(--accent-d);color:var(--accent2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;font-family:inherit}
.lmodal-qbtn:hover{background:rgba(16,185,129,.2)}
.lmodal-count{margin-right:auto;font-size:10.5px;color:var(--t3);display:flex;align-items:center}

.lmodal-list{padding:10px 14px;max-height:360px;overflow-y:auto}
.lrow-v2{display:flex;align-items:center;gap:11px;padding:11px 12px;border-radius:13px;cursor:pointer;transition:.15s;margin-bottom:4px;border:1px solid transparent}
.lrow-v2:hover{background:var(--accent-d)}
.lrow-v2.checked{background:rgba(16,185,129,.1);border-color:rgba(16,185,129,.25)}
.lrow-v2-check{width:20px;height:20px;border-radius:7px;border:2px solid var(--card-b);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.15s;background:rgba(0,0,0,.14)}
.lrow-v2.checked .lrow-v2-check{background:var(--accent);border-color:var(--accent)}
.lrow-v2-check i{font-size:12px;color:#fff;opacity:0;transform:scale(.5);transition:.15s}
.lrow-v2.checked .lrow-v2-check i{opacity:1;transform:scale(1)}
.lrow-v2-avatar{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.lrow-v2.checked .lrow-v2-avatar{background:var(--accent);color:#fff}
.lrow-v2-info{flex:1;min-width:0}
.lrow-v2-name{font-size:12.5px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow-v2-meta{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}
.lrow-v2-status{font-size:9px;font-weight:800;padding:3px 9px;border-radius:20px;flex-shrink:0;white-space:nowrap}
.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}
.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}
.lrow-links{display:flex;gap:4px;margin-top:6px;flex-wrap:wrap}
.lrow-link-btn{background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.22);color:#34D399;border-radius:7px;padding:3px 7px;font-size:9.5px;font-family:ui-monospace,monospace;cursor:pointer;display:inline-flex;align-items:center;gap:4px;transition:.15s;max-width:100%}
.lrow-link-btn:hover{background:rgba(16,185,129,.18);transform:translateY(-1px)}
.lrow-link-btn span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:180px}
.lrow-v2-status.off{background:var(--red-bg);color:var(--red-t)}

.lmodal-footer{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 24px;border-top:1px solid var(--card-b)}
.lmodal-footer-info{font-size:10.5px;color:var(--t3);display:flex;align-items:center;gap:6px}
.lmodal-footer-info i{color:var(--accent)}
.lmodal-footer-btns{display:flex;gap:8px}

@media(max-width:500px){.sub-grid{grid-template-columns:1fr}.sub-card-stats{grid-template-columns:repeat(3,1fr)}}

.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(4px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:28px 26px;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:fi .2s ease}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none}
.modal-title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:18px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--accent)}
.lrow{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid rgba(16,185,129,.05)}
.lrow:last-child{border-bottom:none}
.lrow-check{width:16px;height:16px;border-radius:4px;cursor:pointer;accent-color:var(--accent)}
.lrow-label{flex:1;font-size:12px;color:var(--t1)}
.lrow-badge{font-size:9px;padding:2px 7px;border-radius:5px;background:var(--green-bg);color:var(--green-t);font-weight:700}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.3);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.3);background:var(--red-bg);color:var(--red-t)}
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600}

/* ══════ کانفیگ‌ها - طراحی ردیفی حرفه‌ای ══════ */
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:var(--card);border:1px solid var(--card-b);border-radius:14px;padding:0;transition:all .2s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:0 6px 24px rgba(0,0,0,.18)}
.cfg-card.is-off{opacity:.6}
.cfg-card.is-exp{opacity:.78}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px}
.cfg-status-dot{width:9px;height:9px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 3px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 3px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:13.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:7px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent2);background:var(--accent-d);padding:2px 7px;border-radius:5px;cursor:pointer;transition:.15s}
.cfg-uuid-mini:hover{background:rgba(16,185,129,.2)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.ubar{height:5px;border-radius:4px;background:rgba(16,185,129,0.1);overflow:hidden}
.ubar-f{height:100%;border-radius:4px;transition:width .4s ease}
.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-exp-col{flex-shrink:0;min-width:110px}
.cfg-badges-col{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0}
.proto-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;white-space:nowrap}
.pc-ws{background:var(--accent-d);color:var(--accent2)}
.pc-xhttp{background:var(--purple-bg);color:#34D399}
.pc-ultra{background:var(--green-bg);color:var(--green-t)}
.cfg-sub-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:var(--purple);font-size:11px}
.tog{width:19px;height:30px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;top:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on::after{top:14px}
.tog.on{background:var(--green)}

@media(max-width:880px){
  .cfg-row{flex-wrap:wrap}
  .cfg-divider-v{display:none}
  .cfg-usage-col{min-width:100%;order:5}
}

/* ── زیر ۷۶۸px: تبدیل کامل به کارت موبایل ── */
@media(max-width:768px){
  .cfg-grid{display:grid;grid-template-columns:1fr;gap:13px}
  .cfg-card{border-radius:16px}
  .cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}
  .cfg-row-top{display:flex;align-items:center;justify-content:space-between;gap:10px}
  .cfg-identity{min-width:0;flex:1}
  .cfg-usage-col{min-width:0}
  .cfg-exp-col{min-width:0}
  .cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}
  .cfg-actions{flex-wrap:wrap;border-top:1px solid var(--card-b);padding-top:10px;margin-top:2px;width:100%}
}

/* ══════ اتصالات فعال با IP ══════ */
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.conn-card{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:15px 17px;transition:.2s;position:relative;overflow:hidden}
.conn-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.conn-card::before{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}
.conn-ip-row{display:flex;align-items:center;gap:8px;margin-bottom:10px}
.conn-ip-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0}
.conn-ip{font-family:ui-monospace,monospace;font-size:13px;font-weight:700;color:var(--t1)}
.conn-label{font-size:10.5px;color:var(--t3);margin-top:1px}
.conn-meta{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--t3);padding-top:10px;border-top:1px solid var(--card-b)}

/* ══════ لاگ فعالیت‌ها ══════ */
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid rgba(16,185,129,.05);position:relative}
.log-item:last-child{border-bottom:none}
.log-ic{width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.log-ic.err{background:var(--red-bg);color:var(--red-t)}
.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}
.log-ic.info{background:var(--accent-d);color:var(--accent2)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--t1);line-height:1.6}
.log-time{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:5px}
.log-kind{font-size:8.5px;padding:1px 7px;border-radius:10px;background:var(--accent-d);color:var(--accent2);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.erow{padding:9px 0;border-bottom:1px solid rgba(16,185,129,.05)}
.erow:last-child{border-bottom:none}
.etime{color:var(--t3);font-size:9.5px;margin-bottom:3px;display:flex;align-items:center;gap:4px}
.emsg{color:var(--red-t);font-family:ui-monospace,monospace;background:var(--red-bg);padding:6px 9px;border-radius:6px;word-break:break-all;font-size:10.5px}

@media(max-width:1050px){
  .sidebar{transform:translateX(100%);visibility:hidden;pointer-events:none}
  .sidebar.open{transform:translateX(0);visibility:visible;pointer-events:auto;box-shadow:-10px 0 40px rgba(0,0,0,.4)}
  .sb-close{display:none}
  .sidebar.open .sb-close{display:flex}
  .main{margin-right:0;padding-top:70px}
  .mob-top{display:flex}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
}
@media(max-width:560px){
  .form-row{grid-template-columns:1fr 1fr !important}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{padding:62px 12px 50px}
  .sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}
}
/* FineVPN_v2ray — midnight glass / luminous gold visual system */



.v-metrics{grid-template-columns:repeat(4,1fr)!important}
.v-metric{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:22px 14px!important;gap:8px}
.m-ring{width:52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:22px;color:#10B981;background:rgba(16,185,129,.12);border:1.5px solid rgba(16,185,129,.35);box-shadow:0 0 18px rgba(16,185,129,.15)}
.m-ring.r2{color:#34D399;background:rgba(52,211,153,.1);border-color:rgba(52,211,153,.3)}
.m-ring.r3{color:#0D9488;background:rgba(13,148,136,.12);border-color:rgba(13,148,136,.32)}
.m-ring.r4{color:#6EE7B7;background:rgba(110,231,183,.1);border-color:rgba(110,231,183,.3)}
.v-metric .m-label{font-size:11.5px!important}
.v-metric .m-val{font-size:26px!important;line-height:1.1}
.v-metric .m-sub{font-size:10.5px!important;display:flex;align-items:center;gap:5px}
@media(max-width:900px){.v-metrics{grid-template-columns:repeat(2,1fr)!important}}
@media(max-width:480px){.v-metrics{grid-template-columns:repeat(2,1fr)!important;gap:10px!important}.v-metric{padding:16px 10px!important}.m-ring{width:42px;height:42px;font-size:18px}.m-val{font-size:22px!important}}

.sr-tile{background:rgba(16,185,129,.05);border:1px solid var(--card-b);border-radius:14px;padding:14px;display:flex;flex-direction:column;gap:6px;transition:all .2s}
.sr-tile:hover{background:rgba(16,185,129,.1);border-color:var(--card-bh);transform:translateY(-2px)}
.sr-tile-ico{width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:17px}
.sr-tile-name{font-size:11.5px;font-weight:700;color:var(--t2)}
.sr-tile-val{font-size:11px;color:var(--green-t);display:flex;align-items:center;gap:6px}

/* ══════ کارت ساب قابل کلیک ══════ */
.sub-exp-card{cursor:pointer;transition:all .25s cubic-bezier(.4,0,.2,1)}
.sub-exp-card:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 14px 34px rgba(0,0,0,.3)}
.sub-exp-card.open{border-color:rgba(16,185,129,.45);box-shadow:0 0 0 3px rgba(16,185,129,.1)}
.sub-exp-body{display:none;padding:14px 0 0;border-top:1px dashed var(--card-b);margin-top:14px}
.sub-exp-card.open .sub-exp-body{display:block;animation:fi .2s ease}
.sub-exp-hint{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;margin-top:10px;justify-content:center}
.sub-exp-card.open .sub-exp-hint{display:none}
.sub-ip-row{display:flex;align-items:center;gap:9px;padding:8px 10px;border-radius:10px;background:rgba(16,185,129,.05);border:1px solid var(--card-b);margin-bottom:7px;direction:ltr}
.sub-ip-row .dot{flex-shrink:0}
.sub-ip-addr{font-family:ui-monospace,monospace;font-size:12px;font-weight:700;color:var(--t1)}
.sub-ip-meta{font-size:10px;color:var(--t3);margin-right:auto;white-space:nowrap}
.sub-log-list{max-height:220px;overflow-y:auto}
.sub-log-item{display:flex;gap:9px;padding:7px 2px;border-bottom:1px solid rgba(16,185,129,.05);font-size:11px}
.sub-log-item:last-child{border-bottom:none}
.sub-log-ic{width:24px;height:24px;border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:11px;flex-shrink:0}
.sub-log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.sub-log-ic.err{background:var(--red-bg);color:var(--red-t)}
.sub-log-ic.info{background:var(--accent-d);color:var(--accent2)}
.sub-log-msg{color:var(--t2);line-height:1.5;flex:1;min-width:0}
.sub-log-time{font-size:9px;color:var(--t3);white-space:nowrap}
.sub-sec-label{font-size:10px;font-weight:800;color:var(--t3);text-transform:uppercase;letter-spacing:.06em;margin:14px 0 8px;display:flex;align-items:center;gap:6px}

/* ══════ استایل یکپارچه بخش‌ها (v3) ══════ */
.pg .card{border-radius:18px}
.sec-hero{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:13px;margin-bottom:18px}
.sec-hero-tile{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:18px;padding:18px 20px;position:relative;overflow:hidden;transition:all .2s}
.sec-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.sec-hero-tile::before{content:'';position:absolute;top:-40px;left:-40px;width:130px;height:130px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.sec-hero-ico{width:38px;height:38px;border-radius:11px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:17px;margin-bottom:11px;position:relative;z-index:1}
.sec-hero-ico.red{background:var(--red-bg);color:var(--red-t)}
.sec-hero-ico.pur{background:var(--purple-bg);color:#34D399}
.sec-hero-ico.amb{background:var(--amber-bg);color:var(--amber-t)}
.sec-hero-label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;position:relative;z-index:1}
.sec-hero-val{font-size:23px;font-weight:800;color:var(--t1);line-height:1.15;margin-top:4px;position:relative;z-index:1}
.sec-hero-sub{font-size:10px;color:var(--t3);margin-top:3px;position:relative;z-index:1}
.sec-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 55%);border:1px solid var(--card-b);border-radius:20px;padding:0;overflow:hidden;box-shadow:var(--shadow);margin-bottom:16px;position:relative}
.sec-panel-head{display:flex;align-items:center;gap:12px;padding:18px 22px;border-bottom:1px solid var(--card-b);position:relative;z-index:1}
.sec-panel-ico{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0;box-shadow:0 6px 16px rgba(16,185,129,.35)}
.sec-panel-ico.red{background:linear-gradient(135deg,#EF4444,#B91C1C);box-shadow:0 6px 16px rgba(239,68,68,.35)}
.sec-panel-ico.pur{background:linear-gradient(135deg,#10B981,#065F46);box-shadow:0 6px 16px rgba(16,185,129,.35)}
.sec-panel-title{font-size:14.5px;font-weight:800;color:var(--t1)}
.sec-panel-sub{font-size:10.5px;color:var(--t3);margin-top:2px;line-height:1.6}
.sec-panel-body{padding:18px 22px 20px;position:relative;z-index:1}
.sec-log-box{background:rgba(0,0,0,.22);border:1px solid var(--card-b);border-radius:12px;padding:14px;height:260px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9}
.sec-log-box p{color:var(--t3)}
.sec-log-box .ok{color:var(--green-t)}
.sec-log-box .err{color:var(--red-t)}
.sec-log-box .info{color:var(--accent2)}
.sec-log-box .warn{color:var(--amber-t)}
@media(max-width:600px){.sec-panel-head{padding:15px 16px}.sec-panel-body{padding:14px 16px 16px}}



.card-title{display:flex;align-items:center;gap:9px}
.qr-modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.72);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(4px);padding:20px}
.qr-modal.open{display:flex}
.qr-box{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:26px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow)}
.qr-title{font-size:13.5px;font-weight:800;margin-bottom:16px;color:var(--t1)}
.btn-p{background:linear-gradient(135deg,#10b981,#059669);color:#fff;box-shadow:0 4px 16px rgba(16,185,129,.3)}
.btn-p:hover{background:linear-gradient(135deg,#34d399,#10b981);box-shadow:0 6px 20px rgba(16,185,129,.4)}

/* FineVPN_v2ray — glassmorphism, deep-star sky, luminous gold */
:root, [data-theme="light"]{
  --bg:#030713;--bg2:rgba(5,11,28,.88);--bg3:rgba(17,27,52,.72);
  --card:rgba(13,22,45,.68);--card-b:rgba(231,190,82,.20);--card-bh:rgba(255,218,115,.48);
  --accent:#f0c45b;--accent2:#ffe5a0;--accent-d:rgba(240,196,91,.13);
  --green:#55d7ad;--green-bg:rgba(85,215,173,.12);--green-t:#88f0ce;
  --red:#fb7185;--red-bg:rgba(251,113,133,.12);--red-t:#fda4af;
  --amber:#f5c451;--amber-bg:rgba(245,196,81,.12);--amber-t:#ffe29a;
  --purple:#d9b968;--purple-bg:rgba(217,185,104,.13);
  --t1:#f5f4ff;--t2:#c7cbe0;--t3:#8290b6;--shadow:0 16px 44px rgba(0,0,0,.38);
}
html,body{background-color:#030713}
body{
  background-color:#030713;
  background-image:
    radial-gradient(1px 1px at 17px 23px,rgba(255,255,255,.86) 55%,transparent 100%),
    radial-gradient(1.4px 1.4px at 71px 101px,rgba(255,225,164,.72) 55%,transparent 100%),
    linear-gradient(rgba(2,6,18,.79),rgba(2,6,18,.84)),
    url("https://i.ibb.co/39zWtJzS/1791731497906.jpg");
  background-size:109px 109px,173px 173px,100% 100%,min(66vw,680px) auto;
  background-position:0 0,35px 61px,center,center;
  background-repeat:repeat,repeat,no-repeat,no-repeat;background-attachment:fixed;
}
.sidebar{background:rgba(4,10,27,.84);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border-color:rgba(240,196,91,.2)}
.mob-top{background:rgba(4,10,27,.86);backdrop-filter:blur(22px);-webkit-backdrop-filter:blur(22px);border-color:rgba(240,196,91,.2)}
.logo{border-color:rgba(240,196,91,.18)}
.logo-img{width:44px;height:44px;border-radius:13px;border-color:rgba(255,220,125,.5);box-shadow:0 0 22px rgba(240,196,91,.22)}
.logo-img img,.mob-logo img{object-fit:cover}
.mob-logo{width:32px;height:32px;border-radius:10px;border:1px solid rgba(255,220,125,.48);box-shadow:0 0 16px rgba(240,196,91,.22)}
.card,.metric,.vless-box,.traf-main-stat,.traf-mini,.traf-chart-card,.cfg-card,.conn-card,.sec-panel,.sec-hero-tile,.modal,.qr-box,.sr-tile,.sub-exp-card{
  background:linear-gradient(145deg,rgba(18,29,57,.73),rgba(6,12,29,.69))!important;
  border-color:rgba(240,196,91,.18)!important;box-shadow:0 16px 42px rgba(0,0,0,.24);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px)
}
.card:hover,.metric:hover,.cfg-card:hover,.sec-hero-tile:hover{border-color:rgba(255,221,132,.42)!important;box-shadow:0 18px 48px rgba(0,0,0,.31),0 0 26px rgba(240,196,91,.06)}
.btn-p,.btn-pur,.menu-btn{background:linear-gradient(135deg,#fff0b8 0%,#f1ca62 42%,#bd8a25 100%)!important;color:#211805!important;border:1px solid rgba(255,233,164,.56)!important;box-shadow:0 0 18px rgba(240,196,91,.19),0 7px 22px rgba(0,0,0,.24)!important}
.btn-p:hover,.btn-pur:hover,.menu-btn:hover{background:linear-gradient(135deg,#fff6d6 0%,#ffe18a 45%,#d7a63a 100%)!important;box-shadow:0 0 26px rgba(240,196,91,.33)!important;transform:translateY(-1px)}
.btn-p i,.btn-pur i{color:#211805!important}
.btn-g,.btn-o,.theme-btn{background:rgba(240,196,91,.08)!important;color:#ffe5a0!important;border-color:rgba(240,196,91,.24)!important;backdrop-filter:blur(12px)}
.btn-g:hover,.btn-o:hover,.theme-btn:hover{background:rgba(240,196,91,.17)!important;border-color:rgba(255,221,132,.48)!important}
.fi,.fs,.modal-v2-input,textarea,input[type="text"],input[type="number"],input[type="password"]{background:rgba(4,9,24,.55)!important;border-color:rgba(240,196,91,.18)!important;color:#f5f4ff!important}
.fi:focus,.fs:focus,.modal-v2-input:focus,textarea:focus{border-color:#f0c45b!important;box-shadow:0 0 0 3px rgba(240,196,91,.12)!important}
.nav-it:hover,.nav-it.on{background:rgba(240,196,91,.1);color:#fff0bd;border-right-color:#f0c45b}
.nav-badge{background:rgba(240,196,91,.15);color:#ffe5a0}
.m-ring,.sec-panel-ico,.sec-hero-ico{color:#ffe5a0!important;border-color:rgba(240,196,91,.26)!important;box-shadow:0 0 22px rgba(240,196,91,.1)}
.m-ring.r2,.m-ring.r3,.m-ring.r4{color:#ffe5a0;background:rgba(240,196,91,.09);border-color:rgba(240,196,91,.21)}
.brand-contact{margin-top:22px;padding:18px 20px;border:1px solid rgba(240,196,91,.24);border-radius:22px;background:linear-gradient(135deg,rgba(22,31,56,.82),rgba(6,12,28,.74));box-shadow:0 18px 45px rgba(0,0,0,.28);backdrop-filter:blur(22px);display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap}
.brand-contact-identity{display:flex;align-items:center;gap:13px;min-width:0}
.brand-contact-logo{width:60px;height:60px;object-fit:cover;border-radius:16px;border:1px solid rgba(255,220,125,.44);box-shadow:0 0 22px rgba(240,196,91,.15)}
.brand-contact-title{font-size:15px;font-weight:900;color:#fff0bd;letter-spacing:.02em}
.brand-contact-provider{font-size:11px;color:#d0d5e9;margin-top:4px}
.brand-contact-signature{font-size:12px;color:#f4d98c;margin-top:3px;letter-spacing:.04em}
.brand-contact-links{display:flex;gap:9px;flex-wrap:wrap}
.fine-tg-link{display:inline-flex;align-items:center;gap:8px;padding:10px 13px;border-radius:13px;border:1px solid rgba(240,196,91,.24);background:rgba(240,196,91,.07);color:#ffe5a0;font-size:11.5px;font-weight:700;transition:all .2s}
.fine-tg-link i{font-size:18px;color:#f6cf67}
.fine-tg-link:hover{transform:translateY(-2px);background:rgba(240,196,91,.15);box-shadow:0 0 20px rgba(240,196,91,.12)}
@media(max-width:600px){.brand-contact{padding:15px;gap:14px}.brand-contact-logo{width:50px;height:50px;border-radius:13px}.brand-contact-links{width:100%}.fine-tg-link{flex:1;justify-content:center;min-width:130px}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;scroll-behavior:auto!important;transition-duration:.01ms!important}}

html[data-accent="blue"]{--accent:#60a5fa;--accent-hover:#3b82f6;--border:rgba(96,165,250,.22);--border-b:rgba(96,165,250,.4)}
html[data-accent="purple"]{--accent:#a78bfa;--accent-hover:#8b5cf6;--border:rgba(167,139,250,.22);--border-b:rgba(167,139,250,.4)}
html[data-accent="emerald"]{--accent:#34d399;--accent-hover:#10b981;--border:rgba(52,211,153,.22);--border-b:rgba(52,211,153,.4)}
html[data-accent="gold"]{--accent:#f0c45b;--accent-hover:#d4a333;--border:rgba(240,196,91,.22);--border-b:rgba(240,196,91,.4)}

html[data-accent="blue"] .btn-p,html[data-accent="blue"] .btn-g{background:linear-gradient(135deg,#dbeafe,#60a5fa)!important;color:#10213b!important;border-color:rgba(96,165,250,.65)!important}
html[data-accent="purple"] .btn-p,html[data-accent="purple"] .btn-g{background:linear-gradient(135deg,#ede9fe,#a78bfa)!important;color:#251446!important;border-color:rgba(167,139,250,.65)!important}
html[data-accent="emerald"] .btn-p,html[data-accent="emerald"] .btn-g{background:linear-gradient(135deg,#d1fae5,#34d399)!important;color:#052e26!important;border-color:rgba(52,211,153,.65)!important}
html[data-accent="gold"] .btn-p,html[data-accent="gold"] .btn-g{background:linear-gradient(135deg,#fff0b8,#f0c45b)!important;color:#211805!important;border-color:rgba(240,196,91,.65)!important}

.logo-img,.mob-logo img,.brand-contact-logo{border-radius:50%!important}
</style>
</head>
<body>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="modal-bg" id="modal-links">
  <div class="modal-v2" style="max-width:500px">
    <div class="lmodal-head">
      <button class="modal-v2-close" onclick="closeModal('modal-links')"><i class="ti ti-x"></i></button>
      <div class="lmodal-icon-row">
        <div class="lmodal-icon"><i class="ti ti-link-plus"></i></div>
        <div>
          <div class="lmodal-title-v2">مدیریت کانفیگ‌های <span id="modal-sub-name" style="color:var(--accent2)">—</span></div>
          <div class="lmodal-sub-v2">کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید</div>
        </div>
      </div>
      <div class="lmodal-search">
        <i class="ti ti-search"></i>
        <input type="text" id="lmodal-search-inp" placeholder="جستجوی کانفیگ..." oninput="filterLmodal(this.value)">
      </div>
      <div class="lmodal-quickbar">
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> انتخاب همه</button>
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> لغو همه</button>
        <span class="lmodal-count" id="lmodal-count">۰ انتخاب شده</span>
      </div>
    </div>
    <div class="lmodal-list" id="modal-links-body">در حال بارگذاری...</div>
    <div class="lmodal-footer">
      <div class="lmodal-footer-info"><i class="ti ti-info-circle"></i> تغییرات بلافاصله اعمال می‌شود</div>
      <div class="lmodal-footer-btns">
        <button class="btn btn-o" onclick="closeModal('modal-links')">بستن</button>
        <button class="btn btn-p" id="modal-save-btn" onclick="saveSubLinks()"><i class="ti ti-check"></i> ذخیره</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-create-sub">
  <div class="modal-v2" style="max-width:520px">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-sub')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-folder-plus"></i></div>
      <div class="modal-v2-title">ساخت گروه ساب</div>
      <div class="modal-v2-sub">یک صفحه پابلیک مجزا با ۲۴ کانفیگ خودکار بسازید</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> نام گروه</label>
        <input class="modal-v2-input" id="ns-name" placeholder="مثلاً: کانال اختصاصی">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-align-left"></i> توضیحات (اختیاری)</label>
        <input class="modal-v2-input" id="ns-desc" placeholder="توضیح کوتاه درباره این گروه">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-lock"></i> رمز صفحه پابلیک (اختیاری)</label>
        <input class="modal-v2-input" id="ns-pw" type="password" placeholder="خالی بگذارید = بدون رمز">
      </div>
      
      <div class="cl" style="margin-top:16px;padding:12px;background:rgba(16,185,129,.1);border-radius:10px;border:1px solid rgba(16,185,129,.3)">
        <strong style="color:var(--purple-t)"><i class="ti ti-magic-wand"></i> ساخت سریع ۲۴ کانفیگ</strong>
        <p style="font-size:10.5px;color:var(--t3);margin:4px 0 8px 0">۳ پروتکل × ۲ فینگرپرینت × ۴ ALPN = ۲۴ کانفیگ (VWS/XPU/XHS)</p>
      </div>
      
      <div class="modal-v2-field">
        <label><i class="ti ti-database"></i> حجم مشترک کل (GB)</label>
        <input class="modal-v2-input" id="ns-vol" type="number" min="0" step="0.5" value="1" placeholder="مثلا 1 (خالی = نامحدود)">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-calendar"></i> روزهای اعتبار</label>
        <input class="modal-v2-input" id="ns-days" type="number" min="0" step="1" value="30" placeholder="مثلا 30 (۰ = بدون انقضا)">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-users"></i> حداکثر کاربر هم‌زمان (IP Limit)</label>
        <input class="modal-v2-input" id="ns-iplimit" type="number" min="0" step="1" value="2" placeholder="مثلا 2 (۰ = نامحدود)">
      </div>
      
      <div class="cl" style="margin-top:14px"><i class="ti ti-info-circle"></i><span>حجم مشترک بین تمام ۲۴ کانفیگ تقسیم می‌شود. هر کاربر از هر کانفیگی مصرف کند، از همین حجم کم می‌شود.</span></div>
      <div id="qs-preview" style="margin-top:10px;font-size:11px;color:var(--t3);padding:8px 10px;background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.25);border-radius:8px"></div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="closeModal('modal-create-sub')" style="flex:.6">انصراف</button>
        <button class="btn btn-pur" onclick="createSubQuick()"><i class="ti ti-magic-wand"></i> ساخت گروه + ۲۴ کانفیگ</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> ویرایش کانفیگ</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label>عنوان</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>سهمیه (0 = نامحدود)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label>انقضا (روز از الان، 0 = بدون تغییر/نامحدود)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label>یادداشت</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>Fingerprint (uTLS)</label>
        <select class="fs" id="el-fp" style="width:100%">
          <option value="chrome">chrome</option>
          <option value="firefox">firefox</option>
          <option value="safari">safari</option>
          <option value="ios">ios</option>
          <option value="android">android</option>
          <option value="edge">edge</option>
          <option value="360">360</option>
          <option value="qq">qq</option>
          <option value="random">random</option>
          <option value="randomized">randomized</option>
        </select>
      </div>
      <div class="fg" style="flex:1"><label>ALPN (خالی = پیش‌فرض)</label><input class="fi" id="el-alpn" placeholder="مثلاً: h2,http/1.1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>پورت اتصال</label><input class="fi" id="el-port" type="number" min="1" max="65535" style="width:100%"></div>
      <div class="fg" style="flex:1"><label>محدودیت آی‌پی (0 = نامحدود)</label><input class="fi" id="el-iplimit" type="number" min="0" step="1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>محدودیت سرعت (0 = نامحدود)</label><input class="fi" id="el-speed" type="number" min="0" step="0.5" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-speed-unit"><option value="MBIT">Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div>
    </div>
    <div class="cl"><i class="ti ti-info-circle"></i><span>برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">انصراف</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> ذخیره تغییرات</button>
    </div>
  </div>
</div>
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo"><img src="https://i.ibb.co/39zWtJzS/1791731497906.jpg" alt="FineVPN_v2ray"></div>
    <span class="mob-title">FineVPN_v2ray</span>
  </div>
  <div class="mob-right">
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="logo-img"><img src="https://i.ibb.co/39zWtJzS/1791731497906.jpg" alt="FineVPN_v2ray"></div>
    <div><div class="logo-name">FineVPN_v2ray</div><div class="logo-sub">Secure Tunnel Manager</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">پنل</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="appearance"><i class="ti ti-palette"></i> ظاهر پنل</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> گروه‌های ساب <span class="nav-badge" id="subs-nb">0</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> سابسکریپشن</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-sec">سیستم</div>
    <div class="nav-it" data-pg="categories"><i class="ti ti-category"></i> دسته‌بندی‌ها</div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> خطاها</div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i> تست WebSocket</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
  </div>
  <div class="sb-foot">
    <button class="logout-btn" type="button" onclick="toggleLanguage()" id="language-toggle"><i class="ti ti-language"></i> English</button>
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> خروج</button>
  </div>
</aside>
<main class="main">
<section class="pg on" id="pg-overview">

  <!-- Quick Sub Creator Wizard -->
  <div class="card" style="border:1px solid var(--border-red, rgba(16,185,129,.35));background:linear-gradient(145deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));position:relative;overflow:hidden;margin-bottom:20px">
    <div style="position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,#10b981,#34d399,transparent)"></div>
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">
      <div style="width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,#10b981,#047857);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;box-shadow:0 6px 16px rgba(16,185,129,0.35)"><i class="ti ti-wand"></i></div>
      <div>
        <div style="font-size:15px;font-weight:800;color:var(--t1,#fff)">ساخت سریع گروه ساب (۲۴ کانفیگ)</div>
        <div style="font-size:11.5px;color:var(--muted,#94a3b8)">ساخت خودکار گروه ساب، تنظیم حجم مشترک و تولید ۲۴ کانفیگ با یک کلیک</div>
      </div>
    </div>
    <div class="form-row" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(130px, 1fr));gap:12px;margin-bottom:16px;flex-wrap:wrap">
      <div class="fg" style="margin-bottom:0">
        <label style="font-size:11px;font-weight:700;color:var(--muted,#94a3b8);margin-bottom:5px;display:block">نام گروه ساب</label>
        <input type="text" class="fi" id="qs-name" placeholder="مثلاً: سرویس VIP" style="width:100%">
      </div>
      <div class="fg" style="margin-bottom:0">
        <label style="font-size:11px;font-weight:700;color:var(--muted,#94a3b8);margin-bottom:5px;display:block">حجم مشترک (GB) — <span style="opacity:.8">۰ = نامحدود</span></label>
        <input type="number" class="fi" id="qs-vol" placeholder="20" min="0" step="0.5" value="20" style="width:100%">
      </div>
      <div class="fg" style="margin-bottom:0">
        <label style="font-size:11px;font-weight:700;color:var(--muted,#94a3b8);margin-bottom:5px;display:block">مدت اعتبار (روز) — <span style="opacity:.8">۰ = نامحدود</span></label>
        <input type="number" class="fi" id="qs-days" placeholder="30" min="0" step="1" value="30" style="width:100%">
      </div>
      <div class="fg" style="margin-bottom:0">
        <label style="font-size:11px;font-weight:700;color:var(--muted,#94a3b8);margin-bottom:5px;display:block">سقف کاربر (IP) — <span style="opacity:.8">۰ = نامحدود</span></label>
        <input type="number" class="fi" id="qs-ip" placeholder="2" min="0" step="1" value="2" style="width:100%">
      </div>
    </div>
    <div id="qs-summary" style="font-size:11.5px;color:var(--muted,#94a3b8);background:rgba(16,185,129,.07);border:1px solid rgba(16,185,129,.18);border-radius:12px;padding:10px 13px;margin-bottom:13px;display:flex;align-items:center;gap:8px;flex-wrap:wrap"></div>
    <script>
    function qsPreviewUpdate(){
      const el=document.getElementById('qs-summary'); if(!el) return;
      const vol=parseFloat(document.getElementById('qs-vol').value)||0;
      const days=parseInt(document.getElementById('qs-days').value)||0;
      const ip=parseInt(document.getElementById('qs-ip').value)||0;
      const parts=[];
      parts.push(vol>0?('💾 حجم مشترک: <b style="color:var(--t1,#fff)">'+vol+' GB</b> بین ۲۴ کانفیگ ≈ '+(vol/24).toFixed(2)+' GB هر کانفیگ'):'💾 حجم: <b style="color:var(--t1,#fff)">نامحدود</b>');
      parts.push(days>0?('⏱ اعتبار: <b style="color:var(--t1,#fff)">'+days+' روز</b>'):'⏱ اعتبار: <b style="color:var(--t1,#fff)">نامحدود</b>');
      parts.push(ip>0?('📱 حداکثر <b style="color:var(--t1,#fff)">'+ip+' کاربر</b> هم‌زمان'):'📱 کاربر: <b style="color:var(--t1,#fff)">نامحدود</b>');
      el.innerHTML=parts.join(' <span style="opacity:.4">•</span> ');
    }
    ['qs-vol','qs-days','qs-ip'].forEach(id=>{
      const e=document.getElementById(id); if(e){ e.addEventListener('input',qsPreviewUpdate); }
    });
    qsPreviewUpdate();
    </script>
    <button class="btn btn-p" onclick="quickSubCreate()" id="qs-submit-btn" style="width:100%;padding:12px;font-size:13.5px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px;white-space:normal;text-align:center;line-height:1.6;flex-wrap:wrap">
      <i class="ti ti-plus"></i> ساخت گروه ساب + ۲۴ کانفیگ با حجم مشترک
    </button>
    <div id="qs-result" style="display:none;margin-top:16px;padding:14px;border-radius:12px;background:rgba(31,184,126,0.1);border:1px solid rgba(31,184,126,0.25)">
      <div style="font-size:12px;font-weight:700;color:#3fd79c;margin-bottom:6px"><i class="ti ti-check"></i> گروه ساب و ۲۴ کانفیگ با موفقیت ساخته شد!</div>
      <div style="display:flex;gap:8px;align-items:center">
        <input type="text" id="qs-pub-link" readonly class="fi" style="font-size:11px;direction:ltr;background:rgba(0,0,0,0.3);flex:1">
        <button class="btn btn-sm btn-p" onclick="navigator.clipboard.writeText(document.getElementById('qs-pub-link').value);toast('لینک کپی شد','ok')"><i class="ti ti-copy"></i> کپی</button>
      </div>
    </div>
  </div>

  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="tb-sub" id="last-upd">در حال بارگذاری...</div></div>
    <div class="tb-right">
      <span class="badge bg-green"><span class="dot dg pulse"></span> فعال</span>
      <span class="badge" id="vol-badge" title="وضعیت ذخیره‌سازی">…</span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button>
    </div>
  </div>
  <div class="metrics v-metrics">
    <div class="metric v-metric"><div class="m-ring"><i class="ti ti-plug-connected"></i></div><div class="m-label">اتصالات فعال</div><div class="m-val" id="m-conns">—</div><div class="m-sub"><span class="dot dg pulse"></span> زنده</div></div>
    <div class="metric v-metric"><div class="m-ring r2"><i class="ti ti-transfer"></i></div><div class="m-label">کل ترافیک</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div><div class="m-sub">از راه‌اندازی</div></div>
    <div class="metric v-metric"><div class="m-ring r3"><i class="ti ti-link"></i></div><div class="m-label">کانفیگ فعال</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">از کل</div></div>
    <div class="metric v-metric"><div class="m-ring r4"><i class="ti ti-folders"></i></div><div class="m-label">گروه‌های ساب</div><div class="m-val" id="m-subs">—</div><div class="m-sub">فعال</div></div>
  </div>
  <div class="vless-box">
    <div class="vl-header">
      <div class="vl-title"><i class="ti ti-link"></i> لینک پیش‌فرض (بدون محدودیت)</div>
      <span class="badge bg-blue"><span class="dot db"></span> TLS 443 · WS</span>
    </div>
    <div class="vl-code" id="vless-main">در حال دریافت...</div>
    <div class="vl-actions">
      <button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> کپی</button>
      <button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
      <button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-link-plus"></i> کانفیگ محدود</button>
      <button class="btn btn-pur" onclick="navTo('subgroups')"><i class="ti ti-folders"></i> گروه‌های ساب</button>
    </div>
  </div>
  <div class="g3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> ترافیک ساعتی (MB)</div><div class="ch"><canvas id="ch1"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-chart-bar"></i> توزیع پروتکل‌ها</div><div class="ch-sm" style="min-height:190px"><canvas id="ch2"></canvas></div></div>
  </div>
  <div class="g2" style="grid-template-columns:1fr">
    <div class="card">
      <div class="card-title"><i class="ti ti-heartbeat"></i> وضعیت سرویس</div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px" id="sr-grid">
        <div class="sr-tile">
          <div class="sr-tile-ico" style="color:#34D399;background:rgba(52,211,153,.12)"><i class="ti ti-shield-check"></i></div>
          <div class="sr-tile-name">UUID Auth</div>
          <div class="sr-tile-val"><span class="dot dg pulse"></span> فعال · سخت‌گیرانه</div>
        </div>
        <div class="sr-tile">
          <div class="sr-tile-ico" style="color:#10B981;background:rgba(16,185,129,.12)"><i class="ti ti-circle-check"></i></div>
          <div class="sr-tile-name">VLESS / WS Tunnel</div>
          <div class="sr-tile-val"><span class="dot dg pulse"></span> فعال</div>
        </div>
        <div class="sr-tile">
          <div class="sr-tile-ico" style="color:#6EE7B7;background:rgba(110,231,183,.12)"><i class="ti ti-bolt"></i></div>
          <div class="sr-tile-name">Siz10a XHTTP Ultra</div>
          <div class="sr-tile-val"><span class="dot dg pulse"></span> فعال · 3 mode</div>
        </div>
        <div class="sr-tile">
          <div class="sr-tile-ico" style="color:#0D9488;background:rgba(13,148,136,.14)"><i class="ti ti-folders"></i></div>
          <div class="sr-tile-name">Sub Groups</div>
          <div class="sr-tile-val"><span class="dot dg pulse"></span> فعال v9</div>
        </div>
        <div class="sr-tile">
          <div class="sr-tile-ico" style="color:#34D399;background:rgba(52,211,153,.12)"><i class="ti ti-rss"></i></div>
          <div class="sr-tile-name">Subscription API</div>
          <div class="sr-tile-val"><span class="dot dg pulse"></span> فعال</div>
        </div>
        <div class="sr-tile">
          <div class="sr-tile-ico" style="color:#6EE7B7;background:rgba(110,231,183,.12)"><i class="ti ti-clock"></i></div>
          <div class="sr-tile-name">آپتایم</div>
          <div class="sr-tile-val" id="uptime-inline" style="direction:ltr">—</div>
        </div>
      </div>
      <div style="margin-top:16px;padding-top:14px;border-top:1px solid var(--card-b)">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <span style="font-size:12px;font-weight:700;color:var(--t2)"><i class="ti ti-gauge"></i> بار نسبی</span>
          <span class="sr-v" id="bw-pct">—%</span>
        </div>
        <div class="spbar" style="width:100%;height:8px"><div class="spfill" id="bw-bar" style="width:0%"></div></div>
      </div>
    </div>
  </div>
  <div class="brand-contact">
    <div class="brand-contact-identity">
      <img class="brand-contact-logo" src="https://i.ibb.co/39zWtJzS/1791731497906.jpg" alt="FineVPN_v2ray logo">
      <div><div class="brand-contact-title">FineVPN_v2ray</div><div class="brand-contact-provider">ارائه‌دهنده: مـحـمـدصـادق افـغـان</div><div class="brand-contact-signature">𝑀𝑢ℎ𝑎𝑚𝑚𝑎𝑑𝒔𝒂𝒅𝒊𝒒</div></div>
    </div>
    <div class="brand-contact-links">
      <a class="fine-tg-link" href="https://t.me/sadiq_AFG1" target="_blank" rel="noopener noreferrer"><i class="ti ti-brand-telegram"></i><span>پشتیبانی <b>@sadiq_AFG1</b></span></a>
    </div>
  </div>
</section>
<section class="pg" id="pg-appearance">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-palette"></i> ظاهر پنل</div><div class="tb-sub">تنظیم رنگ‌ها مستقل از صفحهٔ اشتراک؛ تنظیمات در همین مرورگر ذخیره می‌شود.</div></div></div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico pur"><i class="ti ti-palette"></i></div><div><div class="sec-panel-title">تم‌های آماده</div><div class="sec-panel-sub">آبی، بنفش، سبز زمردی یا طلایی را انتخاب کنید.</div></div></div>
    <div class="sec-panel-body" style="display:flex;gap:12px;align-items:center;flex-wrap:wrap">
      <label for="accent-theme-select" style="font-size:12px;font-weight:700">پالت رنگ</label>
      <select class="fi" id="accent-theme-select" onchange="applyAccentTheme(this.value)" style="max-width:220px"><option value="blue">آبی</option><option value="purple">بنفش</option><option value="emerald">سبز زمردی</option><option value="gold">طلایی</option></select>
      <button class="btn btn-g btn-sm" type="button" onclick="toggleLanguage()"><i class="ti ti-language"></i> تغییر زبان فارسی / English</button>
    </div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico"><i class="ti ti-color-swatch"></i></div><div><div class="sec-panel-title">رنگ‌های سفارشی</div><div class="sec-panel-sub">رنگ دکمه‌ها، متن اصلی و حاشیه‌ها را تنظیم کنید.</div></div></div>
    <div class="sec-panel-body">
      <div class="form-row" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px">
        <label class="fg">رنگ دکمه‌ها <input class="fi" id="theme-button-color" type="color" value="#60a5fa" style="display:block;width:100%;height:44px;padding:4px;margin-top:7px"></label>
        <label class="fg">رنگ متن اصلی <input class="fi" id="theme-text-color" type="color" value="#f5f4ff" style="display:block;width:100%;height:44px;padding:4px;margin-top:7px"></label>
        <label class="fg">رنگ حاشیه‌ها <input class="fi" id="theme-border-color" type="color" value="#60a5fa" style="display:block;width:100%;height:44px;padding:4px;margin-top:7px"></label>
      </div>
      <div style="display:flex;gap:9px;flex-wrap:wrap;margin-top:8px">
        <button class="btn btn-p" type="button" onclick="saveCustomAppearance()"><i class="ti ti-device-floppy"></i> ذخیرهٔ رنگ‌ها</button>
        <button class="btn btn-g" type="button" onclick="resetCustomAppearance()"><i class="ti ti-refresh"></i> بازنشانی</button>
      </div>
      <p style="font-size:11px;color:var(--t3);line-height:1.8;margin-top:12px">این تنظیمات فقط روی مرورگر شما اعمال می‌شوند و ظاهر پنل اشتراک را تغییر نمی‌دهند.</p>
    </div>
  </div>
</section>
<section class="pg" id="pg-links">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی</div></div>
    <div class="tb-right">
      <select class="cp-input-full fs cat-filter" id="cat-filter" onchange="loadLinks()"><option value="">همه دسته‌ها</option></select>
      <span class="badge bg-blue" id="links-pg-cnt">۰ کانفیگ</span></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title">ساخت کانفیگ جدید</div>
        <div class="cp-head-sub">UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> شناسه کانفیگ</div>
          <input class="cp-input-full" id="nl-label" placeholder="مثلاً: کاربر علی">
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-note" placeholder="یادداشت (اختیاری)">
          </div>
          <div class="cp-mini-row">
            <select class="cp-input-full fs" id="nl-cat"><option value="">— بدون دسته —</option></select>
          </div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-folders"></i> گروه ساب و انقضا</div>
          <select class="cp-input-full fs" id="nl-sub"><option value="">— بدون گروه —</option></select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="انقضا (روز) · 0 = نامحدود">
          </div>
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)">نامحدود</span>
            <span class="chip" onclick="setExpiry(7,this)">۷ روز</span>
            <span class="chip active" onclick="setExpiry(30,this)">۳۰ روز</span>
            <span class="chip" onclick="setExpiry(90,this)">۹۰ روز</span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> سهمیه ترافیک</div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود">
          <select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
        </div>
        <div class="chip-row" id="quota-chips">
          <span class="chip" onclick="setQuota(0,'GB',this)">نامحدود</span>
          <span class="chip" onclick="setQuota(500,'MB',this)">۵۰۰ MB</span>
          <span class="chip active" onclick="setQuota(1,'GB',this)">۱ GB</span>
          <span class="chip" onclick="setQuota(5,'GB',this)">۵ GB</span>
          <span class="chip" onclick="setQuota(10,'GB',this)">۱۰ GB</span>
          <span class="chip" onclick="setQuota(50,'GB',this)">۵۰ GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-plug-connected"></i> پروتکل انتقال</div>
        <select id="nl-proto" style="display:none">
          <option value="vless-ws">VLESS / WebSocket</option>
          <option value="xhttp-packet-up">XHTTP Ultra · packet-up</option>
          <option value="xhttp-stream-up">XHTTP Ultra · stream-up</option>
        </select>
        <div class="proto-cards">
          <div class="proto-card active" data-val="vless-ws" onclick="selectProto('vless-ws',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-link"></i></div>
            <div class="proto-card-title">VLESS / WS</div>
            <div class="proto-card-desc">پایدار و همه‌منظوره</div>
          </div>
          <div class="proto-card" data-val="xhttp-packet-up" onclick="selectProto('xhttp-packet-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-bolt"></i></div>
            <div class="proto-card-title">XHTTP · packet-up</div>
            <div class="proto-card-desc">سازگار با CDN</div>
          </div>
          <div class="proto-card" data-val="xhttp-stream-up" onclick="selectProto('xhttp-stream-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-rocket"></i></div>
            <div class="proto-card-title">XHTTP · stream-up</div>
            <div class="proto-card-desc">تاخیر پایین‌تر</div>
          </div>
        </div>
      </div>
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-fingerprint"></i> Fingerprint (uTLS)</div>
          <select class="cp-input-full fs" id="nl-fp">
            <option value="chrome" selected>chrome</option>
            <option value="firefox">firefox</option>
            <option value="safari">safari</option>
            <option value="ios">ios</option>
            <option value="android">android</option>
            <option value="edge">edge</option>
            <option value="360">360</option>
            <option value="qq">qq</option>
            <option value="random">random</option>
            <option value="randomized">randomized</option>
          </select>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-antenna-bars-5"></i> ALPN</div>
          <select class="cp-input-full fs" id="nl-alpn-preset" onchange="onAlpnPresetChange()">
            <option value="">پیش‌فرض پروتکل</option>
            <option value="h2,http/1.1">h2,http/1.1</option>
            <option value="http/1.1">http/1.1</option>
            <option value="h2">h2</option>
            <option value="__custom__">دستی...</option>
          </select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-alpn" placeholder="مقدار دستی ALPN" style="display:none">
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-route"></i> پورت اتصال</div>
          <input class="cp-input-full" id="nl-port" type="number" min="1" max="65535" placeholder="443" value="443">
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-users"></i> محدودیت آی‌پی / کاربر هم‌زمان</div>
          <input class="cp-input-full" id="nl-iplimit" type="number" min="0" step="1" placeholder="0 = نامحدود" value="0">
          <div class="chip-row" id="iplimit-chips">
            <span class="chip active" onclick="setIpLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setIpLimit(1,this)">۱ کاربر</span>
            <span class="chip" onclick="setIpLimit(2,this)">۲ کاربر</span>
            <span class="chip" onclick="setIpLimit(5,this)">۵ کاربر</span>
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block" style="flex:1">
          <div class="cp-block-label"><i class="ti ti-gauge"></i> محدودیت سرعت</div>
          <div class="form-row">
            <input class="cp-input-full" id="nl-speed" type="number" min="0" step="0.5" placeholder="0 = نامحدود" value="0" style="flex:1">
            <select class="fs" id="nl-speed-unit" style="flex:0 0 100px">
              <option value="MBIT" selected>Mbps</option>
              <option value="KB">KB/s</option>
              <option value="MB">MB/s</option>
            </select>
          </div>
          <div class="chip-row" id="speed-chips">
            <span class="chip active" onclick="setSpeedLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setSpeedLimit(1,this)">۱ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(5,this)">۵ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(10,this)">۱۰ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(25,this)">۲۵ Mbps</span>
          </div>
        </div>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل پس از ساخت قابل تغییر نیست.</div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
      </div>
    </div>
  </div>
  <div class="bulk-toolbar" style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;padding:12px 14px;margin:12px 0;border:1px solid var(--border);border-radius:14px;background:rgba(255,255,255,.025)">
    <label style="display:flex;align-items:center;gap:7px;font-size:12px"><input type="checkbox" id="bulk-select-all" onchange="selectAllConfigs(this.checked)"> انتخاب همه</label>
    <span id="bulk-selected-count" style="font-size:11px;color:var(--t3);margin-inline-end:auto">۰ انتخاب</span>
    <button class="btn btn-sm btn-g" onclick="bulkConfigAction('activate')"><i class="ti ti-check"></i> فعال‌سازی</button>
    <button class="btn btn-sm btn-g" onclick="bulkConfigAction('deactivate')"><i class="ti ti-ban"></i> غیرفعال‌سازی</button>
    <button class="btn btn-sm btn-g" onclick="bulkConfigAction('reset_usage')"><i class="ti ti-rotate"></i> ریست مصرف</button>
    <button class="btn btn-sm btn-d" onclick="bulkConfigAction('delete')"><i class="ti ti-trash"></i> حذف انتخاب‌شده‌ها</button>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>
<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-folders"></i> گروه‌های ساب</div><div class="tb-sub">هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد</div></div>
    <div class="tb-right">
      <span class="badge bg-purple" id="subs-pg-cnt">۰ گروه</span>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> گروه جدید</button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search">
      <i class="ti ti-search"></i>
      <input type="text" id="subs-search-inp" placeholder="جستجو در گروه‌ها..." oninput="filterSubs(this.value)">
    </div>
  </div>
  <div class="sub-grid" id="subs-grid">
    <div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>
  </div>
</section>
<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-rss"></i> سابسکریپشن</div><div class="tb-sub">لینک‌های اشتراک برای اپ‌های v2ray</div></div></div>
  <div class="sec-hero">
    <div class="sec-hero-tile"><div class="sec-hero-ico"><i class="ti ti-rss"></i></div><div class="sec-hero-label">سابسکریپشن‌های فعال</div><div class="sec-hero-val" id="sb-count">—</div><div class="sec-hero-sub">گروه‌های دارای لینک ساب</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico pur"><i class="ti ti-link"></i></div><div class="sec-hero-label">کل کانفیگ‌ها</div><div class="sec-hero-val" id="sb-links">—</div><div class="sec-hero-sub">قابل اشتراک‌گذاری</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico amb"><i class="ti ti-devices"></i></div><div class="sec-hero-label">اپ‌های پشتیبانی‌شده</div><div class="sec-hero-val" style="font-size:15px">v2rayNG · Streisand</div><div class="sec-hero-sub">و سایر کلاینت‌های VLESS</div></div>
  </div>
  <div class="g2">
    <div class="sec-panel">
      <div class="sec-panel-head"><div class="sec-panel-ico"><i class="ti ti-rss"></i></div><div><div class="sec-panel-title">سابسکریپشن تکی</div><div class="sec-panel-sub">هر کانفیگ URL سابسکریپشن مخصوص دارد</div></div></div>
      <div class="sec-panel-body"><p style="font-size:11.5px;color:var(--t3);line-height:1.9">از کارت کانفیگ روی آیکون <i class="ti ti-rss" style="color:var(--accent)"></i> کلیک کنید تا URL سابسکریپشن اون کانفیگ کپی شه.</p></div>
    </div>
    <div class="sec-panel">
      <div class="sec-panel-head"><div class="sec-panel-ico pur"><i class="ti ti-database"></i></div><div><div class="sec-panel-title">سابسکریپشن کامل (ادمین)</div><div class="sec-panel-sub">شامل تمام کانفیگ‌های فعال</div></div></div>
      <div class="sec-panel-body">
        <div class="sub-box"><span class="sub-url" id="sub-all-url">در حال دریافت...</span><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g" onclick="window.open(location.protocol+'//'+location.host+'/sub-all')"><i class="ti ti-external-link"></i></button></div></div>
        <div class="cl amber" style="margin-top:11px"><i class="ti ti-alert-triangle"></i><span>این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).</span></div>
      </div>
    </div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico amb"><i class="ti ti-folders"></i></div><div><div class="sec-panel-title">لینک سابسکریپشن گروه‌ها</div><div class="sec-panel-sub">هر گروه یک صفحه پابلیک مجزا</div></div></div>
    <div class="sec-panel-body"><div id="sub-groups-list">در حال بارگذاری...</div></div>
  </div>
</section>
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل و مانیتورینگ مصرف پهنای باند</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>

  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> کل ترافیک مصرفی</div>
      <div class="traf-main-val" id="t-traffic">—<span>MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">میانگین ساعتی</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">پیک مصرف</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">بالاترین ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">کمترین مصرف</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
  </div>

  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> روند مصرف ترافیک</div>
        <div class="traf-chart-sub">بر اساس مگابایت در هر ساعت</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> مصرف</div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> میانگین</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">مانیتورینگ زنده‌ی آی‌پی و ترافیک هر اتصال</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>

  <div class="conn-hero">
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div>
      <div class="conn-hero-label">اتصالات زنده</div>
      <div class="conn-hero-val" id="ch-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-transfer"></i></div>
      <div class="conn-hero-label">مجموع ترافیک لحظه‌ای</div>
      <div class="conn-hero-val" id="ch-traffic">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-clock"></i></div>
      <div class="conn-hero-label">میانگین مدت اتصال</div>
      <div class="conn-hero-val" id="ch-avgdur">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div>
      <div class="conn-hero-label">آی‌پی‌های یکتا</div>
      <div class="conn-hero-val" id="ch-uniq">—</div>
    </div>
  </div>

  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> لیست اتصالات</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> بروزرسانی خودکار هر ۵ ثانیه</div>
  </div>

  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title">هیچ اتصال فعالی نیست</div>
    <div class="conn-empty-v2-sub">به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند</div>
  </div>
</section>

<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> فعالیت ساب‌ها</div><div class="tb-sub">کارتی ساب‌ها + اتصال زنده IP → کانفیگ + لاگ کامل</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i> رفرش</button></div></div>

  <!-- Sub cards -->
  <div id="act-subs" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin-bottom:20px"></div>

  <!-- Live connections -->
  <div class="card" style="margin-bottom:20px">
    <div class="card-title"><span class="m-ring" style="width:34px;height:34px;font-size:15px"><i class="ti ti-plug-connected"></i></span> اتصال‌های زنده <span class="ml-auto badge bg-green" id="act-conns-badge">۰</span></div>
    <div id="act-conns"></div>
    <div class="empty" id="act-conns-empty" style="display:none"><i class="ti ti-plug-connected"></i><p>الان اتصال فعالی وجود ندارد</p></div>
  </div>

  <!-- Full activity log -->
  <div class="card">
    <div class="card-title"><span class="m-ring r3" style="width:34px;height:34px;font-size:15px"><i class="ti ti-history"></i></span> لاگ کامل فعالیت</div>
    <div style="display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap">
      <input id="log-search" oninput="loadActivity()" placeholder="🔍 جستجو در لاگ..." style="flex:1;min-width:150px;background:var(--card-b);border:1px solid var(--card-b);border-radius:9px;padding:8px 11px;color:var(--t1);font-size:11.5px;outline:none">
      <select id="log-kind" onchange="loadActivity()" style="background:var(--card-b);border:1px solid var(--card-b);border-radius:9px;padding:8px 11px;color:var(--t1);font-size:11.5px;outline:none">
        <option value="">همه نوعها</option><option value="link">کانفیگ</option><option value="sub">گروه</option><option value="auth">ورود</option><option value="connection">اتصال</option><option value="system">سیستم</option>
      </select>
    </div>
    <div class="log-timeline" id="logs-list">—</div>
    <div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>هنوز لاگی ثبت نشده</p></div>
  </div>
</section>
<section class="pg" id="pg-errors">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-alert-triangle"></i> خطاها</div><div class="tb-sub">خطاهای ثبت‌شده‌ی سیستم</div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">۰</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div></div>
  <div class="sec-hero">
    <div class="sec-hero-tile"><div class="sec-hero-ico red"><i class="ti ti-bug"></i></div><div class="sec-hero-label">تعداد خطاها</div><div class="sec-hero-val" id="er-count">—</div><div class="sec-hero-sub">از زمان راه‌اندازی</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico amb"><i class="ti ti-alert-triangle"></i></div><div class="sec-hero-label">آخرین خطا</div><div class="sec-hero-val" id="er-last" style="font-size:14px">—</div><div class="sec-hero-sub" id="er-last-time">—</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico"><i class="ti ti-shield-check"></i></div><div class="sec-hero-label">وضعیت سیستم</div><div class="sec-hero-val" style="font-size:15px;color:var(--green-t)">سالم</div><div class="sec-hero-sub">همه سرویس‌ها فعال</div></div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico red"><i class="ti ti-bug"></i></div><div><div class="sec-panel-title">لاگ خطاها</div><div class="sec-panel-sub">خطاهای ثبت‌شده‌ی سیستم از زمان آخرین ریست</div></div></div>
    <div class="sec-panel-body"><div id="errs-full">—</div></div>
  </div>
</section>
<section class="pg" id="pg-testws">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> تست WebSocket</div></div></div>
  <div class="sec-panel" style="max-width:760px">
    <div class="sec-panel-head"><div class="sec-panel-ico"><i class="ti ti-wifi"></i></div><div><div class="sec-panel-title">تست WebSocket</div><div class="sec-panel-sub">تست اتصال VLESS/WS روی UUID فعال</div></div></div>
    <div class="sec-panel-body">
      <div class="cl amber" style="margin-top:0;margin-bottom:14px"><i class="ti ti-alert-triangle"></i><span>فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).</span></div>
      <div class="form-row" style="margin-bottom:12px">
        <div class="fg" style="flex:1"><label>UUID (باید در کانفیگ‌ها وجود داشته باشد)</label><input class="fi" id="ws-uuid" placeholder="UUID یک کانفیگ فعال" style="width:100%"></div>
        <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> اتصال</button>
        <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> قطع</button>
      </div>
      <div class="form-row" style="margin-bottom:14px">
        <input class="fi" id="ws-msg" placeholder="پیام تست..." style="flex:1">
        <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> ارسال</button>
      </div>
      <div class="sec-log-box" id="ws-log"><p>منتظر اتصال...</p></div>
    </div>
  </div>
</section>
<section class="pg" id="pg-categories">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-category"></i> دسته‌بندی کانفیگ‌ها</div><div class="tb-sub">کانفیگ‌ها را به دسته‌های منطقی تقسیم کنید</div></div>
    <div class="tb-right"><span class="badge bg-purple" id="cats-pg-cnt">۰ دسته</span></div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico amb"><i class="ti ti-plus"></i></div><div><div class="sec-panel-title">ساخت دسته جدید</div><div class="sec-panel-sub">نام و رنگ دسته را انتخاب کنید</div></div></div>
    <div class="sec-panel-body">
      <div class="cat-mgr-row" style="margin-bottom:12px">
        <input class="fi" id="cat-new-name" placeholder="نام دسته جدید (مثلاً: VIP)" style="flex:1">
        <input class="fi" id="cat-new-color" type="color" value="#10B981" style="width:46px;height:38px;padding:4px;border-radius:9px">
        <button class="btn btn-p" onclick="createCat()"><i class="ti ti-plus"></i> ساخت</button>
      </div>
    </div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico"><i class="ti ti-category"></i></div><div><div class="sec-panel-title">دسته‌های ساخته‌شده</div><div class="sec-panel-sub">هر دسته تعداد کانفیگ‌های متعلق به خود را نشان می‌دهد</div></div><div class="sec-panel-side"><button class="btn btn-p btn-sm" onclick="loadCats()"><i class="ti ti-refresh"></i> رفرش</button></div></div>
    <div class="sec-panel-body">
      <div class="cat-mgr" id="cat-list">در حال بارگذاری...</div>
    </div>
  </div>
</section>
<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div><div class="tb-sub">پیکربندی پنل و اطلاعات سرور</div></div></div>
  <div class="sec-hero">
    <div class="sec-hero-tile"><div class="sec-hero-ico"><i class="ti ti-server"></i></div><div class="sec-hero-label">نسخه پنل</div><div class="sec-hero-val" style="font-size:16px">FineVPN_v2ray v1.0.0</div><div class="sec-hero-sub">ساختار ۲۴ کانفیگ پرفورمنت</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico pur"><i class="ti ti-clock-hour-4"></i></div><div class="sec-hero-label">آپتایم سرور</div><div class="sec-hero-val" id="st-uptime" style="font-size:16px">—</div><div class="sec-hero-sub">از آخرین ریست</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico amb"><i class="ti ti-world"></i></div><div class="sec-hero-label">هاست پابلیک</div><div class="sec-hero-val" id="server-public-host" style="font-size:13px;overflow-wrap:anywhere">—</div><div class="sec-hero-sub">لینک‌های ساب از اینجا</div></div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico"><i class="ti ti-server"></i></div><div><div class="sec-panel-title">اطلاعات سرور</div><div class="sec-panel-sub">مشخصات زیرساخت فعال</div></div></div>
    <div class="sec-panel-body" id="set-server">در حال بارگذاری...</div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico amb"><i class="ti ti-database"></i></div><div><div class="sec-panel-title">ذخیره‌سازی و ماندگاری داده</div><div class="sec-panel-sub">کانفیگ‌ها، ساب‌ها و مصرف حجم بعد از دیپلوی حفظ می‌شوند؟</div></div></div>
    <div class="sec-panel-body" id="set-volume"></div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico pur"><i class="ti ti-user-circle"></i></div><div><div class="sec-panel-title">تغییر نام کاربری و رمز عبور</div><div class="sec-panel-sub">مدیریت دسترسی پنل</div></div></div>
    <div class="sec-panel-body">
      <div class="form-row" style="margin-top:0">
        <div class="fg" style="flex:1"><label><i class="ti ti-user"></i> نام کاربری جدید</label><input class="fi" id="cred-username-v2" placeholder="نام کاربری فعلی را نگه دارید" style="width:100%"></div>
      </div>
      <div class="form-row" style="margin-top:12px">
        <div class="fg" style="flex:1"><label><i class="ti ti-lock"></i> رمز فعلی</label><input class="fi" id="cred-current-v2" type="password" placeholder="رمز فعلی" style="width:100%"></div>
        <div class="fg" style="flex:1"><label><i class="ti ti-key"></i> رمز جدید</label><input class="fi" id="cred-new-v2" type="password" placeholder="خالی = بدون تغییر" style="width:100%"></div>
      </div>
      <div class="form-row" style="margin-top:14px;align-items:center">
        <button class="btn btn-p" onclick="saveCredentialsV2()"><i class="ti ti-device-floppy"></i> ذخیره تغییرات</button>
        <span id="cred-status-v2" style="font-size:11px;color:var(--t3)"></span>
      </div>
    </div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico amb"><i class="ti ti-database-export"></i></div><div><div class="sec-panel-title">پشتیبان‌گیری و بازیابی</div><div class="sec-panel-sub">بکاپ کامل کانفیگ‌ها و ساب‌ها</div></div></div>
    <div class="sec-panel-body">
      <div class="cl" style="margin-top:0"><i class="ti ti-info-circle"></i><span>فایل بکاپ شامل کانفیگ‌ها، گروه‌ها، حجم مصرفی و تنظیمات است. برای حفظ اطلاعات پس از استقرار مجدد، ذخیره‌سازی پایدار را فعال کنید و پشتیبان را جداگانه نگه دارید.</span></div>
      <div class="form-row" style="margin-top:14px;flex-wrap:wrap">
        <button class="btn btn-p" onclick="downloadBackupV2()"><i class="ti ti-download"></i> دانلود بکاپ</button>
        <button class="btn btn-o" onclick="document.getElementById('restore-file-v2').click()"><i class="ti ti-upload"></i> بارگذاری بکاپ</button>
        <input type="file" id="restore-file-v2" accept=".json" style="display:none" onchange="restoreBackupV2(this)">
        <span id="backup-status-v2" style="font-size:11px;color:var(--t3);align-self:center"></span>
      </div>
    </div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico red"><i class="ti ti-shield-lock"></i></div><div><div class="sec-panel-title">امنیت و نشست‌ها</div><div class="sec-panel-sub">مدیریت دستگاه‌های واردشده به پنل</div></div></div>
    <div class="sec-panel-body">
      <div class="log-timeline" id="sess-list">در حال بارگذاری...</div>
      <div style="margin-top:12px;display:flex;gap:8px;flex-wrap:wrap">
        <button class="btn btn-d btn-sm" onclick="revokeSessions()"><i class="ti ti-logout"></i> خروج از سایر دستگاه‌ها</button>
      </div>
    </div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico pur"><i class="ti ti-activity-heartbeat"></i></div><div><div class="sec-panel-title">منابع سرور</div><div class="sec-panel-sub">CPU، RAM و شبکه‌ی همین سرویس</div></div><div class="sec-panel-side"><span class="badge bg-green" id="tel-live"><span class="dot dg pulse"></span> زنده</span></div></div>
    <div class="sec-panel-body">
      <div class="tel-grid" id="tel-grid">در حال بارگذاری...</div>
    </div>
  </div>
</section>


</main>
<script>
let isDark=true;
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme','dark');
}
function toggleTheme(){{}}
applyTheme(isDark);
async function loadCats(){
  try{
    const d=await (await authF('/api/categories')).json();
    const el=document.getElementById('cat-list');if(!el)return;
    const cats=d.categories||[];
    const cc=document.getElementById('cats-pg-cnt');if(cc)cc.textContent=toFa(cats.length)+' دسته';
    if(!cats.length){el.innerHTML='<div class="empty"><i class="ti ti-category"></i><p>هنوز دسته‌ای ساخته نشده</p></div>';return}
    el.innerHTML='<div class="cat-mgr">'+cats.map(c=>`<div class="cat-mgr-row" style="padding:9px 12px;background:var(--card,#0d1c18);border:1px solid var(--line,rgba(255,255,255,.07));border-radius:11px">
      <span class="cat-dot" style="background:${esc(c.color||'#10B981')};width:9px;height:9px;flex:0 0 9px"></span>
      <b style="font-size:12.5px">${esc(c.name)}</b>
      <span class="badge bg-blue" style="font-size:10px">${toFa(c.links_count||0)} کانفیگ</span>
      <button class="btn btn-d btn-sm cat-del" onclick="delCat('${esc(c.id)}')"><i class="ti ti-trash"></i></button>
    </div>`).join('')+'</div>';
  }catch(e){}
}
async function createCat(){
  const name=(document.getElementById('cat-new-name').value||'').trim();
  if(!name){toast('نام دسته الزامی است','err');return}
  const color=document.getElementById('cat-new-color').value;
  try{
    const r=await authF('/api/categories',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,color})});
    if(!r.ok)throw 0;
    document.getElementById('cat-new-name').value='';
    toast('دسته ساخته شد ✓','ok');loadCats();
  }catch(e){toast('خطا در ساخت دسته','err')}
}
async function delCat(id){
  if(!confirm('حذف این دسته؟ کانفیگ‌ها به «عمومی» برمی‌گردند.'))return;
  try{
    const r=await authF('/api/categories/'+id,{method:'DELETE'});
    if(!r.ok)throw 0;
    toast('دسته حذف شد','ok');loadCats();loadLinks();
  }catch(e){toast('خطا در حذف','err')}
}
async function loadSessions(){
  try{
    const d=await (await authF('/api/sessions')).json();
    const el=document.getElementById('sess-list');if(!el)return;
    const ss=d.sessions||[];
    if(!ss.length){el.innerHTML='<div class="empty"><i class="ti ti-login"></i><p>نشست فعلی شما است</p></div>';return}
    el.innerHTML=ss.map(s=>{
      const lt=s.login_at?new Date(s.login_at*1000).toLocaleString('fa-IR',{dateStyle:'short',timeStyle:'short'}):'—';
      const dev=s.device||'نامشخص';
      const devIc=/iphone|ipad/.test(dev.toLowerCase())?'ti-device-mobile':/android/.test(dev.toLowerCase())?'ti-device-mobile':/windows/.test(dev.toLowerCase())?'ti-device-desktop':/mac/.test(dev.toLowerCase())?'ti-device-laptop':'ti-device-question';
      return `<div class="log-item"><div class="log-ic ${s.current?'ok':'warn'}"><i class="ti ${devIc}"></i></div>
        <div class="log-body" style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:6px">
          <span class="log-msg"><b>${esc(dev)}</b> <code style="opacity:.55;font-size:10px">${esc(s.token)}</code></span>
          <span style="display:flex;gap:10px;align-items:center;font-size:10.5px;color:var(--t3)">
            <span title="آی‌پی"><i class="ti ti-world" style="font-size:11px"></i> ${esc(s.ip||'نامشخص')}</span>
            <span title="زمان ورود"><i class="ti ti-login" style="font-size:11px"></i> ${esc(lt)}</span>
            <b style="font-size:11px;color:var(--t3)">${toFa(s.expires_in_hours)} ساعت</b>
          </span>
        </div></div>`;}).join('');
  }catch(e){}
}
async function revokeSessions(){
  if(!confirm('از همه‌ی دستگاه‌های دیگر خارج می‌شوید. ادامه؟'))return;
  try{
    const r=await authF('/api/security/revoke-other-sessions',{method:'POST'});
    const d=await r.json();
    toast((d.revoked||0)+' نشست لغو شد','ok');loadSessions();
  }catch(e){toast('خطا','err')}
}
let telTimer=null;
async function loadTelemetry(){
  try{
    const d=await (await authF('/api/telemetry')).json();
    const el=document.getElementById('tel-grid');if(!el||!d.ok)return;
    const cpuPct=Math.min(100,Math.max(0,d.cpu.host_pct||0));
    const memPct=d.mem.rss_mb&&d.mem.host_total_mb?Math.min(100,d.mem.rss_mb/d.mem.host_total_mb*100):0;
    el.innerHTML=[
      ['ti-cpu','پردازنده',d.cpu.host_pct+'%','روی '+toFa(d.cpu.cores)+' هسته · لود '+d.cpu.load_pct+'%',cpuPct],
      ['ti-memory','حافظه (این سرویس)',d.mem.rss_mb+' MB','از '+d.mem.host_total_mb+' MB کل سرور',memPct],
      ['ti-hard-drive','دیسک',d.disk.used_gb+' GB','از '+d.disk.total_gb+' GB · '+d.disk.free_pct+'% آزاد',100-d.disk.free_pct],
      ['ti-network','شبکه','↑ '+d.net.sent_mb+' MB','↓ '+d.net.recv_mb+' MB',null],
    ].map(t=>`<div class="tel-tile"><div class="tt-l"><i class="ti ${t[0]}"></i> ${t[1]}</div><div class="tt-v">${t[2]}</div><div class="tt-s">${t[3]}</div>${t[4]!==null?`<div class="tel-bar"><i style="width:${Math.min(100,t[4]).toFixed(0)}%"></i></div>`:''}</div>`).join('');
  }catch(e){}
}
function startTelemetry(){if(!telTimer)telTimer=setInterval(()=>{if(document.getElementById('pg-settings').classList.contains('on'))loadTelemetry()},3000)}

function toast(msg,type=''){
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';
  const d=daysLeft(exp);
  if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(d<=3)return `<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> ${toFa(d)} روز مانده</span>`;
  return `<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> ${toFa(d)} روز مانده</span>`;
}
function protoBadge(p){
  const m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp-packet-up':['XHTTP · packet-up','pc-xhttp'],'xhttp-stream-up':['XHTTP · stream-up','pc-xhttp']};
  const v=m[p]||m['vless-ws'];
  return `<span class="proto-chip ${v[1]}">${v[0]}</span>`;
}
let currentLang=localStorage.getItem('finevpn-v2ray-lang')||'fa';
const I18N={
'داشبورد':'Dashboard','کانفیگ‌ها':'Configurations','گروه‌های ساب':'Subscription Groups','سابسکریپشن':'Subscriptions','ترافیک':'Traffic','اتصالات':'Connections','امنیت':'Security','لاگ فعالیت‌ها':'Activity Logs','خطاها':'Errors','تست WebSocket':'WebSocket Test','تنظیمات':'Settings','پشتیبانی':'Support','ورود به داشبورد':'Sign in to dashboard','ورود به پنل':'Panel Sign In','ساخت کانفیگ جدید':'Create New Configuration','گروه‌های ساب':'Subscription Groups','پشتیبانی':'Support','تنظیمات سیستم':'System Settings','تغییر رمز عبور':'Change Password','ذخیره تغییرات':'Save Changes','ذخیره رمز جدید':'Save New Password','انصراف':'Cancel','ذخیره':'Save','بستن':'Close','رفرش':'Refresh','کپی':'Copy','دانلود Backup':'Download Backup','Export لینک‌ها':'Export Links','پشتیبانی مستقیم':'Direct Support','وب‌سایت رسمی':'Official Website','تلگرام':'Telegram','اینستاگرام':'Instagram','یوتیوب':'YouTube','توییتر / X':'Twitter / X','سازنده':'Creator','فعال':'Active','نامحدود':'Unlimited','در حال بارگذاری...':'Loading...','پیش‌فرض اولیه · Initial defaults':'Initial defaults','نام کاربری':'Username','رمز عبور · Password':'Password','کد امنیتی · Security code':'Security code','کد / code':'Code','در حال ورود...':'Signing in...','خروج':'Logout','پنل':'Panel','سیستم':'System','کانفیگ‌ها':'Configurations','گروه جدید':'New Group','ساخت کانفیگ':'Create Configuration','ساخت سریع گروه ساب (۲۴ کانفیگ)':'Quick Subscription Group (24 Configs)','ساخت خودکار گروه ساب، تنظیم حجم مشترک و تولید ۲۴ کانفیگ با یک کلیک':'Create a subscription group with shared quota and 24 configs in one click','گروه دسترسی':'Access Group','کپی همه‌ی کانفیگ‌ها':'Copy All Configurations','کپی همه':'Copy All','اتصالات زنده':'Live Connections','کل مصرف':'Total Usage','سهمیه و اعتبار گروه':'Group Quota and Validity','کانفیگ‌های فعال':'Active Configurations','ذخیره‌سازی و ماندگاری داده':'Storage and Data Persistence','پشتیبان‌گیری و بازیابی':'Backup and Restore','امنیت و نشست‌ها':'Security and Sessions','تغییر نام کاربری و رمز عبور':'Change Username and Password','دانلود بکاپ':'Download Backup','بارگذاری بکاپ':'Upload Backup','حذف':'Delete','فعال':'Active','غیرفعال':'Inactive','ساخت':'Create','هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد':'Each group has its own public page and configurations','نام کانفیگ':'Configuration name','عنوان':'Title','نام گروه ساب':'Subscription group name','گروه‌های اشتراک':'Subscription groups','گروه اشتراک':'Subscription group','توضیحات':'Description','حجم':'Traffic quota','حجم مشترک':'Shared quota','مدت اعتبار':'Validity period','روز':'days','بدون محدودیت':'Unlimited','مصرف‌شده':'Used','باقی‌مانده':'Remaining','آمار':'Statistics','عملیات':'Actions','ذخیره':'Save','بازگشت':'Back','بستن':'Close','لغو':'Cancel','حذف گروه':'Delete group','حذف کانفیگ':'Delete configuration','تأیید':'Confirm','بله':'Yes','خیر':'No','در حال ذخیره...':'Saving...','خطا':'Error','موفقیت':'Success','اطلاعات ذخیره شد':'Information saved','کشور خروجی':'Exit-country label','پرچم کشور':'Country flag','انتخاب همه':'Select all','انتخاب‌شده':'Selected','حذف انتخاب‌شده‌ها':'Delete selected','فعال‌سازی':'Activate','غیرفعال‌سازی':'Deactivate','ریست مصرف':'Reset usage','رنگ پنل':'Panel color','آبی':'Blue','بنفش':'Purple','سبز زمردی':'Emerald','طلایی':'Gold','تازه‌سازی':'Refresh','پشتیبانی @sadiq_AFG1':'Support @sadiq_AFG1'

,'مدیریت کانفیگ‌های':'Manage configurations','کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید':'Choose the configurations to include in this group','انتخاب همه':'Select all','لغو همه':'Clear all','۰ انتخاب شده':'0 selected','تغییرات بلافاصله اعمال می‌شود':'Changes take effect immediately','ساخت گروه ساب':'Create subscription group','یک صفحه پابلیک مجزا با ۲۴ کانفیگ خودکار بسازید':'Create a separate public page with 24 automatically generated configurations','نام گروه':'Group name','توضیحات (اختیاری)':'Description (optional)','رمز صفحه پابلیک (اختیاری)':'Public page password (optional)','ساخت سریع ۲۴ کانفیگ':'Quick-create 24 configurations','۳ پروتکل × ۲ فینگرپرینت × ۴ ALPN = ۲۴ کانفیگ (VWS/XPU/XHS)':'3 protocols × 2 fingerprints × 4 ALPN options = 24 configurations','حجم مشترک کل (GB)':'Total shared quota (GB)','روزهای اعتبار':'Validity days','حداکثر کاربر هم‌زمان (IP Limit)':'Maximum simultaneous users (IP limit)','حجم مشترک بین تمام ۲۴ کانفیگ تقسیم می‌شود. هر کاربر از هر کانفیگی مصرف کند، از همین حجم کم می‌شود.':'The shared quota is used by all 24 configurations. Traffic from any configuration reduces this same quota.','ساخت گروه + ۲۴ کانفیگ':'Create group + 24 configurations','ویرایش کانفیگ':'Edit configuration','سهمیه (0 = نامحدود)':'Quota (0 = unlimited)','واحد':'Unit','انقضا (روز از الان، 0 = بدون تغییر/نامحدود)':'Expiry (days from now; 0 = unchanged/unlimited)','یادداشت':'Note','ALPN (خالی = پیش‌فرض)':'ALPN (blank = default)','پورت اتصال':'Connection port','محدودیت آی‌پی (0 = نامحدود)':'IP limit (0 = unlimited)','محدودیت سرعت (0 = نامحدود)':'Speed limit (0 = unlimited)','برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.':'Set expiry to 0 to keep the current expiry.','ساخت خودکار گروه ساب، تنظیم حجم مشترک و تولید ۲۴ کانفیگ با یک کلیک':'Create a subscription group, set a shared quota, and generate 24 configurations in one click','نام گروه ساب':'Subscription group name','حجم مشترک (GB) —':'Shared quota (GB) —','۰ = نامحدود':'0 = unlimited','مدت اعتبار (روز) —':'Validity period (days) —','سقف کاربر (IP) —':'User limit (IP) —','ساخت گروه ساب + ۲۴ کانفیگ با حجم مشترک':'Create subscription group + 24 configurations with shared quota','گروه ساب و ۲۴ کانفیگ با موفقیت ساخته شد!':'Subscription group and 24 configurations created successfully!','رفرش':'Refresh','اتصالات فعال':'Active connections','زنده':'Live','کل ترافیک':'Total traffic','از راه‌اندازی':'Since startup','کانفیگ فعال':'Active configuration','از کل':'of total','لینک پیش‌فرض (بدون محدودیت)':'Default link (unlimited)','در حال دریافت...':'Loading...','کانفیگ محدود':'Limited configuration','ترافیک ساعتی (MB)':'Hourly traffic (MB)','توزیع پروتکل‌ها':'Protocol distribution','وضعیت سرویس':'Service status','فعال · سخت‌گیرانه':'Active · strict','فعال · 3 mode':'Active · 3 modes','فعال v9':'Active v9','آپتایم':'Uptime','بار نسبی':'Relative load','ارائه‌دهنده: مـحـمـدصـادق افـغـان':'Provider: Muhammad Sadiq Afghan','ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی':'Create and manage configurations with quotas, expiry, and groups','همه دسته‌ها':'All categories','ساخت کانفیگ جدید':'Create new configuration','UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن':'Random UUID · choose quota, expiry, and protocol','شناسه کانفیگ':'Configuration ID','— بدون دسته —':'— No category —','گروه ساب و انقضا':'Subscription group and expiry','— بدون گروه —':'— No group —','۷ روز':'7 days','۳۰ روز':'30 days','۹۰ روز':'90 days','سهمیه ترافیک':'Traffic quota','۵۰۰ MB':'500 MB','۱ GB':'1 GB','۵ GB':'5 GB','۱۰ GB':'10 GB','۵۰ GB':'50 GB','پروتکل انتقال':'Transport protocol','پایدار و همه‌منظوره':'Stable and general-purpose','سازگار با CDN':'CDN compatible','تاخیر پایین‌تر':'Lower latency','پیش‌فرض پروتکل':'Protocol default','دستی...':'Manual...','محدودیت آی‌پی / کاربر هم‌زمان':'IP limit / simultaneous users','۱ کاربر':'1 user','۲ کاربر':'2 users','۵ کاربر':'5 users','۱ Mbps':'1 Mbps','۵ Mbps':'5 Mbps','۱۰ Mbps':'10 Mbps','۲۵ Mbps':'25 Mbps','UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل پس از ساخت قابل تغییر نیست.':'UUIDs are random · only registered UUIDs can connect · protocol cannot be changed after creation.','هنوز کانفیگی وجود ندارد':'No configurations yet','هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد':'Each group has its own public page and configurations','۰ گروه':'0 groups','گروه جدید':'New group','هنوز گروهی وجود ندارد':'No groups yet','یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید':'Create a group to organize configurations','لینک‌های اشتراک برای اپ‌های v2ray':'Subscription links for V2Ray apps','ظاهر و زبان':'Appearance and language','انتخاب رنگ پنل ذخیره می‌شود و برای مرورگر شما باقی می‌ماند.':'The panel color is saved in this browser.','تغییر زبان فارسی / English':'Switch language Persian / English','سابسکریپشن‌های فعال':'Active subscriptions','گروه‌های دارای لینک ساب':'Groups with subscription links','کل کانفیگ‌ها':'Total configurations','قابل اشتراک‌گذاری':'Shareable','اپ‌های پشتیبانی‌شده':'Supported apps','و سایر کلاینت‌های VLESS':'and other VLESS clients','سابسکریپشن تکی':'Individual subscription','هر کانفیگ URL سابسکریپشن مخصوص دارد':'Each configuration has its own subscription URL','از کارت کانفیگ روی آیکون':'On a configuration card, click the icon','کلیک کنید تا URL سابسکریپشن اون کانفیگ کپی شه.':'to copy that configuration’s subscription URL.','سابسکریپشن کامل (ادمین)':'Full subscription (admin)','شامل تمام کانفیگ‌های فعال':'Includes all active configurations','این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).':'This URL works only in a browser signed in to the panel (session cookie required).','لینک سابسکریپشن گروه‌ها':'Group subscription links','هر گروه یک صفحه پابلیک مجزا':'Each group has a separate public page','تحلیل و مانیتورینگ مصرف پهنای باند':'Bandwidth usage analytics and monitoring','کل ترافیک مصرفی':'Total traffic used','میانگین ساعتی':'Hourly average','MB در ساعت':'MB per hour','پیک مصرف':'Peak usage','بالاترین ساعت':'Highest hour','کمترین مصرف':'Lowest usage','روند مصرف ترافیک':'Traffic usage trend','بر اساس مگابایت در هر ساعت':'Megabytes per hour','مصرف':'Usage','میانگین':'Average','مانیتورینگ زنده‌ی آی‌پی و ترافیک هر اتصال':'Live IP and traffic monitoring for each connection','مجموع ترافیک لحظه‌ای':'Current total traffic','میانگین مدت اتصال':'Average connection duration','آی‌پی‌های یکتا':'Unique IPs','لیست اتصالات':'Connection list','بروزرسانی خودکار هر ۵ ثانیه':'Auto-refresh every 5 seconds','هیچ اتصال فعالی نیست':'No active connections','به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند':'Clients appear here when they connect','فعالیت ساب‌ها':'Subscription activity','کارتی ساب‌ها + اتصال زنده IP → کانفیگ + لاگ کامل':'Subscription cards + live IP-to-config connections + full logs','اتصال‌های زنده':'Live connections','الان اتصال فعالی وجود ندارد':'There are no active connections right now','لاگ کامل فعالیت':'Full activity log','همه نوعها':'All types','کانفیگ':'Configuration','گروه':'Group','ورود':'Login','اتصال':'Connection','هنوز لاگی ثبت نشده':'No logs recorded yet','خطاهای ثبت‌شده‌ی سیستم':'System errors recorded','تعداد خطاها':'Error count','از زمان راه‌اندازی':'Since startup','آخرین خطا':'Latest error','وضعیت سیستم':'System status','سالم':'Healthy','همه سرویس‌ها فعال':'All services are active','لاگ خطاها':'Error log','خطاهای ثبت‌شده‌ی سیستم از زمان آخرین ریست':'System errors since the last reset','تست اتصال VLESS/WS روی UUID فعال':'Test VLESS/WS connection using an active UUID','فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).':'Only registered, active UUIDs can connect (this tests VLESS/WS; test XHTTP from the client app).','UUID (باید در کانفیگ‌ها وجود داشته باشد)':'UUID (must exist in configurations)','قطع':'Disconnect','ارسال':'Send','منتظر اتصال...':'Waiting for connection...','دسته‌بندی کانفیگ‌ها':'Configuration categories','کانفیگ‌ها را به دسته‌های منطقی تقسیم کنید':'Organize configurations into logical categories','۰ دسته':'0 categories','ساخت دسته جدید':'Create category','نام و رنگ دسته را انتخاب کنید':'Choose a category name and color','دسته‌های ساخته‌شده':'Created categories','هر دسته تعداد کانفیگ‌های متعلق به خود را نشان می‌دهد':'Each category shows how many configurations belong to it','پیکربندی پنل و اطلاعات سرور':'Panel configuration and server information','نسخه پنل':'Panel version','ساختار ۲۴ کانفیگ پرفورمنت':'24-configuration performance setup','آپتایم سرور':'Server uptime','از آخرین ریست':'Since last reset','هاست پابلیک':'Public host','لینک‌های ساب از اینجا':'Subscription links from here','اطلاعات سرور':'Server information','مشخصات زیرساخت فعال':'Active infrastructure details','کانفیگ‌ها، ساب‌ها و مصرف حجم بعد از دیپلوی حفظ می‌شوند؟':'Do configurations, subscriptions, and traffic usage persist after deployment?','مدیریت دسترسی پنل':'Panel access management','نام کاربری جدید':'New username','رمز فعلی':'Current password','رمز جدید':'New password','بکاپ کامل کانفیگ‌ها و ساب‌ها':'Full backup of configurations and subscriptions','فایل بکاپ شامل کانفیگ‌ها، گروه‌ها، حجم مصرفی و تنظیمات است. برای حفظ اطلاعات پس از استقرار مجدد، ذخیره‌سازی پایدار را فعال کنید و پشتیبان را جداگانه نگه دارید.':'The backup contains configurations, groups, traffic usage, and settings. Enable persistent storage and keep a separate backup to retain data after redeployments.','بارگذاری بکاپ':'Upload backup','مدیریت دستگاه‌های واردشده به پنل':'Manage devices signed in to the panel','خروج از سایر دستگاه‌ها':'Sign out of other devices','منابع سرور':'Server resources','CPU، RAM و شبکه‌ی همین سرویس':'CPU, RAM, and network usage for this service'
};
Object.assign(I18N, {"دسته‌بندی‌ها":"Categories","۰ کانفیگ":"0 configurations","محدودیت سرعت":"Speed limit","۰ انتخاب":"0 selected","۰":"0","جستجوی کانفیگ...":"Search configurations...","مثلاً: کانال اختصاصی":"e.g. VIP group","توضیح کوتاه درباره این گروه":"Short description of this group","خالی بگذارید = بدون رمز":"Leave blank = no password","مثلا 1 (خالی = نامحدود)":"e.g. 1 (blank = unlimited)","مثلا 30 (۰ = بدون انقضا)":"e.g. 30 (0 = no expiry)","مثلا 2 (۰ = نامحدود)":"e.g. 2 (0 = unlimited)","مثلاً: h2,http/1.1":"e.g. h2,http/1.1","مثلاً: سرویس VIP":"e.g. VIP service","مثلاً: کاربر علی":"e.g. User Ali","یادداشت (اختیاری)":"Note (optional)","انقضا (روز) · 0 = نامحدود":"Expiry (days) · 0 = unlimited","0 = نامحدود":"0 = unlimited","مقدار دستی ALPN":"Manual ALPN value","جستجو در گروه‌ها...":"Search groups...","🔍 جستجو در لاگ...":"🔍 Search logs...","UUID یک کانفیگ فعال":"UUID of an active configuration","پیام تست...":"Test message...","نام دسته جدید (مثلاً: VIP)":"New category name (e.g. VIP)","نام کاربری فعلی را نگه دارید":"Keep current username","خالی = بدون تغییر":"Blank = no change","وضعیت ذخیره‌سازی":"Storage status","دسته":"Category","هنوز دسته‌ای ساخته نشده":"No categories have been created yet","نام دسته الزامی است":"Category name is required","دسته ساخته شد ✓":"Category created ✓","خطا در ساخت دسته":"Failed to create category","حذف این دسته؟ کانفیگ‌ها به «عمومی» برمی‌گردند.":"Delete this category? Configurations will be moved to General.","دسته حذف شد":"Category deleted","خطا در حذف":"Delete failed","نشست فعلی شما است":"This is your current session","نامشخص":"Unknown","آی‌پی":"IP address","زمان ورود":"Login time","از همه‌ی دستگاه‌های دیگر خارج می‌شوید. ادامه؟":"You will be signed out from all other devices. Continue?","نشست لغو شد":"Session revoked","پردازنده":"CPU","روی":"on","هسته · لود":"cores · load","حافظه (این سرویس)":"Memory (this service)","MB کل سرور":"MB total server memory","دیسک":"Disk","% آزاد":"% free","شبکه":"Network","منقضی":"Expired","نامحدود":"Unlimited","حالت فارسی فعال شد":"Persian mode enabled","رمز فعلی را وارد کنید":"Enter the current password","چیزی برای تغییر وارد نشده":"Nothing to change was entered","رمز جدید حداقل ۶ کاراکتر":"New password must be at least 6 characters","در حال ذخیره...":"Saving...","خطا در به‌روزرسانی":"Update failed","✓ ذخیره شد":"✓ Saved","اعلان ورود به‌روزرسانی شد ✓":"Login notice updated ✓","در حال ساخت بکاپ...":"Creating backup...","خطا در ساخت بکاپ":"Backup creation failed","✓ بکاپ دانلود شد":"✓ Backup downloaded","بازگردانی بکاپ، تمام کانفیگ‌ها و ساب‌های فعلی را جایگزین می‌کند. ادامه می‌دهید؟":"Restoring this backup will replace all current configurations and subscriptions. Continue?","در حال بازگردانی...":"Restoring...","خطا در بازگردانی":"Restore failed","کانفیگ و":"Configuration and","ساب بازگردانی شد":"subscription restored","بکاپ بازگردانی شد ✓":"Backup restored ✓","فایل پشتیبان دانلود شد":"Backup file downloaded","دانلود پشتیبان ناموفق بود":"Backup download failed","Export لینک‌ها ناموفق بود":"Failed to export links","ولوم دائمی":"Persistent volume","ذخیره موقت":"Temporary storage","دیسک دائمی:":"Persistent storage:","مگابایت آزاد":"MB free","هیچ Volume پایداری شناسایی نشد؛ یک Volume به سرویس متصل کنید و Mount Path را /data قرار دهید.":"No persistent Volume detected. Attach a Volume to the service and set its mount path to /data.","آخرین بروزرسانی:":"Last updated:","همین الان":"just now","دقیقه پیش":"minutes ago","ساعت پیش":"hours ago","روز پیش":"days ago","روشن/خاموش":"Enable/disable","هنوز سابی وجود ندارد":"No subscriptions yet","در حال بارگذاری...":"Loading...","الان اتصال فعالی برای این ساب وجود ندارد":"There is no active connection for this subscription right now","مصرف به تفکیک کانفیگ":"Usage by configuration","هنوز رویدادی ثبت نشده":"No events recorded yet","ساب روشن شد ✓":"Subscription enabled ✓","ساب خاموش شد":"Subscription disabled","خطا در تغییر وضعیت":"Failed to change status","انتخاب کانفیگ":"Select configuration","UUID کپی شد":"UUID copied","آی‌پی‌های متصل / محدودیت":"Connected IPs / limit","فعال/غیرفعال":"Enable/disable","لینک کپی شد":"Link copied","Sub کپی شد":"Sub copied","ویرایش":"Edit","انتخاب":"Select","ابتدا کانفیگ‌ها را انتخاب کنید":"Select configurations first","فعال‌کردن":"Activate","غیرفعال‌کردن":"Deactivate","صفرکردن مصرف":"Reset usage","این کانفیگ‌ها برای همیشه حذف می‌شوند. ادامه می‌دهید؟":"These configurations will be permanently deleted. Continue?","برای کانفیگ اجرا شود؟":"Apply to the selected configurations?","مورد انجام شد ✓":"items processed ✓","عملیات گروهی ناموفق بود:":"Bulk operation failed:","کانفیگ جدید":"New configuration","کانفیگ ساخته شد ✓":"Configuration created ✓","خطا در ساخت":"Creation failed","کانفیگ ویرایش شد ✓":"Configuration updated ✓","خطا در ویرایش":"Update failed","فعال شد ✓":"Enabled ✓","غیرفعال شد":"Disabled","مصرف ریست شد ✓":"Usage reset ✓","حذف این کانفیگ؟":"Delete this configuration?","حذف شد ✓":"Deleted ✓","بدون توضیحات":"No description","رمزدار":"Password-protected","پابلیک":"Public","صفحه پابلیک":"Public page","لینک پابلیک کپی شد":"Public link copied","کپی پابلیک":"Copy public link","باز کردن":"Open","لینک ساب (base64)":"Subscription link (base64)","لینک ساب کپی شد":"Subscription link copied","کپی ساب":"Copy subscription","QR ساب":"Subscription QR","گروه ساخته شد ✓":"Group created ✓","خطا در ساخت گروه":"Failed to create group","گروه سریع":"Quick group","نام گروه را وارد کنید":"Enter a group name","مقادیر نمی‌توانند منفی باشند":"Values cannot be negative","حجم مشترک حداقل ۱ مگابایت باید باشد":"Shared quota must be at least 1 MB","در حال ساخت...":"Creating...","ساخت گروه شکست خورد":"Group creation failed","هشدار: تنظیم حجم مشترک ناموفق بود":"Warning: failed to set shared quota","هشدار: حجم مشترک درست ثبت نشد":"Warning: shared quota was not saved correctly","کانفیگ ساخته شد":"Configuration created","گروه ساخته شد. لینک سابسکریپشن کپی شود؟":"Group created. Copy the subscription link?","خطا در ساخت سریع":"Quick creation failed","این گروه و فقط کانفیگ‌های وابسته به همین گروه حذف می‌شوند. کانفیگ‌های گروه‌های دیگر باقی می‌مانند. ادامه می‌دهید؟":"This group and only its associated configurations will be deleted. Configurations in other groups will remain. Continue?","گروه حذف شد ✓":"Group deleted ✓","خطا در بارگذاری":"Loading failed","کپی لینک VLESS":"Copy VLESS link","ساب کپی شد":"Subscription copied","کپی Sub URL":"Copy Sub URL","QR کد":"QR code","انتخاب شده":"selected","کانفیگ‌های گروه ذخیره شدند ✓":"Group configurations saved ✓","خطا در ذخیره":"Save failed","کپی شد":"Copied","کپی شد ✓":"Copied ✓","ثانیه":"seconds","دقیقه":"minutes","ساعت":"hours","IP کپی شد":"IP copied","کپی IP":"Copy IP","بدون خطا":"No errors","سیستم پایدار":"System stable","رفرش شد":"Refreshed","UUID را وارد کنید":"Enter a UUID","اتصال:":"Connection:","✓ متصل - UUID معتبر":"✓ Connected - valid UUID","✗ خطا - UUID نامعتبر یا غیرفعال":"✗ Error - invalid or inactive UUID","دریافت":"Receive","- دسترسی رد شد":"- Access denied","ارسال:":"Send:","ساب گروه جدید":"New subscription group","در حال ساخت ۲۴ کانفیگ...":"Creating 24 configurations...","ساخت کانفیگ‌ها ناقص بود (":"Configuration creation was incomplete (","گروه ساب با ۲۴ کانفیگ ساخته شد":"Subscription group created with 24 configurations","خطا در ساخت ساب:":"Failed to create subscription:"});
Object.assign(I18N, {"دسته‌بندی‌ها":"Categories","محدودیت سرعت":"Speed limit","۰ کانفیگ":"0 configurations","۰ انتخاب":"0 selected","۰":"0"});
Object.assign(I18N, {"ظاهر پنل":"Panel appearance","تنظیم رنگ‌ها مستقل از صفحهٔ اشتراک؛ تنظیمات در همین مرورگر ذخیره می‌شود.":"Customize colors separately from the subscription page; settings are saved in this browser.","تم‌های آماده":"Presets","پالت رنگ":"Color palette","رنگ‌های سفارشی":"Custom colors","رنگ دکمه‌ها":"Button color","رنگ متن اصلی":"Main text color","رنگ حاشیه‌ها":"Border color","ذخیرهٔ رنگ‌ها":"Save colors","بازنشانی":"Reset","این تنظیمات فقط روی مرورگر شما اعمال می‌شوند و ظاهر پنل اشتراک را تغییر نمی‌دهند.":"These settings apply only in this browser and do not change the subscription portal.","رنگ‌های سفارشی ذخیره شد":"Custom colors saved","تنظیمات ظاهر بازنشانی شد":"Appearance reset"});
const I18N_TEXT_ORIGINALS=new WeakMap();
const I18N_ATTRIBUTE_ORIGINALS=new WeakMap();
function translatePage(lang){
  const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);const nodes=[];
  while(walker.nextNode())nodes.push(walker.currentNode);
  for(const node of nodes){
    const parent=node.parentElement;if(!parent||parent.closest('script,style,textarea,input,pre,code'))continue;
    if(!I18N_TEXT_ORIGINALS.has(node))I18N_TEXT_ORIGINALS.set(node,node.nodeValue||'');
    const original=I18N_TEXT_ORIGINALS.get(node);const match=original.match(/^(\s*)([\s\S]*?)(\s*)$/);if(!match)continue;
    const raw=match[2].trim();if(!raw)continue;
    const next=lang==='en'?(I18N[raw]||raw):raw;const value=match[1]+next+match[3];
    if(node.nodeValue!==value)node.nodeValue=value;
  }
  document.querySelectorAll('[placeholder],[title],[aria-label]').forEach(el=>{
    let originals=I18N_ATTRIBUTE_ORIGINALS.get(el);
    if(!originals){originals={};for(const attr of ['placeholder','title','aria-label'])if(el.hasAttribute(attr))originals[attr]=el.getAttribute(attr);I18N_ATTRIBUTE_ORIGINALS.set(el,originals);}
    for(const [attr,original] of Object.entries(originals)){if(original!==null&&original!==undefined)el.setAttribute(attr,lang==='en'?(I18N[original]||original):original);}
  });
  const btn=document.getElementById('language-toggle');const buttonHtml='<i class="ti ti-language"></i> '+(lang==='fa'?'English':'فارسی');if(btn&&btn.innerHTML!==buttonHtml)btn.innerHTML=buttonHtml;
}
function applyLanguage(lang){currentLang=lang==='en'?'en':'fa';try{localStorage.setItem('finevpn-v2ray-lang',currentLang);document.documentElement.lang=currentLang;document.documentElement.dir=currentLang==='fa'?'rtl':'ltr';}catch(e){}translatePage(currentLang);}
function toggleLanguage(){applyLanguage(currentLang==='en'?'fa':'en');toast(currentLang==='en'?'English mode enabled':'حالت فارسی فعال شد');}
function applyAccentTheme(theme){const allowed=['blue','purple','emerald','gold'];const chosen=allowed.includes(theme)?theme:'blue';document.documentElement.setAttribute('data-accent',chosen);try{localStorage.setItem('finevpn-v2ray-accent',chosen);}catch(e){}const sel=document.getElementById('accent-theme-select');if(sel&&sel.value!==chosen)sel.value=chosen;}
function fineHex(value,fallback){return /^#[0-9a-fA-F]{6}$/.test(value||'')?value:fallback;}
function applyCustomAppearance(save=true){
  let colors={button:'#60a5fa',text:'#f5f4ff',border:'#60a5fa'};
  try{const stored=JSON.parse(localStorage.getItem('finevpn-v2ray-custom-colors')||'{}');colors={button:fineHex(stored.button,colors.button),text:fineHex(stored.text,colors.text),border:fineHex(stored.border,colors.border)}}catch(e){}
  const b=document.getElementById('theme-button-color'),t=document.getElementById('theme-text-color'),r=document.getElementById('theme-border-color');
  if(b&&b.value)colors.button=fineHex(b.value,colors.button);if(t&&t.value)colors.text=fineHex(t.value,colors.text);if(r&&r.value)colors.border=fineHex(r.value,colors.border);
  document.documentElement.style.setProperty('--t1',colors.text);document.documentElement.style.setProperty('--card-b',colors.border+'55');document.documentElement.style.setProperty('--card-bh',colors.border+'bb');
  let style=document.getElementById('fine-custom-appearance-css');if(!style){style=document.createElement('style');style.id='fine-custom-appearance-css';document.head.appendChild(style)}
  style.textContent='html[data-accent] .btn-p,html[data-accent] .btn-pur,html[data-accent] .menu-btn{background:linear-gradient(135deg,'+colors.button+','+colors.button+')!important;border-color:'+colors.border+'!important;color:#fff!important}.nav-it.on{border-right-color:'+colors.button+'!important}.card,.metric,.cfg-card,.sec-panel,.sub-exp-card{border-color:'+colors.border+'77!important}';
  if(b)b.value=colors.button;if(t)t.value=colors.text;if(r)r.value=colors.border;
  if(save){try{localStorage.setItem('finevpn-v2ray-custom-colors',JSON.stringify(colors))}catch(e){}}
}
function saveCustomAppearance(){applyCustomAppearance(true);toast('رنگ‌های سفارشی ذخیره شد','ok')}
function loadCustomAppearance(){let raw=null;try{raw=localStorage.getItem('finevpn-v2ray-custom-colors')}catch(e){}if(!raw)return;try{const c=JSON.parse(raw);const b=document.getElementById('theme-button-color'),t=document.getElementById('theme-text-color'),r=document.getElementById('theme-border-color');if(b)b.value=fineHex(c.button,'#60a5fa');if(t)t.value=fineHex(c.text,'#f5f4ff');if(r)r.value=fineHex(c.border,'#60a5fa')}catch(e){}applyCustomAppearance(false)}
function resetCustomAppearance(){try{localStorage.removeItem('finevpn-v2ray-custom-colors')}catch(e){};const b=document.getElementById('theme-button-color'),t=document.getElementById('theme-text-color'),r=document.getElementById('theme-border-color');if(b)b.value='#60a5fa';if(t)t.value='#f5f4ff';if(r)r.value='#60a5fa';try{document.getElementById('fine-custom-appearance-css')?.remove();document.documentElement.style.removeProperty('--t1');document.documentElement.style.removeProperty('--card-b');document.documentElement.style.removeProperty('--card-bh')}catch(e){}applyAccentTheme('blue');toast('تنظیمات ظاهر بازنشانی شد','ok')}
applyLanguage(currentLang);
applyAccentTheme(localStorage.getItem('finevpn-v2ray-accent')||'blue');
loadCustomAppearance();
const _i18nObserver=new MutationObserver(()=>{if(!document.documentElement.dataset.i18nUpdating){document.documentElement.dataset.i18nUpdating='1';translatePage(currentLang);delete document.documentElement.dataset.i18nUpdating;}});
_i18nObserver.observe(document.body,{subtree:true,childList:true});

async function saveCredentialsV2(){
  const username=document.getElementById('cred-username-v2').value.trim();
  const current_password=document.getElementById('cred-current-v2').value;
  const new_password=document.getElementById('cred-new-v2').value;
  const st=document.getElementById('cred-status-v2');
  if(!current_password){st.textContent='رمز فعلی را وارد کنید';st.style.color='var(--red-t)';return}
  if(!username&&!new_password){st.textContent='چیزی برای تغییر وارد نشده';st.style.color='var(--red-t)';return}
  if(new_password&&new_password.length<6){st.textContent='رمز جدید حداقل ۶ کاراکتر';st.style.color='var(--red-t)';return}
  st.innerHTML='<i class="ti ti-loader-2 ti-spin"></i> در حال ذخیره...';st.style.color='var(--t3)';
  try{
    const r=await authF('/api/change-credentials',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:username||undefined,current_password,new_password:new_password||undefined})});
    const d=await r.json();if(!r.ok)throw Error(d.detail||'خطا در به‌روزرسانی');
    st.textContent='✓ ذخیره شد';st.style.color='var(--green-t)';
    document.getElementById('cred-current-v2').value='';document.getElementById('cred-new-v2').value='';
    toast('اعلان ورود به‌روزرسانی شد ✓','ok');
    if(username)setTimeout(()=>location.reload(),1200);
  }catch(e){st.textContent=e.message;st.style.color='var(--red-t)'}
}
async function downloadBackupV2(){
  const st=document.getElementById('backup-status-v2');
  st.innerHTML='<i class="ti ti-loader-2 ti-spin"></i> در حال ساخت بکاپ...';st.style.color='var(--t3)';
  try{
    const r=await authF('/api/backup');
    if(!r.ok)throw Error('خطا در ساخت بکاپ');
    const blob=await r.blob();
    const a=document.createElement('a');
    a.href=URL.createObjectURL(blob);
    a.download='finevpn-v2ray-backup-'+new Date().toISOString().slice(0,10)+'.json';
    document.body.appendChild(a);a.click();a.remove();
    st.textContent='✓ بکاپ دانلود شد';st.style.color='var(--green-t)';
  }catch(e){st.textContent=e.message;st.style.color='var(--red-t)'}
}
async function restoreBackupV2(input){
  const file=input.files[0];if(!file)return;
  const st=document.getElementById('backup-status-v2');
  if(!confirm('بازگردانی بکاپ، تمام کانفیگ‌ها و ساب‌های فعلی را جایگزین می‌کند. ادامه می‌دهید؟')){input.value='';return}
  st.innerHTML='<i class="ti ti-loader-2 ti-spin"></i> در حال بازگردانی...';st.style.color='var(--t3)';
  try{
    const text=await file.text();
    const data=JSON.parse(text);
    const r=await authF('/api/restore',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
    const d=await r.json();if(!r.ok)throw Error(d.detail||'خطا در بازگردانی');
    st.textContent='✓ '+d.links+' کانفیگ و '+d.subs+' ساب بازگردانی شد';st.style.color='var(--green-t)';
    toast('بکاپ بازگردانی شد ✓','ok');
    setTimeout(()=>location.reload(),1500);
  }catch(e){st.textContent=e.message;st.style.color='var(--red-t)'}
  input.value='';
}


async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts={}){
  const r=await fetch(url,opts);
  if(r.status===401){location.href='/login';throw new Error('unauthorized')}
  return r;
}
async function downloadBackup(){
  try{
    const r=await authF('/api/backup');
    if(!r.ok)throw new Error('backup failed');
    const blob=await r.blob(), a=document.createElement('a');
    a.href=URL.createObjectURL(blob);a.download='finevpn-v2ray-backup.json';a.click();URL.revokeObjectURL(a.href);
    toast('فایل پشتیبان دانلود شد','ok');
  }catch(e){toast('دانلود پشتیبان ناموفق بود','err')}
}
async function exportActiveLinks(){
  try{
    const r=await authF('/api/links/export'), d=await r.json();
    const blob=new Blob([(d.links||[]).join('\\n')+'\\n'],{type:'text/plain;charset=utf-8'}), a=document.createElement('a');
    a.href=URL.createObjectURL(blob);a.download='finevpn-v2ray-active-links.txt';a.click();URL.revokeObjectURL(a.href);
    toast(`${d.count||0} لینک export شد`,'ok');
  }catch(e){toast('Export لینک‌ها ناموفق بود','err')}
}
function setQuota(val,unit,el){
  document.getElementById('nl-val').value = val===0?'':val;
  document.getElementById('nl-unit').value = unit;
  document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setExpiry(days,el){
  document.getElementById('nl-exp').value = days===0?'':days;
  document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function selectProto(val,el){
  document.getElementById('nl-proto').value = val;
  document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setIpLimit(n,el){
  document.getElementById('nl-iplimit').value = n;
  document.querySelectorAll('#iplimit-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setSpeedLimit(n,el){
  document.getElementById('nl-speed').value = n;
  document.getElementById('nl-speed-unit').value = 'MBIT';
  document.querySelectorAll('#speed-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function onAlpnPresetChange(){
  const p=document.getElementById('nl-alpn-preset').value;
  const inp=document.getElementById('nl-alpn');
  if(p==='__custom__'){inp.style.display='block';inp.value='';inp.focus();}
  else{inp.style.display='none';inp.value=p;}
}
const sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);
function navTo(name){
  document.querySelectorAll('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));
  document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));
  const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity,categories:loadCats,settings:()=>{loadSetServer();loadSessions();loadTelemetry();startTelemetry();},appearance:loadCustomAppearance,testws:null};
  if(loaders[name])loaders[name]();
  closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}
let prevTraf=0,ch1,ch2,ch3;
async function fetchStats(){
  try{
    const r=await authF('/stats'),d=await r.json();
    document.getElementById('m-conns').textContent=d.active_connections;
    document.getElementById('conns-nb').textContent=d.active_connections;
    document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    document.getElementById('m-alinks').textContent=d.active_links??'—';
    document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';
    document.getElementById('m-subs').textContent=d.subs_count??'—';
    document.getElementById('errs-badge').textContent=d.total_errors+' خطا';
    document.getElementById('uptime-inline').textContent=d.uptime;
    if(d.volume){const vb=document.getElementById('vol-badge');
      if(vb){const ok=d.volume.mounted&&d.volume.writable;
        vb.className='badge '+(ok?'b-ok':'b-warn');
        vb.innerHTML='<i class="ti ti-'+(ok?'database-check':'alert-triangle')+'"></i> '+(ok?'ولوم دائمی':'ذخیره موقت');
        vb.title=ok?('دیسک دائمی: '+d.volume.data_dir+' · '+d.volume.free_mb+' مگابایت آزاد'):'هیچ Volume پایداری شناسایی نشد؛ یک Volume به سرویس متصل کنید و Mount Path را /data قرار دهید.';
      }}
    document.getElementById('uptime-badge').textContent='سرور · '+d.uptime;
    document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' اتصال';
    document.getElementById('t-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    const delta=d.total_traffic_mb-prevTraf,pct=Math.min(100,Math.round((delta/50)*100));
    document.getElementById('bw-pct').textContent=pct+'%';
    document.getElementById('bw-bar').style.width=pct+'%';
    prevTraf=d.total_traffic_mb;
    if(d.hourly){
      if(!ch1||!ch3)initCharts();
      const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));
      [ch1,ch3].forEach(c=>{if(!c||!c.data)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});
      if(vals.length){const avg=vals.reduce((a,b)=>a+b,0)/vals.length,peak=Math.max(...vals);document.getElementById('t-avg').innerHTML=avg.toFixed(2)+'<span class="m-unit">MB</span>';document.getElementById('t-peak').innerHTML=peak.toFixed(2)+'<span class="m-unit">MB</span>';}
    }
    renderErrs(d.recent_errors||[]);
  }catch(e){console.error(e)}
}
function renderErrs(errs){
  const el=document.getElementById('errs-full');if(!el)return;
  if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> هیچ خطایی نیست</div>';return}
  el.innerHTML=errs.slice().reverse().map(e=>`<div class="erow"><div class="etime"><i class="ti ti-clock"></i>${new Date(e.time).toLocaleString('fa-IR')}</div><div class="emsg">${esc(e.error)}${e.url?' — '+esc(e.url):''}</div></div>`).join('');
}
let actLogPoll=null;
async function loadActivity(){
  try{
    const [ar,sr,cr]=await Promise.all([authF('/api/activity'),authF('/api/subs'),authF('/api/connections')]);
    const {logs=[]}=await ar.json();
    const {subs=[]}=await sr.json();
    const cd=await cr.json();
    const conns=cd.connections||[];

    // --- sub cards ---
    const subsBox=document.getElementById('act-subs');
    subsBox.innerHTML=subs.length?subs.map(s=>{
      const limitFmt=s.total_limit_bytes?fmtB(s.total_limit_bytes):'نامحدود';
      const usedPct=s.total_limit_bytes?Math.min(100,Math.round((s.total_used_bytes/s.total_limit_bytes)*100)):0;
      const age=Date.now()-new Date(s.created_at).getTime();
      const ageTxt=age<60000?'همین الان':age<3600000?Math.floor(age/60000)+' دقیقه پیش':age<86400000?Math.floor(age/3600000)+' ساعت پیش':Math.floor(age/86400000)+' روز پیش';
      const ipLimits=(s.link_ids||[]).map(lid=>{const L=(allLinksList||[]).find(x=>x.uuid===lid);return L?L.ip_limit:0});
      const ipMax=ipLimits.length?Math.max(...ipLimits):0;
      const subConns=conns.filter(c=>(s.link_ids||[]).some(lid=>(c.labels||[]).includes(labelOf(lid))));
      return `<div class="card sub-exp-card" style="padding:16px" onclick="toggleSubCard(this,'${esc(s.sub_id)}')">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
          <span class="m-ring" style="width:36px;height:36px;font-size:16px"><i class="ti ti-folder"></i></span>
          <div style="flex:1;min-width:0">
            <div style="font-size:14px;font-weight:800;color:var(--t1)">${esc(s.name)}</div>
            <div style="font-size:10.5px;color:var(--t3)"><i class="ti ti-clock"></i> ${ageTxt}</div>
          </div>
          <label class="switch" style="position:relative;display:inline-block;width:38px;height:21px;cursor:pointer" title="روشن/خاموش">
            <input type="checkbox" ${s.active_count>0?'checked':''} onchange="toggleSub('${esc(s.sub_id)}',this.checked)" style="opacity:0;width:0;height:0">
            <span class="slider" style="position:absolute;inset:0;background:rgba(255,255,255,.12);border-radius:20px;transition:.25s"></span>
          </label>
        </div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:12px">
          <div style="background:rgba(16,185,129,.06);border-radius:10px;padding:9px 6px;text-align:center">
            <div style="font-size:14px;font-weight:800;color:var(--green-t)">${esc(s.total_used_fmt||'0 B')}</div>
            <div style="font-size:9.5px;color:var(--t3)">مصرف</div>
          </div>
          <div style="background:rgba(16,185,129,.06);border-radius:10px;padding:9px 6px;text-align:center">
            <div style="font-size:14px;font-weight:800;color:var(--t1)">${toFa(s.links_count)}</div>
            <div style="font-size:9.5px;color:var(--t3)">کانفیگ</div>
          </div>
          <div style="background:rgba(16,185,129,.06);border-radius:10px;padding:9px 6px;text-align:center">
            <div style="font-size:14px;font-weight:800;color:var(--t1)">${ipMax?toFa(ipMax):'∞'}</div>
            <div style="font-size:9.5px;color:var(--t3)">سقف IP</div>
          </div>
        </div>
        <div style="font-size:10px;color:var(--t3);display:flex;justify-content:space-between;margin-bottom:5px">
          <span>حجم مشترک: ${limitFmt}</span><span>${usedPct}%</span>
        </div>
        <div class="spbar" style="width:100%;height:7px"><div class="spfill" style="width:${usedPct}%"></div></div>
        <div class="sub-exp-hint"><i class="ti ti-chevron-down"></i> برای جزئیات کلیک کنید</div>
        <div class="sub-exp-body" id="sub-body-${esc(s.sub_id)}"></div>
      </div>`;
    }).join(''):'<div class="empty"><i class="ti ti-folders"></i><p>هنوز سابی وجود ندارد</p></div>';

    // --- live connections ---
    const cb=document.getElementById('act-conns-badge');
    cb.textContent=toFa(cd.count||0)+' اتصال';
    const cBox=document.getElementById('act-conns'),cEm=document.getElementById('act-conns-empty');
    if(!conns.length){cBox.innerHTML='';cEm.style.display='block'}
    else{
      cEm.style.display='none';
      cBox.innerHTML=conns.map(c=>`
        <div style="display:flex;align-items:center;gap:10px;padding:10px 4px;border-bottom:1px solid var(--card-b);direction:ltr">
          <span class="dot dg pulse"></span>
          <span style="font-weight:700;color:var(--t1);font-size:12px">${esc(c.ip)}</span>
          <span style="font-size:11px;color:var(--t3)">→</span>
          <span style="font-size:11.5px;color:var(--t2);flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(c.label||'نامشخص')}</span>
          ${c.dest?`<span style="font-size:11px;color:var(--green-t)">⇢ ${esc(c.dest)}</span>`:''}
          <span style="font-size:10px;color:var(--purple-t);background:var(--purple-bg);padding:2px 7px;border-radius:6px;white-space:nowrap">${esc(c.device||'')}</span>
          <span style="font-size:10.5px;color:var(--t3);white-space:nowrap">${esc(c.bytes_fmt||'0 B')}</span>
        </div>`).join('');
    }

    // --- full log ---
    const q=(document.getElementById('log-search')||{value:''}).value.trim().toLowerCase();
    const f=(document.getElementById('log-kind')||{value:''}).value;
    const filtered=logs.filter(l=>{
      if(f&&l.kind!==f)return false;
      if(q&&!(l.message||'').toLowerCase().includes(q)&&!new Date(l.time).toLocaleString('fa-IR').includes(q))return false;
      return true;
    });
    const sorted=filtered.slice().reverse();
    const el=document.getElementById('logs-list'),em=document.getElementById('logs-empty');
    if(!sorted.length){el.innerHTML='';em.style.display='block'}
    else{
      em.style.display='none';
      const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
      const kindFa={link:'کانفیگ',sub:'گروه',auth:'ورود',connection:'اتصال',system:'سیستم'};
      el.innerHTML=sorted.map(l=>`
        <div class="log-item">
          <div class="log-ic ${l.level}"><i class="ti ${icMap[l.level]||'ti-info-circle'}"></i></div>
          <div class="log-body">
            <div class="log-msg">${esc(l.message)}</div>
            <div class="log-time"><i class="ti ti-clock"></i> ${new Date(l.time).toLocaleString('fa-IR')} <span class="log-kind">${kindFa[l.kind]||l.kind}</span></div>
          </div>
        </div>
      `).join('');
    }
  }catch(e){console.error(e)}
  if(!actLogPoll){actLogPoll=setInterval(()=>{
    if(document.getElementById('pg-logs').classList.contains('on')){
      // ═══ وقتی کارت جزئیات ساب باز است، re-render نکنید تا کارت بسته نشود ═══
      if(document.querySelector('.sub-exp-card.open')) return;
      loadActivity();
    }
  },5000)}
}
function labelOf(uuid){const L=(allLinksList||[]).find(x=>x.uuid===uuid);return L?L.label:''}
// ══════ کارت ساب: باز/بسته کردن + بارگذاری جزئیات ══════
let subDetailCache={};
async function toggleSubCard(el,subId){
  const body=document.getElementById('sub-body-'+subId);
  if(!body) return;
  const isOpen=el.classList.contains('open');
  if(isOpen){ el.classList.remove('open'); return; }
  el.classList.add('open');
  body.innerHTML='<div style="text-align:center;padding:14px;color:var(--t3);font-size:11px"><i class="ti ti-loader ti-spin"></i> در حال بارگذاری...</div>';
  try{
    const [ar,cr]=await Promise.all([authF('/api/activity'),authF('/api/connections')]);
    const {logs=[]}=await ar.json();
    const cd=await cr.json();
    const conns=cd.connections||[];
    // connections touching this sub (by label match)
    const sr=await authF('/api/subs'); const {subs=[]}=await sr.json();
    const s=subs.find(x=>x.sub_id===subId)||{};
    // ═══ allLinksList فقط بعد از ورود به صفحه links پر می‌شود؛ اینجا مستقل می‌گیریم ═══
    if(!allLinksList.length){
      try{const lr=await authF('/api/links'); const {links=[]}=await lr.json(); if(links.length) allLinksList=links;}catch(e){}
    }
    const myLabels=(s.link_ids||[]).map(labelOf).filter(Boolean);
    const myConns=conns.filter(c=>(c.labels||[]).some(l=>myLabels.includes(l)));
    // per-sub log: mentions any of my labels OR sub creation
    const myLogs=logs.filter(l=>l.message&&myLabels.some(lb=>l.message.includes(lb)));
    const subLogs=logs.filter(l=>l.sub_id===subId);
    const allLogs=[...myLogs,...subLogs].slice(-40).reverse();
    let h='';
    h+='<div class="sub-sec-label"><i class="ti ti-users"></i> آی‌پی‌های متصل ('+toFa(myConns.length)+')</div>';
    if(!myConns.length){h+='<div style="font-size:11px;color:var(--t3);padding:6px 2px">الان اتصال فعالی برای این ساب وجود ندارد</div>'}
    else{
      myConns.forEach(c=>{
        const cdev=c.device||'نامشخص';
        const cua=c.ua||c.user_agent||'';
        const uaShort=cua?cua.split(' ').slice(0,3).join(' '):'';
        h+='<div class="sub-ip-row" style="display:block;padding:9px 10px;border:1px solid var(--card-b);border-radius:10px;margin-bottom:6px">'
          +'<div style="display:flex;align-items:center;gap:8px;direction:ltr"><span class="dot dg pulse"></span><span class="sub-ip-addr">'+esc(c.ip)+'</span>'
          +'<span style="font-size:10px;color:var(--purple-t);background:var(--purple-bg);padding:2px 7px;border-radius:6px;white-space:nowrap"><i class="ti ti-device-mobile"></i> '+esc(cdev)+'</span>'
          +'<span style="font-size:10px;color:var(--t3);margin-right:auto;white-space:nowrap">'+esc(c.bytes_fmt||'0 B')+'</span></div>'
          +'<div style="display:flex;gap:8px;margin-top:5px;font-size:10px;color:var(--t2);direction:ltr;flex-wrap:wrap">'
          +'<span><i class="ti ti-router"></i> '+esc((c.labels||[]).filter(l=>myLabels.includes(l)).join(' · ')||'—')+'</span>'
          +(c.dest?'<span style="color:var(--green-t)"><i class="ti ti-world"></i> '+esc(c.dest)+'</span>':'')
          +(uaShort?'<span style="color:var(--t3);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:160px" title="'+esc(cua)+'"><i class="ti ti-code"></i> '+esc(uaShort)+'</span>':'')
          +'</div></div>';
      });
    }
    // per-config usage breakdown
    let perCfg=[];
    try{const lr=await authF('/api/links');const {links:allLinks=[]}=await lr.json();
      perCfg=(allLinks||[]).filter(l=>(s.link_ids||[]).includes(l.uuid)).map(l=>({label:l.label,used:l.used_bytes||0,active:l.active})).sort((a,b)=>b.used-a.used);
    }catch(e){}
    if(perCfg.length){
      h+='<div class="sub-sec-label"><i class="ti ti-chart-bar"></i> مصرف به تفکیک کانفیگ</div>';
      h+='<div class="sub-cfg-list">';
      const maxUsed=Math.max(1,...perCfg.map(x=>x.used));
      perCfg.forEach(x=>{
        h+='<div class="sub-cfg-row"><div style="display:flex;justify-content:space-between;font-size:10.5px;margin-bottom:3px"><span style="color:var(--t2);font-weight:600">'+esc(x.label)+(x.active?'':' <span style="color:var(--red-t)">⚫</span>')+'</span><span style="color:var(--t3)">'+fmtB(x.used)+'</span></div><div class="spbar" style="height:5px"><div class="spfill" style="width:'+Math.round(x.used/maxUsed*100)+'%"></div></div></div>';
      });
      h+='</div>';
    }
    h+='<div class="sub-sec-label"><i class="ti ti-history"></i> لاگ کامل این ساب ('+toFa(allLogs.length)+')</div>';
    if(!allLogs.length){h+='<div style="font-size:11px;color:var(--t3);padding:6px 2px">هنوز رویدادی ثبت نشده</div>'}
    else{
      h+='<div class="sub-log-list">';
      const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
      allLogs.forEach(l=>{
        h+='<div class="sub-log-item"><div class="sub-log-ic '+(l.level||'info')+'"><i class="ti '+(icMap[l.level]||'ti-info-circle')+'"></i></div><div class="sub-log-msg">'+esc(l.message)+'</div><div class="sub-log-time">'+new Date(l.time).toLocaleTimeString('fa-IR')+'</div></div>';
      });
      h+='</div>';
    }
    body.innerHTML=h;
    // ═══ کلیک داخل جزئیات کارت رو بلاک میکنیم تا کارت بسته نشه ═══
    body.querySelectorAll('.sub-ip-row,.sub-cfg-list,.sub-log-list,.sub-sec-label').forEach(r=>r.addEventListener('click',e=>e.stopPropagation()));
  }catch(e){console.error(e);body.innerHTML='<div style="font-size:11px;color:var(--red-t)">خطا در بارگذاری</div>'}
}

async function toggleSub(subId,on){
  try{
    const r=await authF('/api/subs/'+subId),s=await r.json();
    for(const lid of (s.link_ids||[])){
      await authF('/api/links/'+lid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:on})});
    }
    toast(on?'ساب روشن شد ✓':'ساب خاموش شد','ok');
  }catch(e){toast('خطا در تغییر وضعیت','err')}
}
let allSubsList=[],allLinksList=[];
async function loadLinks(){
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    let {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    allSubsList=subs;allLinksList=links;
    const nlSub=document.getElementById('nl-sub');
    nlSub.innerHTML='<option value="">— بدون گروه —</option>'+subs.map(s=>`<option value="${esc(s.sub_id)}">${esc(s.name)}</option>`).join('');
    const nlCat=document.getElementById('nl-cat');
    const cf=document.getElementById('cat-filter'), curCat=cf?cf.value:'';
    const cats=(await (await authF('/api/categories')).json()).categories||[];
    window._cats=Array.isArray(cats)?cats:[];
    if(nlCat)nlCat.innerHTML='<option value="">— بدون دسته —</option>'+window._cats.map(c=>`<option value="${esc(c.id)}">${esc(c.name)}</option>`).join('');
    if(cf)cf.innerHTML='<option value="">همه دسته‌ها</option>'+window._cats.map(c=>`<option value="${esc(c.id)}">${esc(c.name)}</option>`).join('');
    if(cf&&curCat)cf.value=curCat;
    document.getElementById('links-nb').textContent=links.length;
    const lpc=document.getElementById('links-pg-cnt');if(lpc)lpc.textContent=toFa(links.length)+' کانفیگ';
    if(!links.length){const grid0=document.getElementById('links-grid');
      if(grid0)grid0.innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>';
      return}
    const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
    if(!grid)return;
    if(empty)empty.style.display='none';
    const cf2=document.getElementById('cat-filter');
    const fCat=cf2?cf2.value:'';
    if(fCat)links=links.filter(l=>String((l.category||{}).id||'0')===fCat);
    const subMap=Object.fromEntries(subs.map(s=>[s.sub_id,s.name]));
    grid.innerHTML=links.map(l=>{
  const catPill=(l.category&&l.category.name)?`<span class="cat-pill" style="background:${(l.category.color||'#10B981')}22;color:${l.category.color||'#10B981'}"><span class="cat-dot" style="background:${l.category.color||'#10B981'}"></span>${esc(l.category.name)}</span>`:'';
  const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
  const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
  const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
  const allowed=l.active&&!l.expired;
  const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
  return `<div class="cfg-card ${cardCls}" data-link-id="${esc(l.uuid)}">
    <div class="cfg-row">
      <label class="bulk-config-select" title="انتخاب کانفیگ" style="display:flex;align-items:center;padding-inline:5px"><input class="bulk-config-check" type="checkbox" value="${esc(l.uuid)}" onchange="updateBulkSelection()" aria-label="انتخاب کانفیگ"></label>
      <span class="cfg-status-dot ${allowed?'pulse':''}"></span>
      <div class="cfg-identity">
        <div class="cfg-label">${esc(l.label)}${catPill}</div>
        <div class="cfg-sub-meta">
          <span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID کپی شد','ok'))" title="${l.uuid}"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>
          <span>${new Date(l.created_at).toLocaleDateString('fa-IR')}</span>
        </div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-usage-col">
        <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
        <div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>از ${lim}</span></div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-exp-col">${expChip(l.expires_at,l.expired)}</div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-badges-col">
        ${protoBadge(l.protocol)}
        <span class="cfg-sub-tag" title="پورت اتصال"><i class="ti ti-route"></i> :${l.port||443}</span>
        <span class="cfg-sub-tag" title="Fingerprint"><i class="ti ti-fingerprint"></i> ${esc(l.fingerprint||'chrome')}</span>
        <span class="cfg-sub-tag" title="آی‌پی‌های متصل / محدودیت"><i class="ti ti-users"></i> ${l.connected_ips||0}${l.ip_limit?('/'+l.ip_limit):' (∞)'}</span>
        <span class="cfg-sub-tag" title="محدودیت سرعت"><i class="ti ti-gauge"></i> ${l.speed_limit_bytes?((l.speed_limit_bytes*8/1024/1024).toFixed(1)+' Mbps'):'نامحدود'}</span>
        ${l.sub_id&&allSubsList.find(s=>s.sub_id===l.sub_id)?`<span class="cfg-sub-tag"><i class="ti ti-folder"></i> ${esc(allSubsList.find(s=>s.sub_id===l.sub_id).name)}</span>`:''}
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-actions">
        <button class="tog${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})" title="فعال/غیرفعال"></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی لینک"><i class="ti ti-copy"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('Sub کپی شد','ok'))" title="Sub URL"><i class="ti ti-rss"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink('${l.uuid}')" title="ویرایش"><i class="ti ti-edit"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="resetUsage('${l.uuid}')" title="ریست مصرف"><i class="ti ti-rotate"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')" title="حذف"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  </div>`;
}).join('');
  }catch(e){console.error(e)}
}
function selectedConfigIds(){return Array.from(document.querySelectorAll('.bulk-config-check:checked')).map(el=>el.value)}
function selectAllConfigs(checked){document.querySelectorAll('.bulk-config-check').forEach(el=>el.checked=!!checked);updateBulkSelection()}
function updateBulkSelection(){const ids=selectedConfigIds();const count=document.getElementById('bulk-selected-count');if(count)count.textContent=toFa(ids.length)+' انتخاب';const all=document.getElementById('bulk-select-all');if(all){const checks=Array.from(document.querySelectorAll('.bulk-config-check'));all.checked=checks.length>0&&checks.every(x=>x.checked);all.indeterminate=checks.some(x=>x.checked)&&!all.checked;}}
async function bulkConfigAction(action){
  const ids=selectedConfigIds();if(!ids.length){toast('ابتدا کانفیگ‌ها را انتخاب کنید','err');return}
  const labels={activate:'فعال‌کردن',deactivate:'غیرفعال‌کردن',reset_usage:'صفرکردن مصرف',delete:'حذف'};
  const warning=action==='delete'?'این '+ids.length+' کانفیگ برای همیشه حذف می‌شوند. ادامه می‌دهید؟':labels[action]+' برای '+ids.length+' کانفیگ اجرا شود؟';
  if(!confirm(warning))return;
  try{const r=await authF('/api/links/bulk',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({action,ids})});const d=await r.json();if(!r.ok)throw new Error(d.detail||'operation failed');toast(toFa(d.changed||0)+' مورد انجام شد ✓','ok');await loadLinks();}catch(e){toast('عملیات گروهی ناموفق بود: '+(e.message||''),'err')}
}

async function createLink(){
  const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';
  const val=document.getElementById('nl-val').value;
  const unit=document.getElementById('nl-unit').value;
  const exp=document.getElementById('nl-exp').value;
  const note=document.getElementById('nl-note').value.trim();
  const sub_id=document.getElementById('nl-sub').value||null;
  const protocol=document.getElementById('nl-proto').value||'vless-ws';
  const fingerprint=document.getElementById('nl-fp').value||'chrome';
  const alpn=document.getElementById('nl-alpn').value.trim();
  const port=Number(document.getElementById('nl-port').value)||443;
  const ip_limit=Number(document.getElementById('nl-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('nl-speed').value)||0;
  const speed_limit_unit=document.getElementById('nl-speed-unit').value;
  try{
    const category_id=document.getElementById('nl-cat')?document.getElementById('nl-cat').value||null:null;
    const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,category_id,protocol,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit})});
    if(!r.ok)throw new Error('failed');
    ['nl-label','nl-val','nl-exp','nl-note','nl-alpn'].forEach(id=>document.getElementById(id).value='');
    document.getElementById('nl-port').value='443';
    document.getElementById('nl-iplimit').value='0';
    document.getElementById('nl-speed').value='0';
    document.getElementById('nl-alpn-preset').value='';
    document.getElementById('nl-alpn').style.display='none';
    toast('کانفیگ ساخته شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ساخت','err')}
}
function openEditLink(uuid){
  const l=allLinksList.find(x=>x.uuid===uuid);
  if(!l)return;
  document.getElementById('el-uuid').value=uuid;
  document.getElementById('el-label').value=l.label;
  document.getElementById('el-note').value=l.note||'';
  if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}
  else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB';}
  document.getElementById('el-exp').value='';
  document.getElementById('el-fp').value=l.fingerprint||'chrome';
  document.getElementById('el-alpn').value=l.alpn||'';
  document.getElementById('el-port').value=l.port||443;
  document.getElementById('el-iplimit').value=l.ip_limit||0;
  if(!l.speed_limit_bytes){document.getElementById('el-speed').value='0';document.getElementById('el-speed-unit').value='MBIT';}
  else{document.getElementById('el-speed').value=(l.speed_limit_bytes*8/1024/1024).toFixed(2);document.getElementById('el-speed-unit').value='MBIT';}
  openModal('modal-edit-link');
}
async function saveEditLink(){
  const uuid=document.getElementById('el-uuid').value;
  const label=document.getElementById('el-label').value.trim();
  const note=document.getElementById('el-note').value.trim();
  const val=document.getElementById('el-val').value;
  const unit=document.getElementById('el-unit').value;
  const exp=document.getElementById('el-exp').value;
  const fingerprint=document.getElementById('el-fp').value||'chrome';
  const alpn=document.getElementById('el-alpn').value.trim();
  const port=Number(document.getElementById('el-port').value)||443;
  const ip_limit=Number(document.getElementById('el-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('el-speed').value)||0;
  const speed_limit_unit=document.getElementById('el-speed-unit').value;
  const body={label,note,limit_value:val||0,limit_unit:unit,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit};
  if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{
    const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    closeModal('modal-edit-link');
    toast('کانفیگ ویرایش شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ویرایش','err')}
}
async function toggleActive(uuid,newState){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد ✓':'غیرفعال شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function resetUsage(uuid){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('مصرف ریست شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function deleteLink(uuid){
  if(!confirm('حذف این کانفیگ؟'))return;
  try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
function showQR(link){document.getElementById('qr-img').src='/api/qr?data='+encodeURIComponent(link);document.getElementById('qr-modal').classList.add('open')}
let allSubsRaw=[];
async function loadSubs(){
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    allSubsRaw=subs;
    document.getElementById('subs-nb').textContent=subs.length;
    document.getElementById('subs-pg-cnt').textContent=toFa(subs.length)+' گروه';
    renderSubsGrid(subs);
  }catch(e){console.error(e)}
}
function renderSubsGrid(subs){
  const grid=document.getElementById('subs-grid');
  if(!subs.length){
    grid.innerHTML='<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>';
    return;
  }
  grid.innerHTML=subs.map(s=>`
    <div class="sub-card">
      <div class="sub-card-top">
        <div class="sub-card-head-v2">
          <div class="sub-card-icon"><i class="ti ti-folder"></i></div>
          <div class="sub-card-titles">
            <div class="sub-card-name-v2">${esc(s.name)}</div>
            ${s.desc?`<div class="sub-card-desc-v2">${esc(s.desc)}</div>`:'<div class="sub-card-desc-v2" style="opacity:.5">بدون توضیحات</div>'}
          </div>
          <div class="sub-card-lock-badge ${s.has_password?'locked':'open'}" title="${s.has_password?'رمزدار':'پابلیک'}">
            <i class="ti ${s.has_password?'ti-lock':'ti-lock-open'}"></i>
          </div>
        </div>
        <div class="sub-card-stats">
          <div class="sub-card-stat"><div class="sub-card-stat-val">${toFa(s.links_count)}</div><div class="sub-card-stat-label">کانفیگ</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">${toFa(s.active_count)}</div><div class="sub-card-stat-label">فعال</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">${esc(s.total_used_fmt)}</div><div class="sub-card-stat-label">مصرف</div></div>
        </div>
      </div>
      <div class="sub-card-url-row">
        <span class="sub-card-url-text" title="صفحه پابلیک">${esc(s.public_url)}</span>
        <button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('لینک پابلیک کپی شد','ok'))" title="کپی پابلیک"><i class="ti ti-copy"></i></button>
        <button class="sub-card-url-copy" onclick="window.open('${esc(s.public_url)}','_blank')" title="باز کردن"><i class="ti ti-external-link"></i></button>
      </div>
      <div class="sub-card-url-row" style="margin-top:6px">
        <span class="sub-card-url-text" style="color:var(--purple-t)" title="لینک ساب (base64)">${esc(s.sub_url)}</span>
        <button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('لینک ساب کپی شد','ok'))" title="کپی ساب"><i class="ti ti-rss"></i></button>
        <button class="sub-card-url-copy" onclick="showQR('${esc(s.sub_url)}')" title="QR ساب"><i class="ti ti-qrcode"></i></button>
      </div>
      <div class="sub-card-bottom">
        <button class="btn btn-sm btn-g" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-link-plus"></i> کانفیگ‌ها</button>
        <button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('لینک ساب کپی شد','ok'))"><i class="ti ti-rss"></i> ساب</button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(s.sub_url)}')" title="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteSub('${esc(s.sub_id)}')" title="حذف"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  `).join('');
}
function filterSubs(q){
  q=q.trim().toLowerCase();
  if(!q){renderSubsGrid(allSubsRaw);return}
  renderSubsGrid(allSubsRaw.filter(s=>s.name.toLowerCase().includes(q)||(s.desc||'').toLowerCase().includes(q)));
}
async function createSub(){
  const name=document.getElementById('ns-name').value.trim()||'گروه جدید';
  const desc=document.getElementById('ns-desc').value.trim();
  const pw=document.getElementById('ns-pw').value;
  try{
    const r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc,password:pw})});
    if(!r.ok)throw new Error('failed');
    ['ns-name','ns-desc','ns-pw'].forEach(id=>document.getElementById(id).value='');
    closeModal('modal-create-sub');
    toast('گروه ساخته شد ✓','ok');loadSubs();
  }catch(e){toast('خطا در ساخت گروه','err')}
}

function qsUpdatePreview(){
  const el=document.getElementById('qs-preview');if(!el)return;
  const vol=parseFloat(document.getElementById('ns-vol').value)||0;
  const days=parseInt(document.getElementById('ns-days').value)||0;
  const ip=parseInt(document.getElementById('ns-iplimit').value)||0;
  const parts=[];
  parts.push(vol>0?('💡 حجم مشترک: <b>'+vol+' GB</b> بین ۲۴ کانفیگ = '+( (vol/24).toFixed(2) )+' GB هر کانفیگ'):'💡 حجم <b>نامحدود</b>');
  parts.push(days>0?('⏱ اعتبار: <b>'+days+' روز</b>'):'⏱ بدون انقضا');
  parts.push(ip>0?('📱 حداکثر <b>'+ip+' کاربر</b> هم‌زمان'):'📱 کاربر نامحدود');
  el.innerHTML=parts.join(' &nbsp;•&nbsp; ');
}
['ns-vol','ns-days','ns-iplimit'].forEach(id=>{
  const e=document.getElementById(id);if(e)e.addEventListener('input',qsUpdatePreview);
});

async function createSubQuick(){
  const name=document.getElementById('ns-name').value.trim()||'گروه سریع';
  const desc=document.getElementById('ns-desc').value.trim();
  const pw=document.getElementById('ns-pw').value;
  const vol=parseFloat(document.getElementById('ns-vol').value)||0;
  const days=parseInt(document.getElementById('ns-days').value)||0;
  const ipLimit=parseInt(document.getElementById('ns-iplimit').value)||0;
  const totalLimitBytes=vol>0?Math.round(vol*1024*1024*1024):0;
  const expiresAt=days>0?new Date(Date.now()+days*86400000).toISOString():null;
  if(!name){toast('نام گروه را وارد کنید','err');return;}
  if(vol<0||days<0||ipLimit<0){toast('مقادیر نمی‌توانند منفی باشند','err');return;}
  if(totalLimitBytes>0&&totalLimitBytes<1024*1024){toast('حجم مشترک حداقل ۱ مگابایت باید باشد','err');return;}
  
  const btn=document.querySelector('#modal-create-sub .btn-pur');
  btn.disabled=true; btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ساخت...';
  
  try{
    // 1. Create sub group
    const r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc,password:pw})});
    if(!r.ok)throw new Error('ساخت گروه شکست خورد');
    const sub=await r.json();
    const subId=sub.sub_id;
    
    // 2. Set shared bandwidth (retry on failure, verify)
    if(totalLimitBytes>0){
      let bwOk=false;
      for(let attempt=0;attempt<3&&!bwOk;attempt++){
        const br=await authF('/api/subs/'+subId+'/bandwidth',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({total_limit_bytes:totalLimitBytes})});
        bwOk=br.ok;
      }
      if(!bwOk)toast('هشدار: تنظیم حجم مشترک ناموفق بود','err');
      else{
        const chk=await authF('/api/subs/'+subId+'/bandwidth');
        if(chk.ok){const bd=await chk.json();
          if(bd.total_limit_bytes!==totalLimitBytes)toast('هشدار: حجم مشترک درست ثبت نشد','err');}
      }
    }
    
    // 3. Create 24 configs
    const protocols=["vless-ws","xhttp-packet-up","xhttp-stream-up"];
    const fps=["chrome","ios"];
    const alpns=["","h2","http/1.1","h2,http/1.1"];
    const abbr={"vless-ws":"VWS","xhttp-packet-up":"XPU","xhttp-stream-up":"XSU","chrome":"CH","ios":"IO","":"DEF","h2":"H2","http/1.1":"11","h2,http/1.1":"MIX"};
    
    let num=1, created=0;
    for(const proto of protocols){
      for(const fp of fps){
        for(const alpn of alpns){
          const label=abbr[proto]+'-'+abbr[fp]+'-'+abbr[alpn]+'-'+String(num).padStart(2,'0');
          const lr=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({
            label,protocol:proto,fingerprint:fp,alpn:alpn,port:443,
            limit_bytes:0,ip_limit:ipLimit,speed_limit_bytes:0,expires_days:days
          })});
          if(lr.ok){
            const link=await lr.json();
            await authF('/api/subs/'+subId+'/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_id:link.uuid,action:'add'})});
            created++;
          }
          num++;
        }
      }
    }
    
    closeModal('modal-create-sub');
    const sumTxt='✓ '+created+' کانفیگ ساخته شد'+(vol>0?(' | حجم مشترک: '+vol+' GB'):'')+(days>0?(' | '+days+' روز'):'');
    toast(sumTxt,'ok');
    setTimeout(()=>{ if(confirm('گروه ساخته شد. لینک سابسکریپشن کپی شود؟')){ loadSubs(); } },600);
    loadSubs();loadLinks();
  }catch(e){
      toast(e.message||'خطا در ساخت سریع','err');
    }finally{
      btn.disabled=false; btn.innerHTML='<i class="ti ti-magic-wand"></i> ساخت گروه + ۲۴ کانفیگ';
    }
}
async function deleteSub(sub_id){
  if(!confirm('این گروه و فقط کانفیگ‌های وابسته به همین گروه حذف می‌شوند. کانفیگ‌های گروه‌های دیگر باقی می‌مانند. ادامه می‌دهید؟'))return;
  try{const r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('گروه حذف شد ✓','ok');loadSubs();loadLinks();}catch(e){toast('خطا','err')}
}
let lmodalLinks=[],lmodalInSub=new Set();
async function openSubLinks(sub_id,name){
  currentSubId=sub_id;
  document.getElementById('modal-sub-name').textContent=name;
  document.getElementById('modal-links-body').innerHTML='<div style="color:var(--t3);font-size:12px;padding:20px;text-align:center"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite;font-size:20px"></i></div>';
  document.getElementById('lmodal-search-inp').value='';
  openModal('modal-links');
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    const thisSub=subs.find(s=>s.sub_id===sub_id);
    lmodalInSub=new Set(thisSub?.link_ids||[]);
    lmodalLinks=links;
    renderLmodalList(links);
  }catch(e){toast('خطا در بارگذاری','err')}
}
function renderLmodalList(links){
  const body=document.getElementById('modal-links-body');
  if(!links.length){body.innerHTML='<div class="empty" style="padding:30px"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>';updateLmodalCount();return}
  body.innerHTML=links.map(l=>{
    const checked=lmodalInSub.has(l.uuid);
    const on=l.active&&!l.expired;
    const vlink=l.vless_link||'';
    const surl=l.sub_url||'';
    return `<div class="lrow-v2 ${checked?'checked':''}" data-uuid="${l.uuid}" data-name="${esc(l.label).toLowerCase()}" onclick="toggleLrow('${l.uuid}',this)">
      <div class="lrow-v2-check"><i class="ti ti-check"></i></div>
      <div class="lrow-v2-avatar"><i class="ti ti-key"></i></div>
      <div class="lrow-v2-info">
        <div class="lrow-v2-name">${esc(l.label)}</div>
        <div class="lrow-v2-meta"><i class="ti ti-database" style="font-size:10px"></i> ${fmtB(l.used_bytes)}</div>
        <div class="lrow-links">
          <button class="lrow-link-btn" onclick="event.stopPropagation();navigator.clipboard.writeText('${esc(vlink)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی لینک VLESS"><i class="ti ti-copy"></i><span>لینک</span></button>
          <button class="lrow-link-btn" onclick="event.stopPropagation();navigator.clipboard.writeText('${esc(surl)}').then(()=>toast('ساب کپی شد','ok'))" title="کپی Sub URL"><i class="ti ti-rss"></i><span>ساب</span></button>
          <button class="lrow-link-btn" onclick="event.stopPropagation();showQR('${esc(vlink)}')" title="QR کد"><i class="ti ti-qrcode"></i><span>QR</span></button>
        </div>
      </div>
      <span class="lrow-v2-status ${on?'on':'off'}">${on?'فعال':'غیرفعال'}</span>
    </div>`;
  }).join('');
  updateLmodalCount();
}
function toggleLrow(uuid,el){
  if(lmodalInSub.has(uuid)){lmodalInSub.delete(uuid);el.classList.remove('checked')}
  else{lmodalInSub.add(uuid);el.classList.add('checked')}
  updateLmodalCount();
}
function lmodalSelectAll(state){
  lmodalLinks.forEach(l=>{if(state)lmodalInSub.add(l.uuid);else lmodalInSub.delete(l.uuid)});
  renderLmodalList(lmodalLinks);
}
function updateLmodalCount(){
  const el=document.getElementById('lmodal-count');
  if(el)el.textContent=toFa(lmodalInSub.size)+' انتخاب شده';
}
function filterLmodal(q){
  q=q.trim().toLowerCase();
  document.querySelectorAll('#modal-links-body .lrow-v2').forEach(row=>{
    row.style.display = !q || row.dataset.name.includes(q) ? '' : 'none';
  });
}
async function saveSubLinks(){
  if(!currentSubId)return;
  const link_ids=[...lmodalInSub];
  try{
    const r=await authF('/api/subs/'+currentSubId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_ids})});
    if(!r.ok)throw new Error();
    await Promise.all(lmodalLinks.map(l=>
      authF('/api/links/'+l.uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({sub_id:lmodalInSub.has(l.uuid)?currentSubId:null})})
    ));
    closeModal('modal-links');
    toast('کانفیگ‌های گروه ذخیره شدند ✓','ok');
    loadSubs();loadLinks();
  }catch(e){toast('خطا در ذخیره','err')}
}
async function loadSubsPage(){
  document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    const sbc=document.getElementById('sb-count');if(sbc)sbc.textContent=toFa(subs.length);
    const sbl=document.getElementById('sb-links');if(sbl)sbl.textContent=toFa(subs.reduce((a,s)=>a+(s.links_count||0),0));
    const el=document.getElementById('sub-groups-list');
    if(!subs.length){el.innerHTML='<div class="empty"><i class="ti ti-rss-off"></i><p>هنوز گروهی ندارید</p></div>';return}
    el.innerHTML=subs.map(s=>`
      <div style="padding:13px 15px;background:var(--accent-d);border:1px solid var(--card-b);border-radius:10px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">
        <div>
          <div style="font-weight:700;font-size:13px;margin-bottom:3px">${esc(s.name)}</div>
          <div style="font-family:ui-monospace,monospace;font-size:10px;color:#34D399">${esc(s.sub_url)}</div>
          <div style="font-size:10px;color:var(--t3);margin-top:3px">${toFa(s.links_count)} کانفیگ · ${esc(s.total_used_fmt)} مصرف ${s.has_password?'· 🔒 رمزدار':''}</div>
        </div>
        <div style="display:flex;gap:5px;flex-wrap:wrap">
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-copy"></i> ساب</button>
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-globe"></i> پابلیک</button>
          <button class="btn btn-sm btn-g" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button>
        </div>
      </div>
    `).join('');
  }catch(e){}
}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(()=>toast('کپی شد ✓','ok'))}
function parseBytesFmt(s){
  if(!s)return 0;
  const m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);
  if(!m)return 0;
  const n=parseFloat(m[1]),u=m[2].toUpperCase();
  const mult={B:1,KB:1024,MB:1024**2,GB:1024**3,TB:1024**4};
  return n*(mult[u]||1);
}
async function loadConns(){
  try{
    const r=await authF('/api/connections'),d=await r.json();
    const grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.count+' اتصال';
    document.getElementById('ch-count').textContent=toFa(d.count);
    const conns=d.connections||[];
    if(!d.count){
      grid.innerHTML='';ce.style.display='block';
      document.getElementById('ch-traffic').textContent='—';
      document.getElementById('ch-avgdur').textContent='—';
      document.getElementById('ch-uniq').textContent='—';
      return;
    }
    ce.style.display='none';
    const totalBytes=conns.reduce((s,c)=>s+parseBytesFmt(c.bytes_fmt),0);
    document.getElementById('ch-traffic').textContent=fmtB(totalBytes);
    const uniqIps=new Set(conns.map(c=>c.ip)).size;
    document.getElementById('ch-uniq').textContent=toFa(uniqIps);
    const durs=conns.map(c=>c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0);
    const avgSec=durs.length?Math.floor(durs.reduce((a,b)=>a+b,0)/durs.length):0;
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ث':avgSec<3600?Math.floor(avgSec/60)+' د':Math.floor(avgSec/3600)+' س';
    const maxDur=Math.max(...durs,1);
    grid.innerHTML=conns.map(c=>{
      const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      const dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';
      const durPct=Math.min(100,Math.round((secs/maxDur)*100));
      const protoVal=c.transport==='vless-ws'?'vless-ws':(c.transport||'').replace('xhttp-','xhttp-');
      return `<div class="conn-card-v2">
        <div class="conn-card-v2-glow"></div>
        <div class="conn-card-v2-top">
          <div class="conn-avatar"><i class="ti ti-device-desktop"></i></div>
          <div class="conn-card-v2-id">
            <div class="conn-ip-v2">${esc(c.ip)}
              <button class="conn-ip-copy" onclick="navigator.clipboard.writeText('${esc(c.ip)}').then(()=>toast('IP کپی شد','ok'))" title="کپی IP"><i class="ti ti-copy"></i></button>
            </div>
            <div class="conn-label-v2">${esc(c.label)}</div>
          </div>
          <span class="conn-status-pill"><span class="dot dg pulse"></span> زنده</span>
        </div>
        <div class="conn-card-v2-divider"></div>
        <div class="conn-card-v2-body">
          <div class="conn-proto-row">${protoBadge(protoVal)}</div>
          <div class="conn-stat-row">
            <div class="conn-stat-box">
              <div class="conn-stat-icon"><i class="ti ti-transfer"></i></div>
              <div>
                <div class="conn-stat-text-label">ترافیک</div>
                <div class="conn-stat-text-val">${esc(c.bytes_fmt)}</div>
              </div>
            </div>
            <div class="conn-stat-box">
              <div class="conn-stat-icon time"><i class="ti ti-clock"></i></div>
              <div>
                <div class="conn-stat-text-label">مدت اتصال</div>
                <div class="conn-stat-text-val">${dur}</div>
              </div>
            </div>
          </div>
          <div class="conn-duration-track"><div class="conn-duration-fill" style="width:${durPct}%"></div></div>
        </div>
      </div>`;
    }).join('');
  }catch(e){console.error(e)}
}
async function loadErrs(){try{const r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);
  const ec=document.getElementById('er-count');if(ec)ec.textContent=toFa(d.recent_errors?d.recent_errors.length:0);
  const el=document.getElementById('er-last'),elt=document.getElementById('er-last-time');
  if(d.recent_errors&&d.recent_errors.length){const e0=d.recent_errors[d.recent_errors.length-1];if(el)el.textContent=String(e0.message||e0).slice(0,40);if(elt)elt.textContent=new Date(e0.time||Date.now()).toLocaleString('fa-IR');}
  else{if(el)el.textContent='بدون خطا';if(elt)elt.textContent='سیستم پایدار'}
}catch(e){}}
async function loadSetServer(){
  try{
    const r=await authF('/stats'),d=await r.json();
    const el=document.getElementById('set-server');if(!el)return;
    const rows=[['نسخه پنل','FineVPN_v2ray v1.0.0'],['آپتایم',String(d.uptime||'—')],['اتصالات فعال',toFa(d.active_connections||0)],['کل کانفیگ‌ها',toFa(d.links_count||0)],['گروه‌های ساب',toFa(d.subs_count||0)],['کل ترافیک',(d.total_traffic_mb||0).toFixed(2)+' MB']];
    el.innerHTML='<div class="log-timeline">'+rows.map(k=>'<div class="log-item"><div class="log-ic info"><i class="ti ti-dot"></i></div><div class="log-body" style="display:flex;justify-content:space-between;align-items:center"><span class="log-msg">'+k[0]+'</span><b style="color:var(--t1);font-size:12px">'+k[1]+'</b></div></div>').join('')+'</div>';
    const up=document.getElementById('st-uptime');if(up)up.textContent=String(d.uptime||'—');
    try{const sr=await authF('/api/system'),sd=await sr.json();const hostEl=document.getElementById('server-public-host');if(hostEl)hostEl.textContent=sd.public_host||location.host||'—';}catch(hostErr){}
    // persistence panel (public /health — no auth needed, but reuse cookie)
    try{
      const hr=await authF('/health'),hv=await hr.json();
      const vel=document.getElementById('set-volume');
      if(vel&&hv&&hv.volume){
        const v=hv.volume, ok=v.mounted&&v.writable;
        if(ok){
          // volume active → hide this panel entirely
          const panel=vel.closest('.sec-panel'); if(panel) panel.style.display='none';
        }else{
          vel.innerHTML='<div class="vol-steps">'
            +'<div class="vol-step"><div class="vs-n"><i class="ti ti-alert-triangle" style="font-size:13px"></i></div><div><b>ولوم دائمی متصل نیست</b><div class="vs-s">داده‌ها روی فضای موقت هستند و ممکن است بعد از استقرار مجدد از بین بروند — کانفیگ‌ها، گروه‌ها و مصرف حجم مشترک.</div></div></div>'
            +'</div>'
            +'<div class="vol-note"><i class="ti ti-alert-triangle"></i> برای فعال‌سازی: در تنظیمات پلتفرم، یک Volume پایدار بسازید و به این سرویس متصل کنید<br>· <b>نام ولیم (Volume name):</b> <code dir="ltr">panel_data</code><br>· <b>Mount Path:</b> <code dir="ltr">/data</code><br>سپس سرویس را دوباره Deploy کنید و وضعیت ذخیره‌سازی را بررسی کنید.</div>';
        }
      }
    }catch(e2){}
  }catch(e){}
}


async function fetchDefaultVless(){
  try{const r=await authF('/api/links'),d=await r.json();const links=d.links||[];const def=links.find(l=>l.limit_bytes===0&&l.active&&!l.expired)||links.find(l=>l.active&&!l.expired)||links[0];document.getElementById('vless-main').textContent=def?def.vless_link:'هنوز کانفیگی وجود ندارد';}catch(e){}
}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('کپی شد ✓','ok'))}
function qrFor(id){showQR(document.getElementById(id).textContent)}
function refreshAll(){fetchStats();fetchDefaultVless();loadLinks();if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('رفرش شد','ok')}

function togglePwField(id,btn){
  const inp=document.getElementById(id);
  const icon=btn.querySelector('i');
  const toText=inp.type==='password';
  inp.type=toText?'text':'password';
  icon.className='ti '+(toText?'ti-eye-off':'ti-eye');
}

function makeGradient(ctx,color1,color2){
  const g=ctx.createLinearGradient(0,0,0,260);
  g.addColorStop(0,color1);g.addColorStop(1,color2);
  return g;
}
function initCharts(){
  if(typeof Chart==='undefined')return;
  const cv1=document.getElementById('ch1');if(!cv1)return;
  const c1=cv1.getContext('2d');
  const grad1=makeGradient(c1,'rgba(16,185,129,.38)','rgba(16,185,129,0)');
  const opts={
    responsive:true,maintainAspectRatio:false,
    interaction:{mode:'index',intersect:false},
    plugins:{
      legend:{display:false},
      tooltip:{
        backgroundColor:'rgba(13,27,46,.96)',borderColor:'rgba(16,185,129,.3)',borderWidth:1,
        titleColor:'#E8F4FF',bodyColor:'#7BAED4',padding:11,cornerRadius:10,displayColors:false,
        titleFont:{family:'Vazirmatn',size:11,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
        callbacks:{label:v=>`${v.parsed.y.toFixed(2)} مگابایت`}
      }
    },
    scales:{
      x:{grid:{display:false},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9,family:'Vazirmatn'}}},
      y:{grid:{color:'rgba(16,185,129,.06)'},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9,family:'Vazirmatn'},callback:v=>v+' MB'}}
    },
    elements:{line:{capBezierPoints:true}}
  };
  const ds1={label:'MB',data:[],borderColor:'#10B981',backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:'#10B981',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:2.5};
  ch1=new Chart(document.getElementById('ch1'),{type:'line',data:{labels:[],datasets:[ds1]},options:opts});

  function makeGradientV2(ctx,c1,c2,c3){
    const g=ctx.createLinearGradient(0,0,0,320);
    g.addColorStop(0,c1);g.addColorStop(.6,c2);g.addColorStop(1,c3);
    return g;
  }
  const c3ctx=document.getElementById('ch3').getContext('2d');
  const gradFill3=makeGradientV2(c3ctx,'rgba(16,185,129,.45)','rgba(16,185,129,.08)','rgba(16,185,129,0)');
  ch3=new Chart(document.getElementById('ch3'),{
    type:'line',
    data:{labels:[],datasets:[
      {label:'مصرف',data:[],borderColor:'#10B981',backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#10B981',pointHoverBorderWidth:3,borderWidth:3,order:2},
      {label:'میانگین',data:[],borderColor:'#F59E0B',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}
    ]},
    options:{
      responsive:true,maintainAspectRatio:false,
      interaction:{mode:'index',intersect:false},
      plugins:{
        legend:{display:false},
        tooltip:{
          backgroundColor:'rgba(13,27,46,.97)',borderColor:'rgba(16,185,129,.35)',borderWidth:1,
          titleColor:'#E8F4FF',bodyColor:'#9DC3E8',padding:13,cornerRadius:12,displayColors:true,boxPadding:4,
          titleFont:{family:'Vazirmatn',size:11.5,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
          callbacks:{label:v=>` ${v.dataset.label}: ${v.parsed.y.toFixed(2)} MB`}
        }
      },
      scales:{
        x:{grid:{display:false},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9.5,family:'Vazirmatn'},maxRotation:0}},
        y:{grid:{color:'rgba(16,185,129,.05)'},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9.5,family:'Vazirmatn'},callback:v=>v+' MB'}}
      }
    }
  });

  const cv2=document.getElementById('ch2');if(!cv2)return;
  ch2=new Chart(cv2,{
    type:'bar',
    data:{labels:['VLESS/WS','XHTTP Ultra','HTTP Proxy'],datasets:[{
      data:[55,35,10],
      backgroundColor:['#10B981','#34D399','#0D9488'],
      borderRadius:8,
      barThickness:26,
      maxBarThickness:34
    }]},
    options:{
      indexAxis:'y',
      responsive:true,maintainAspectRatio:false,
      plugins:{
        legend:{display:false},
        tooltip:{backgroundColor:'rgba(13,27,46,.96)',borderColor:'rgba(16,185,129,.3)',borderWidth:1,padding:10,cornerRadius:10,bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}
      }
    }
  });
}
let ws;
function wsLog(c,m){const l=document.getElementById('ws-log'),p=document.createElement('p');const colors={ok:'#34D399',err:'#F87171',info:'#7BAED4',sent:'#FCD34D'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('fa-IR')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('UUID را وارد کنید','err');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','اتصال: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok','✓ متصل - UUID معتبر');ws.onerror=()=>wsLog('err','✗ خطا - UUID نامعتبر یا غیرفعال');ws.onmessage=m=>wsLog('info','دریافت '+(m.data.size||m.data.length)+' byte');ws.onclose=e=>wsLog('err','قطع ('+e.code+')'+(e.code===1008?' - دسترسی رد شد':''))}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','ارسال: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(window.ws)window.ws.close()}
document.addEventListener('DOMContentLoaded',async()=>{
  await checkAuth();
  const sau=document.getElementById('sub-all-url');if(sau)sau.textContent=location.protocol+'//'+location.host+'/sub-all';
  loadSetServer();
  fetchStats();fetchDefaultVless();loadLinks();loadSubs();
  setInterval(fetchStats,4000);
  setInterval(()=>{
    if(document.getElementById('pg-links').classList.contains('on'))loadLinks();
    if(document.getElementById('pg-subgroups').classList.contains('on')&&!document.querySelector('.sub-exp-card.open'))loadSubs();
    if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();
    if(document.getElementById('pg-connections').classList.contains('on'))loadConns();
    if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();
  },5000);
});

async function quickSubCreate(){
  const btn = document.getElementById('qs-submit-btn');
  const resBox = document.getElementById('qs-result');
  const linkInp = document.getElementById('qs-pub-link');
  const name = document.getElementById('qs-name').value.trim() || 'ساب گروه جدید';
  // 0 = unlimited for all three
  const rawVol = document.getElementById('qs-vol').value.trim();
  const rawDays = document.getElementById('qs-days').value.trim();
  const rawIp = document.getElementById('qs-ip').value.trim();
  const volGb = rawVol === '' ? 0 : (parseFloat(rawVol) || 0);
  const days = rawDays === '' ? 0 : (parseInt(rawDays) || 0);
  const ipLimit = rawIp === '' ? 0 : (parseInt(rawIp) || 0);

  if (btn.dataset.busy === '1') { return; }
  btn.dataset.busy = '1';
  btn.disabled = true;
  btn.innerHTML = '<i class="ti ti-loader animate-spin"></i> در حال ساخت ۲۴ کانفیگ...';

  try {
    // 1. Create Sub Group
    const subRes = await authF('/api/subs', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({name: name})
    });
    const subData = await subRes.json();
    const subId = subData.sub_id;
    const pubUrl = subData.public_url || (location.protocol + '//' + location.host + '/p/' + subData.uuid_key);

    // 2. Set Shared Bandwidth
    if (volGb > 0) {
      await authF('/api/subs/' + subId + '/bandwidth', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({total_limit_bytes: Math.round(volGb * 1024 * 1024 * 1024)})
      });
    }

    // 3. Create 24 Configs Matrix — batch endpoint (fast), with sequential fallback
    let made = 0;
    try {
      const qc = await authF('/api/subs/' + subId + '/quick-create', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({days: days, ip_limit: ipLimit})
      });
      const qd = await qc.json();
      if (qc.ok && qd.count === 24) {
        made = 24;
      } else {
        throw new Error(qd.detail || 'batch incomplete');
      }
    } catch (batchErr) {
      // Fallback: sequential creation (slower, same result)
      const protos = ["vless-ws", "xhttp-packet-up", "xhttp-stream-up"];
      const fps = ["chrome", "ios"];
      const alpns = ["", "h2", "http/1.1", "h2,http/1.1"];
      const abbrP = {"vless-ws": "VWS", "xhttp-packet-up": "XPU", "xhttp-stream-up": "XHS"};
      const abbrF = {"chrome": "CH", "ios": "IO"};
      const abbrA = {"": "DEF", "h2": "H2", "http/1.1": "11", "h2,http/1.1": "MIX"};
      let count = 1;
      for (const p of protos) {
        for (const f of fps) {
          for (const a of alpns) {
            const lbl = abbrP[p] + '-' + abbrF[f] + '-' + abbrA[a] + '-' + String(count).padStart(2, '0');
            const lRes = await authF('/api/links', {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({label: lbl, protocol: p, fingerprint: f, alpn: a, port: 443, limit_bytes: 0, ip_limit: ipLimit, speed_limit_bytes: 0, expires_days: days, sub_id: subId})
            });
            const linkData = await lRes.json();
            await authF('/api/subs/' + subId + '/links', {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({link_id: linkData.uuid, action: 'add'})
            });
            count++; made++;
          }
        }
      }
    }
    if (made !== 24) { throw new Error('ساخت کانفیگ‌ها ناقص بود (' + made + '/24)'); }

    // Success UI
    btn.dataset.busy = '';
    btn.disabled = false;
    linkInp.value = pubUrl;
    resBox.style.display = 'block';
    toast('گروه ساب با ۲۴ کانفیگ ساخته شد', 'ok');
    refreshAll();
  } catch(err) {
    btn.dataset.busy = '';
    btn.disabled = false;
    toast('خطا در ساخت ساب: ' + err.message, 'err');
  } finally {
    btn.disabled = false;
    btn.innerHTML = '<i class="ti ti-plus"></i> ساخت گروه ساب + ۲۴ کانفیگ با حجم مشترک';
  }
}

</script>
</body></html>"""


def get_public_page_html(uuid_key: str) -> str:
    """صفحه پابلیک ساب v3 — طراحی حرفه‌ای‌تر: لینک کانفیگ پنهان با دکمه نمایش، صفحه‌ی رمز با طراحی ویژه"""
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>FineVPN_v2ray — سابسکریپشن</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{
  --bg:#070d0b;--bg2:#0b1613;--bg3:#0f1f1a;
  --card:#0d1c18;--card-b:rgba(16,185,129,0.14);--card-bh:rgba(16,185,129,0.32);
  --accent:#10B981;--accent2:#34D399;--accent-d:rgba(16,185,129,0.12);
  --green:#1FB87E;--green-bg:rgba(31,184,126,0.1);--green-t:#3FD79C;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.1);--red-t:#FB8585;
  --amber:#F2A33D;--amber-bg:rgba(242,163,61,0.1);--amber-t:#F9C988;
  --purple:#9D7BF0;--purple-bg:rgba(157,123,240,0.1);--purple-t:#BCA4F7;
  --t1:#EFF4FF;--t2:#8AA0C4;--t3:#48577A;
  --radius:18px;--shadow:0 12px 40px rgba(0,0,0,0.45);
  --serif:'Vazirmatn',sans-serif;
}}
[data-theme="light"]{{
  --bg:#F0FDF9;--bg2:#E1FBEF;--bg3:#D2F5E6;
  --card:#FFFFFF;--card-b:rgba(16,185,129,0.16);--card-bh:rgba(16,185,129,0.34);
  --accent:#059669;--accent2:#047857;--accent-d:rgba(5,150,105,0.10);
  --green:#0E9A6A;--green-bg:rgba(14,154,106,0.08);--green-t:#0A7553;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#A51E1E;
  --amber:#C97A12;--amber-bg:rgba(201,122,18,0.08);--amber-t:#8F5A0C;
  --purple:#7350D6;--purple-bg:rgba(115,80,214,0.08);--purple-t:#5A3CAD;
  --t1:#101A30;--t2:#48577A;--t3:#8694B0;
  --shadow:0 12px 36px rgba(20,40,90,0.12);
}}
html,body{{min-height:100%;overflow-x:hidden;background:var(--bg);font-family:var(--serif);color:var(--t1);font-size:14px;transition:background .35s,color .35s}}
.bg-fx{{position:fixed;inset:0;background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(16,185,129,0.14),transparent 62%),var(--bg);z-index:0;pointer-events:none;transition:background .35s}}
.grid-fx{{position:fixed;inset:0;background-image:linear-gradient(rgba(16,185,129,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(16,185,129,0.03) 1px,transparent 1px);background-size:46px 46px;z-index:0;pointer-events:none}}
.wrap{{position:relative;z-index:10;max-width:800px;margin:0 auto;padding:24px 16px 64px}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:26px;gap:10px}}
.brand{{display:flex;align-items:center;gap:11px;min-width:0}}
.brand-img{{width:40px;height:40px;border-radius:50%;overflow:hidden;border:1px solid var(--card-b);box-shadow:0 0 14px rgba(16,185,129,.35),0 0 8px rgba(16,185,129,.25);flex-shrink:0}}
.brand-img img{{width:100%;height:100%;object-fit:cover}}
.brand-name{{font-size:14.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em}}
.brand-sub{{font-size:9.5px;color:var(--t3);font-weight:500}}
.top-actions{{display:flex;align-items:center;gap:6px;flex-shrink:0}}
.icon-btn{{width:36px;height:36px;border-radius:11px;background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer;transition:.18s}}
.icon-btn:hover{{background:var(--accent-d);color:var(--accent2);border-color:var(--card-bh)}}

.sub-info{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px 24px 22px;margin-bottom:16px;box-shadow:var(--shadow);position:relative;overflow:hidden}}
.sub-info::before{{content:'';position:absolute;top:0;right:0;width:160px;height:160px;background:radial-gradient(circle at top right,rgba(59,124,246,.1),transparent 70%);pointer-events:none}}
.sub-eyebrow{{font-size:10px;font-weight:700;color:var(--accent2);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px;display:flex;align-items:center;gap:6px}}
.sub-eyebrow i{{font-size:13px}}
.sub-name{{font-size:23px;font-weight:800;color:var(--t1);margin-bottom:6px;letter-spacing:-.02em}}
.sub-desc{{font-size:12.5px;color:var(--t2);line-height:1.8;margin-bottom:14px}}
.sub-meta-row{{font-size:10.5px;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:6px}}
.sub-sub-box{{background:var(--accent-d);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;display:flex;align-items:center;gap:9px;flex-wrap:wrap}}
.sub-sub-url{{font-family:ui-monospace,monospace;font-size:10px;color:var(--accent2);word-break:break-all;flex:1;min-width:140px}}

.stats-bar{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px}}
.stat-card{{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:16px 17px;transition:.2s}}
.stat-card:hover{{border-color:var(--card-bh);transform:translateY(-1px)}}
.stat-label{{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:7px}}
.stat-val{{font-size:22px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.01em}}
.stat-sub{{font-size:9.5px;color:var(--t3);margin-top:6px}}

.copy-all-bar{{display:flex;align-items:center;gap:12px;background:linear-gradient(120deg,var(--accent) 0%,#2952C8 100%);border-radius:18px;padding:16px 19px;margin-bottom:18px;box-shadow:0 10px 30px rgba(59,124,246,.28);flex-wrap:wrap}}
.copy-all-text{{flex:1;min-width:160px}}
.copy-all-title{{font-size:13.5px;font-weight:800;color:#fff;display:flex;align-items:center;gap:6px}}
.copy-all-sub{{font-size:10px;color:rgba(255,255,255,.78);margin-top:3px}}
.copy-all-btn{{background:#fff;color:#047857;border:none;border-radius:12px;padding:10px 19px;font-family:inherit;font-size:12.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.18s;white-space:nowrap}}
.copy-all-btn:hover{{transform:translateY(-1px);box-shadow:0 6px 16px rgba(0,0,0,.22)}}
.copy-all-btn:active{{transform:translateY(0) scale(.98)}}

.cfg-title{{font-size:12px;font-weight:800;color:var(--t2);margin-bottom:13px;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.07em}}
.cfg-title i{{color:var(--accent);font-size:15px}}
.cfg-grid{{display:grid;gap:13px}}

/* ── کارت کانفیگ به‌شکل بلیط دسترسی (signature element) ── */
.cfg-card{{background:var(--card);border:1px solid var(--card-b);border-radius:18px;transition:all .2s;position:relative;overflow:hidden}}
.cfg-card:hover{{border-color:var(--card-bh);box-shadow:var(--shadow)}}
.cfg-top{{padding:17px 19px 15px;position:relative}}
.cfg-top::after{{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}}
.cfg-card.inactive .cfg-top::after{{background:var(--red)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px;flex-wrap:wrap}}
.cfg-label{{font-size:14.5px;font-weight:700;color:var(--t1)}}
.cfg-badges{{display:flex;gap:5px;flex-wrap:wrap;margin-top:6px}}
.proto-chip{{font-size:9px;padding:3px 8px;border-radius:7px;font-weight:800;letter-spacing:.02em}}
.pc-ws{{background:var(--accent-d);color:var(--accent2)}}
.pc-xhttp{{background:var(--purple-bg);color:var(--purple-t)}}
.pc-ultra{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status{{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:700;padding:4px 10px;border-radius:20px;white-space:nowrap}}
.cfg-status.ok{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status.no{{background:var(--red-bg);color:var(--red-t)}}
.cfg-usage{{margin-bottom:4px}}
.ubar{{height:6px;border-radius:4px;background:rgba(96,148,246,0.1);overflow:hidden;margin-bottom:5px}}
.ubar-f{{height:100%;border-radius:4px;transition:width .5s ease}}
.utxt{{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}}

/* خط جداکننده‌ی بلیطی با دندانه‌های گرد، شبیه پاره‌خط بُرد بلیط */
.cfg-tear{{position:relative;height:0;border-top:1.5px dashed var(--card-b);margin:0 19px}}
.cfg-tear::before,.cfg-tear::after{{content:'';position:absolute;top:50%;width:18px;height:18px;border-radius:50%;background:var(--bg);transform:translateY(-50%);border:1px solid var(--card-b)}}
.cfg-tear::before{{right:-28px}}
.cfg-tear::after{{left:-28px}}

.cfg-bottom{{padding:15px 19px 18px}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1px dashed var(--card-b);border-radius:11px;padding:10px 13px;cursor:pointer;font-family:inherit;color:var(--t2);font-size:11.5px;font-weight:600;transition:.15s}}
.cfg-link-toggle:hover{{background:var(--accent-d);border-color:var(--card-bh);color:var(--accent2)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:7px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .2s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s ease}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(0,0,0,.22);border:1px solid var(--card-b);border-radius:10px;padding:11px 13px;font-size:9.8px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.7;margin-top:9px;max-height:90px;overflow-y:auto}}
[data-theme="light"] .cfg-vless{{background:rgba(46,99,214,.05)}}
.cfg-link-label{{font-size:9.5px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:5px;margin-top:11px;margin-bottom:5px;text-transform:uppercase;letter-spacing:.05em}}
.cfg-link-label i{{font-size:12px}}
.cfg-link-label .ll-vless i{{color:var(--accent2)}}
.cfg-link-label .ll-sub i{{color:var(--purple-t)}}
.cfg-vless.is-sub{{color:var(--purple-t);margin-top:5px}}
[data-theme="light"] .cfg-vless.is-sub{{background:rgba(157,123,240,.05)}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap;margin-top:11px}}
.btn{{font-family:inherit;font-size:11.5px;font-weight:700;border-radius:10px;padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-g{{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(96,148,246,.16)}}
.btn-g:hover{{background:rgba(96,148,246,.2)}}
.btn-pur{{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(157,123,240,.2)}}
.btn-pur:hover{{background:rgba(157,123,240,.22)}}
.conn-chip{{display:inline-flex;align-items:center;gap:4px;font-size:9.5px;padding:3px 8px;border-radius:20px;background:var(--green-bg);color:var(--green-t);font-weight:700}}
.dot{{width:5px;height:5px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}

/* ── صفحه‌ی قفل / رمز ── */
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:78vh;padding:20px 0}}
.lock-card{{background:var(--card);border:1px solid var(--card-b);border-radius:26px;padding:0;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow);overflow:hidden;position:relative}}
.lock-banner{{background:linear-gradient(150deg,rgba(59,124,246,.16),rgba(59,124,246,.02) 70%);padding:38px 30px 26px;position:relative}}
.lock-shield{{width:64px;height:64px;border-radius:18px;background:var(--accent-d);border:1px solid var(--card-bh);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-7px;border-radius:22px;border:1px solid var(--card-b);animation:breathe 2.6s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.5}}50%{{transform:scale(1.08);opacity:0}}}}
.lock-shield i{{font-size:28px;color:var(--accent2)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px;color:var(--t1);letter-spacing:-.01em}}
.lock-sub{{font-size:12px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:24px 30px 30px}}
.lock-field{{position:relative;margin-bottom:13px}}
.lock-inp{{width:100%;padding:13px 44px 13px 44px;border-radius:13px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.14em;transition:.18s}}
[data-theme="light"] .lock-inp{{background:rgba(46,99,214,.04)}}
.lock-inp:focus{{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d)}}
.lock-eye{{position:absolute;left:13px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}}
.lock-eye:hover{{color:var(--accent2)}}
.lock-lockicon{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none}}
.lock-err{{color:var(--red-t);font-size:11.5px;margin-bottom:10px;min-height:16px;display:flex;align-items:center;justify-content:center;gap:5px}}
.lock-btn{{width:100%;justify-content:center;padding:13px;font-size:13px;border-radius:13px}}
.lock-footer{{padding:14px 30px;border-top:1px solid var(--card-b);font-size:10px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}}

.empty-state{{text-align:center;padding:80px 20px;color:var(--t3)}}
.empty-state i{{font-size:38px;display:block;margin-bottom:14px}}

.toast{{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:12px;padding:10px 20px;font-size:12.5px;font-weight:600;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:var(--shadow);white-space:nowrap}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(31,184,126,.35);background:var(--green-bg);color:var(--green-t)}}

.qr-modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.72);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:26px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow)}}
.qr-title{{font-size:13.5px;font-weight:800;margin-bottom:16px;color:var(--t1)}}
.qr-img{{border-radius:14px;overflow:hidden;margin-bottom:15px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:10px;border-radius:14px}}

.footer{{text-align:center;padding-top:28px;font-size:10.5px;color:var(--t3)}}
.footer a{{color:var(--accent2);font-weight:700}}

@media(max-width:520px){{
  .stats-bar{{grid-template-columns:1fr 1fr}}
  .stats-bar .stat-card:nth-child(3){{grid-column:1/-1}}
  .sub-name{{font-size:19px}}
  .copy-all-bar{{flex-direction:column;align-items:stretch}}
  .copy-all-btn{{justify-content:center}}
  .wrap{{padding:16px 12px 50px}}
  .lock-banner{{padding:32px 22px 22px}}
  .lock-form{{padding:20px 22px 26px}}
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
/* FineVPN_v2ray v1.0.0 — midnight glass / luminous gold visual system */



/* FineVPN_v2ray public page — starry glass and illuminated gold */
:root, [data-theme="light"]{{
  --bg:#030713;--bg2:rgba(5,11,28,.88);--bg3:rgba(17,27,52,.72);--card:rgba(13,22,45,.67);
  --card-b:rgba(231,190,82,.2);--card-bh:rgba(255,218,115,.48);--accent:#f0c45b;--accent2:#ffe5a0;--accent-d:rgba(240,196,91,.13);
  --green:#55d7ad;--green-bg:rgba(85,215,173,.12);--green-t:#88f0ce;--red:#fb7185;--red-bg:rgba(251,113,133,.12);--red-t:#fda4af;
  --amber:#f5c451;--amber-bg:rgba(245,196,81,.12);--amber-t:#ffe29a;--purple:#d9b968;--purple-bg:rgba(217,185,104,.13);--purple-t:#ffe5a0;
  --t1:#f5f4ff;--t2:#c7cbe0;--t3:#8290b6;--shadow:0 16px 44px rgba(0,0,0,.38)
}}
html,body{{background-color:#030713;color:#f5f4ff}}
.bg-fx{{background-color:#030713;background-image:
  radial-gradient(1px 1px at 17px 23px,rgba(255,255,255,.86) 55%,transparent 100%),
  radial-gradient(1.4px 1.4px at 71px 101px,rgba(255,225,164,.72) 55%,transparent 100%),
  linear-gradient(rgba(2,6,18,.78),rgba(2,6,18,.83)),url("https://i.ibb.co/39zWtJzS/1791731497906.jpg");
  background-size:109px 109px,173px 173px,100% 100%,min(66vw,680px) auto;background-position:0 0,35px 61px,center,center;
  background-repeat:repeat,repeat,no-repeat,no-repeat;opacity:1}}
.grid-fx{{background-image:none;opacity:0}}
.brand-img{{width:48px;height:48px;border-radius:14px;border-color:rgba(255,220,125,.48);box-shadow:0 0 20px rgba(240,196,91,.2)}}
.brand-name{{color:#fff0bd}}
.sub-info,.stat-card,.cfg-card,.lock-card,.qr-box,.copy-all-bar,.config-card,.sub-card{{background:linear-gradient(145deg,rgba(18,29,57,.78),rgba(6,12,29,.74))!important;border-color:rgba(240,196,91,.2)!important;box-shadow:0 16px 42px rgba(0,0,0,.24);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}}
.btn-p,.btn-g,.btn-o,.btn-pur,.copy-all-btn,.lock-btn{{background:linear-gradient(135deg,#fff0b8 0%,#f1ca62 42%,#bd8a25 100%)!important;color:#211805!important;border:1px solid rgba(255,233,164,.56)!important;box-shadow:0 0 18px rgba(240,196,91,.18),0 7px 22px rgba(0,0,0,.24)!important}}
.btn-p:hover,.btn-g:hover,.btn-o:hover,.btn-pur:hover,.copy-all-btn:hover,.lock-btn:hover{{background:linear-gradient(135deg,#fff6d6 0%,#ffe18a 45%,#d7a63a 100%)!important;transform:translateY(-1px);box-shadow:0 0 25px rgba(240,196,91,.31)!important}}
input,textarea,select,.lock-inp{{background:rgba(4,9,24,.65)!important;border-color:rgba(240,196,91,.2)!important;color:#f5f4ff!important}}
input:focus,textarea:focus,select:focus,.lock-inp:focus{{border-color:#f0c45b!important;box-shadow:0 0 0 3px rgba(240,196,91,.12)!important}}
.brand-contact{{margin-top:28px;padding:18px 20px;border:1px solid rgba(240,196,91,.24);border-radius:22px;background:linear-gradient(135deg,rgba(22,31,56,.82),rgba(6,12,28,.74));box-shadow:0 18px 45px rgba(0,0,0,.28);backdrop-filter:blur(22px);display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap}}
.brand-contact-identity{{display:flex;align-items:center;gap:13px;min-width:0}}
.brand-contact-logo{{width:56px;height:56px;object-fit:cover;border-radius:15px;border:1px solid rgba(255,220,125,.44);box-shadow:0 0 22px rgba(240,196,91,.15)}}
.brand-contact-title{{font-size:15px;font-weight:900;color:#fff0bd;letter-spacing:.02em}}
.brand-contact-provider{{font-size:11px;color:#d0d5e9;margin-top:4px}}
.brand-contact-signature{{font-size:12px;color:#f4d98c;margin-top:3px;letter-spacing:.04em}}
.brand-contact-links{{display:flex;gap:9px;flex-wrap:wrap}}
.fine-tg-link{{display:inline-flex;align-items:center;gap:8px;padding:10px 13px;border-radius:13px;border:1px solid rgba(240,196,91,.24);background:rgba(240,196,91,.07);color:#ffe5a0;font-size:11.5px;font-weight:700;transition:all .2s}}
.fine-tg-link i{{font-size:18px;color:#f6cf67}}
.fine-tg-link:hover{{transform:translateY(-2px);background:rgba(240,196,91,.15);box-shadow:0 0 20px rgba(240,196,91,.12)}}
@media(max-width:560px){{.wrap{{padding:16px 12px 44px}}.brand-contact{{padding:14px;gap:14px}}.brand-contact-links{{width:100%}}.fine-tg-link{{flex:1;justify-content:center;min-width:125px}}.brand-contact-logo{{width:48px;height:48px}}}}
@media(prefers-reduced-motion:reduce){{*,*::before,*::after{{animation-duration:.01ms!important;animation-iteration-count:1!important;scroll-behavior:auto!important;transition-duration:.01ms!important}}}}

html[data-accent="blue"]{{--accent:#60a5fa;--accent2:#93c5fd;--accent-d:rgba(96,165,250,.15)}}
html[data-accent="purple"]{{--accent:#a78bfa;--accent2:#c4b5fd;--accent-d:rgba(167,139,250,.15)}}
html[data-accent="emerald"]{{--accent:#34d399;--accent2:#6ee7b7;--accent-d:rgba(52,211,153,.15)}}
html[data-accent="gold"]{{--accent:#f0c45b;--accent2:#ffe5a0;--accent-d:rgba(240,196,91,.13)}}
.top-actions{{display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:flex-end}}
.public-action{{padding:8px 11px;border-radius:11px;border:1px solid var(--card-b);background:rgba(13,22,45,.72);color:var(--t1);font-family:inherit;font-weight:700;font-size:11px;cursor:pointer;display:inline-flex;gap:6px;align-items:center}}
.download-section{{margin-top:24px;padding:18px;border:1px solid var(--card-b);border-radius:20px;background:linear-gradient(145deg,rgba(18,29,57,.72),rgba(6,12,29,.7));backdrop-filter:blur(20px)}}
.download-title{{font-size:15px;font-weight:900;margin-bottom:5px}}
.download-subtitle{{font-size:11px;color:var(--t2);margin-bottom:14px;line-height:1.8}}
.download-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px}}
.download-card{{display:flex;gap:11px;align-items:center;text-decoration:none;border:1px solid var(--card-b);background:rgba(255,255,255,.025);border-radius:14px;padding:13px;color:var(--t1);transition:transform .18s,border-color .18s}}
.download-card:hover{{transform:translateY(-2px);border-color:var(--card-bh)}}
.download-app-icon{{width:42px;height:42px;border-radius:12px;display:grid;place-items:center;background:var(--accent-d);color:var(--accent2);font-size:22px;flex-shrink:0}}
.download-app-name{{font-weight:800;font-size:12px}}
.download-app-platform{{font-size:10px;color:var(--t2);margin-top:3px}}
.speed-panel{{margin:18px 0;padding:16px;border:1px solid var(--card-b);border-radius:18px;background:linear-gradient(145deg,rgba(18,29,57,.72),rgba(6,12,29,.7))}}
.speed-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-bottom:12px}}
.speed-chip{{padding:12px;border:1px solid var(--card-b);border-radius:13px;background:rgba(255,255,255,.025)}}
.speed-chip label{{display:block;color:var(--t2);font-size:10px;margin-bottom:5px}}
.speed-chip strong{{font-size:17px;direction:ltr;display:block}}
#traffic-chart{{width:100%;height:90px;display:block}}

html[data-accent="blue"] .btn-p,html[data-accent="blue"] .btn-g,html[data-accent="blue"] .btn-o,html[data-accent="blue"] .btn-pur,html[data-accent="blue"] .copy-all-btn,html[data-accent="blue"] .lock-btn{{background:linear-gradient(135deg,#dbeafe,#60a5fa)!important;color:#10213b!important;border-color:rgba(96,165,250,.65)!important}}
html[data-accent="purple"] .btn-p,html[data-accent="purple"] .btn-g,html[data-accent="purple"] .btn-o,html[data-accent="purple"] .btn-pur,html[data-accent="purple"] .copy-all-btn,html[data-accent="purple"] .lock-btn{{background:linear-gradient(135deg,#ede9fe,#a78bfa)!important;color:#251446!important;border-color:rgba(167,139,250,.65)!important}}
html[data-accent="emerald"] .btn-p,html[data-accent="emerald"] .btn-g,html[data-accent="emerald"] .btn-o,html[data-accent="emerald"] .btn-pur,html[data-accent="emerald"] .copy-all-btn,html[data-accent="emerald"] .lock-btn{{background:linear-gradient(135deg,#d1fae5,#34d399)!important;color:#052e26!important;border-color:rgba(52,211,153,.65)!important}}
html[data-accent="gold"] .btn-p,html[data-accent="gold"] .btn-g,html[data-accent="gold"] .btn-o,html[data-accent="gold"] .btn-pur,html[data-accent="gold"] .copy-all-btn,html[data-accent="gold"] .lock-btn{{background:linear-gradient(135deg,#fff0b8,#f0c45b)!important;color:#211805!important;border-color:rgba(240,196,91,.65)!important}}
@keyframes fineStarDrift{{from{{background-position:0 0,35px 61px,center,center}}to{{background-position:109px 109px,208px 234px,center,center}}}}
.bg-fx{{animation:fineStarDrift 90s linear infinite}}
@media(prefers-reduced-motion:reduce){{.bg-fx{{animation:none!important}}}}

.brand-img,.brand-contact-logo{{border-radius:50%!important}}
.bg-fx::after{{content:'';position:absolute;left:50%;top:11%;width:min(46vw,420px);aspect-ratio:1;transform:translateX(-50%);border-radius:50%;border:1px solid rgba(255,220,125,.2);background:url("https://i.ibb.co/39zWtJzS/1791731497906.jpg") center/cover no-repeat;opacity:.055;box-shadow:0 0 80px rgba(240,196,91,.12);pointer-events:none}}
</style>
</head>
<body>
<div class="bg-fx"></div><div class="grid-fx"></div>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-img"><img src="https://i.ibb.co/39zWtJzS/1791731497906.jpg" alt="FineVPN_v2ray"></div>
      <div><div class="brand-name">FineVPN_v2ray</div><div class="brand-sub">Secure Subscription Portal</div></div>
    </div>
    <div class="top-actions">
      <button class="public-action" onclick="refreshSubscription()" id="refresh-sub-btn"><i class="ti ti-refresh"></i><span data-public-i18n="تازه‌سازی">تازه‌سازی</span></button>
      <button class="public-action" onclick="togglePublicLanguage()"><i class="ti ti-language"></i><span id="public-lang-label">English</span></button>
      <button class="public-action" onclick="togglePublicThemePanel()"><i class="ti ti-palette"></i> ظاهر</button>
    </div>
  </div>
  <div id="public-theme-panel" style="display:none;margin:0 0 18px;padding:16px;border:1px solid var(--card-b);border-radius:18px;background:linear-gradient(145deg,rgba(18,29,57,.92),rgba(6,12,29,.9));backdrop-filter:blur(20px)">
    <div style="font-size:14px;font-weight:900;margin-bottom:12px">تنظیم ظاهر پنل اشتراک</div>
    <div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:12px">
      <label for="public-theme-select" style="font-size:12px;font-weight:700">تم آماده</label>
      <select class="public-action" id="public-theme-select" onchange="applyPublicThemePreset(this.value,true)"><option value="blue">آبی</option><option value="purple">بنفش</option><option value="emerald">سبز زمردی</option><option value="gold">طلایی</option></select>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px">
      <label style="font-size:11px">رنگ دکمه‌ها<input id="public-theme-button" type="color" value="#60a5fa" style="display:block;width:100%;height:38px;margin-top:6px;border:1px solid var(--card-b);border-radius:9px;background:transparent;padding:3px"></label>
      <label style="font-size:11px">رنگ متن اصلی<input id="public-theme-text" type="color" value="#eff4ff" style="display:block;width:100%;height:38px;margin-top:6px;border:1px solid var(--card-b);border-radius:9px;background:transparent;padding:3px"></label>
      <label style="font-size:11px">رنگ حاشیه‌ها<input id="public-theme-border" type="color" value="#60a5fa" style="display:block;width:100%;height:38px;margin-top:6px;border:1px solid var(--card-b);border-radius:9px;background:transparent;padding:3px"></label>
    </div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:12px"><button class="public-action" onclick="savePublicTheme()"><i class="ti ti-device-floppy"></i> ذخیرهٔ ظاهر</button><button class="public-action" onclick="resetPublicTheme()"><i class="ti ti-refresh"></i> بازنشانی</button></div>
  </div>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
  </div>
  <div class="brand-contact public-brand-contact">
    <div class="brand-contact-identity"><img class="brand-contact-logo" src="https://i.ibb.co/39zWtJzS/1791731497906.jpg" alt="FineVPN_v2ray logo"><div><div class="brand-contact-title">FineVPN_v2ray</div><div class="brand-contact-provider">ارائه‌دهنده: مـحـمـدصـادق افـغـان</div><div class="brand-contact-signature">𝑀𝑢ℎ𝑎𝑚𝑚𝑎𝑑𝒔𝒂𝒅𝒊𝒒</div></div></div>
    <div class="brand-contact-links"><a class="fine-tg-link" href="https://t.me/sadiq_AFG1" target="_blank" rel="noopener noreferrer"><i class="ti ti-brand-telegram"></i><span>پشتیبانی @sadiq_AFG1</span></a></div>
  </div>
  <section class="download-section" aria-label="دانلود برنامه‌های سازگار">
    <div class="download-title">دانلود برنامه‌های سازگار</div>
    <div class="download-subtitle">برای واردکردن لینک اشتراک، برنامهٔ متناسب با دستگاه خود را از منبع رسمی دریافت کنید.</div>
    <div class="download-grid">
      <a class="download-card" href="https://play.google.com/store/apps/details?id=dev.hexasoftware.v2box" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-android"></i></span><span><span class="download-app-name">V2Box</span><span class="download-app-platform">Android · Google Play</span></span></a>
      <a class="download-card" href="https://play.google.com/store/apps/details?id=app.hiddify.com" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-android"></i></span><span><span class="download-app-name">Hiddify</span><span class="download-app-platform">Android · Google Play</span></span></a>
      <a class="download-card" href="https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-apple"></i></span><span><span class="download-app-name">V2Box</span><span class="download-app-platform">iPhone · App Store</span></span></a>
      <a class="download-card" href="https://github.com/hiddify/hiddify-app/releases/latest" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-windows"></i></span><span><span class="download-app-name">Hiddify</span><span class="download-app-platform">Windows · Official Releases</span></span></a>
    </div>
  </section>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';

let isDark=true;
function applyTheme(dark){{
  document.documentElement.setAttribute('data-theme','dark');
}}
function toggleTheme(){{}}
applyTheme(isDark);
let publicLang=localStorage.getItem('finevpn-v2ray-lang')||'fa';
function applyPublicAccent(){{const chosen=localStorage.getItem('finevpn-v2ray-public-preset')||'blue';document.documentElement.setAttribute('data-accent',['blue','purple','emerald','gold'].includes(chosen)?chosen:'blue')}}
function togglePublicThemePanel(){{const p=document.getElementById('public-theme-panel');if(!p)return;const show=p.style.display==='none'||!p.style.display;p.style.display=show?'block':'none';if(show)loadPublicTheme()}}
function publicHex(v,f){{return /^#[0-9a-fA-F]{{6}}$/.test(v||'')?v:f}}
function applyPublicThemePreset(theme,resetCustom=false){{const allowed=['blue','purple','emerald','gold'];const chosen=allowed.includes(theme)?theme:'blue';const presets={{blue:['#60a5fa','#93c5fd'],purple:['#a78bfa','#c4b5fd'],emerald:['#34d399','#6ee7b7'],gold:['#f0c45b','#ffe5a0']}};document.documentElement.setAttribute('data-accent',chosen);document.documentElement.style.setProperty('--accent',presets[chosen][0]);document.documentElement.style.setProperty('--accent2',presets[chosen][1]);try{{localStorage.setItem('finevpn-v2ray-public-preset',chosen)}}catch(e){{}}if(resetCustom){{try{{localStorage.removeItem('finevpn-v2ray-public-colors')}}catch(e){{}}document.getElementById('fine-public-theme-css')?.remove();document.documentElement.style.removeProperty('--t1');document.documentElement.style.removeProperty('--card-b');document.documentElement.style.removeProperty('--card-bh')}}const sel=document.getElementById('public-theme-select');if(sel)sel.value=chosen}}
function applyPublicTheme(save){{let c={{button:'#60a5fa',text:'#eff4ff',border:'#60a5fa'}};try{{const v=JSON.parse(localStorage.getItem('finevpn-v2ray-public-colors')||'{{}}');c={{button:publicHex(v.button,c.button),text:publicHex(v.text,c.text),border:publicHex(v.border,c.border)}}}}catch(e){{}}const b=document.getElementById('public-theme-button'),t=document.getElementById('public-theme-text'),r=document.getElementById('public-theme-border');if(b&&b.value)c.button=publicHex(b.value,c.button);if(t&&t.value)c.text=publicHex(t.value,c.text);if(r&&r.value)c.border=publicHex(r.value,c.border);document.documentElement.style.setProperty('--accent',c.button);document.documentElement.style.setProperty('--t1',c.text);document.documentElement.style.setProperty('--card-b',c.border+'55');document.documentElement.style.setProperty('--card-bh',c.border+'bb');let st=document.getElementById('fine-public-theme-css');if(!st){{st=document.createElement('style');st.id='fine-public-theme-css';document.head.appendChild(st)}}st.textContent='html[data-accent] .btn-p,html[data-accent] .btn-g,html[data-accent] .btn-o,html[data-accent] .btn-pur,html[data-accent] .copy-all-btn,html[data-accent] .lock-btn,html[data-accent] .public-action{{background:linear-gradient(135deg,'+c.button+','+c.button+')!important;color:#fff!important;border-color:'+c.border+'!important}}.sec-panel,.download-section,.speed-panel,.speed-chip,.download-card{{border-color:'+c.border+'77!important}}body,.sec-panel-title,.download-title{{color:'+c.text+'}}';if(b)b.value=c.button;if(t)t.value=c.text;if(r)r.value=c.border;if(save){{try{{localStorage.setItem('finevpn-v2ray-public-colors',JSON.stringify(c))}}catch(e){{}}}}}}
function savePublicTheme(){{applyPublicTheme(true);toast(publicLang==='fa'?'ظاهر اشتراک ذخیره شد':'Subscription appearance saved','ok')}}
function loadPublicTheme(){{let chosen='blue';try{{chosen=localStorage.getItem('finevpn-v2ray-public-preset')||'blue'}}catch(e){{}}applyPublicThemePreset(chosen);let raw=null;try{{raw=localStorage.getItem('finevpn-v2ray-public-colors')}}catch(e){{}}if(!raw)return;try{{const c=JSON.parse(raw);const b=document.getElementById('public-theme-button'),t=document.getElementById('public-theme-text'),r=document.getElementById('public-theme-border');if(b)b.value=publicHex(c.button,'#60a5fa');if(t)t.value=publicHex(c.text,'#eff4ff');if(r)r.value=publicHex(c.border,'#60a5fa')}}catch(e){{}}applyPublicTheme(false)}}
function resetPublicTheme(){{try{{localStorage.removeItem('finevpn-v2ray-public-colors');localStorage.removeItem('finevpn-v2ray-public-preset')}}catch(e){{}}document.getElementById('public-theme-button').value='#60a5fa';document.getElementById('public-theme-text').value='#eff4ff';document.getElementById('public-theme-border').value='#60a5fa';document.getElementById('fine-public-theme-css')?.remove();document.documentElement.style.removeProperty('--t1');document.documentElement.style.removeProperty('--card-b');document.documentElement.style.removeProperty('--card-bh');applyPublicThemePreset('blue');applyPublicTheme(false);toast(publicLang==='fa'?'ظاهر بازنشانی شد':'Appearance reset','ok')}}
try{{const initialPublicPreset=localStorage.getItem('finevpn-v2ray-public-preset')||'blue';applyPublicThemePreset(initialPublicPreset)}}catch(e){{applyPublicThemePreset('blue')}}
loadPublicTheme();
const PUBLIC_I18N={{'تازه‌سازی':'Refresh','در حال بارگذاری...':'Loading...','گروه دسترسی':'Access Group','آخرین بروزرسانی:':'Last updated:','کپی لینک ساب':'Copy subscription link','QR کل':'Group QR','کپی همه‌ی کانفیگ‌ها':'Copy all configurations','تمام لینک‌های فعال این گروه را یک‌جا کپی کن':'Copy all active links at once','کپی همه':'Copy all','کانفیگ‌های فعال':'Active configs','اتصالات زنده':'Live connections','آنلاین':'Online','کل مصرف':'Total usage','سهمیه و اعتبار گروه':'Group quota and validity','دانلود برنامه‌های سازگار':'Download compatible apps','برای واردکردن لینک اشتراک، برنامهٔ متناسب با دستگاه خود را از منبع رسمی دریافت کنید.':'Download a compatible client from its official store to import your subscription.','پشتیبانی @sadiq_AFG1':'Support @sadiq_AFG1','لینک کانفیگ':'Config link','لینک ساب کلاینت':'Client subscription link','کپی لینک':'Copy link','کپی ساب کلاینت':'Copy client subscription','نمایش لینک کانفیگ':'Show config link','پنهان کردن لینک':'Hide config link','ترافیک دانلود':'Download traffic','ترافیک آپلود':'Upload traffic','سرعت دانلود':'Download speed','سرعت آپلود':'Upload speed','آمار زندهٔ انتقال داده':'Live traffic statistics','حجم دانلود':'Download volume','حجم آپلود':'Upload volume','کانفیگ‌ها':'Configurations','عدد':'items','اتصال':'connection','مصرف شده':'used','سهمیه:':'Quota:','سهمیه: <b>نامحدود</b>':'Quota: <b>Unlimited</b>','اعتبار:':'Validity:','نامحدود':'Unlimited','روز مانده':'days left','اعتبار نامحدود':'Unlimited validity','محدودیت حجمی فعال نیست':'No traffic limit is active','مصرف‌شده:':'Used:','از':'of','QR کانفیگ':'Configuration QR','QR ساب':'Subscription QR','لینک کپی شد ✓':'Link copied ✓','لینک ساب کلاینت کپی شد ✓':'Client subscription copied ✓','همه‌ی':'all','کانفیگی برای کپی نیست':'No configurations to copy','داده تازه شد':'Data refreshed','تازه‌سازی ناموفق بود':'Refresh failed','خطا در بارگذاری':'Loading failed','آنلاین':'Online','فعال':'Active','غیرفعال':'Inactive','مصرف‌شده:':'Used:','سرعت از اختلاف شمارنده‌های واقعی بین درخواست‌های متوالی محاسبه می‌شود؛ در اولین بارگذاری ممکن است صفر باشد.':'Speed is calculated from real counter deltas between requests; it may be zero on first load.'}};
Object.assign(PUBLIC_I18N, {{"بستن":"Close","ارائه‌دهنده: مـحـمـدصـادق افـغـان":"Provider: Muhammad Sadiq Afghan","رمز اشتباه است":"Incorrect password","همه کانفیگ‌ها":"All configurations","نمودار سرعت واقعی":"Real-time speed chart","ساب گروه:":"Subscription group:","کانفیگ کپی شد ✓":"Configuration copied ✓","لینک ساب کپی شد ✓":"Subscription link copied ✓","اطلاعات تازه شد":"Information refreshed","خطا در بارگذاری":"Failed to load","کانفیگ کپی شد":"Configuration copied","تازه‌سازی ناموفق بود":"Refresh failed","همه‌ی":"all","داده تازه شد":"Data refreshed","آخرین بروزرسانی:":"Last updated:","محدودیت حجمی فعال نیست":"No traffic limit is active","مصرف شده":"used","سهمیه:":"Quota:","اعتبار:":"Validity:","مصرف‌شده:":"Used:","از":"of","اتصال":"connection","روز مانده":"days left","نامحدود":"Unlimited","فعال":"Active","غیرفعال":"Inactive","QR کانفیگ":"Configuration QR","QR ساب":"Subscription QR","آنلاین":"Online"}});
Object.assign(PUBLIC_I18N, {{"ظاهر":"Appearance","تنظیم ظاهر پنل اشتراک":"Subscription appearance","تم آماده":"Preset theme","رنگ دکمه‌ها":"Button color","رنگ متن اصلی":"Main text color","رنگ حاشیه‌ها":"Border color","ذخیرهٔ ظاهر":"Save appearance","بازنشانی":"Reset","ظاهر اشتراک ذخیره شد":"Subscription appearance saved","ظاهر بازنشانی شد":"Appearance reset"}});
const PUBLIC_I18N_TEXT_ORIGINALS=new WeakMap();
function translatePublic(lang){{
  const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);const nodes=[];
  while(walker.nextNode())nodes.push(walker.currentNode);
  for(const node of nodes){{
    const parent=node.parentElement;if(!parent||parent.closest('script,style,textarea,input,pre,code'))continue;
    if(!PUBLIC_I18N_TEXT_ORIGINALS.has(node))PUBLIC_I18N_TEXT_ORIGINALS.set(node,node.nodeValue||'');
    const original=PUBLIC_I18N_TEXT_ORIGINALS.get(node);const match=original.match(/^(\\s*)([\\s\\S]*?)(\\s*)$/);if(!match)continue;
    const raw=match[2].trim();if(!raw)continue;
    const next=lang==='en'?(PUBLIC_I18N[raw]||raw):raw;const value=match[1]+next+match[3];
    if(node.nodeValue!==value)node.nodeValue=value;
  }}
  document.documentElement.lang=lang;document.documentElement.dir=lang==='fa'?'rtl':'ltr';const lbl=document.getElementById('public-lang-label');if(lbl)lbl.textContent=lang==='fa'?'English':'فارسی';
}}
function togglePublicLanguage(){{publicLang=publicLang==='fa'?'en':'fa';try{{localStorage.setItem('finevpn-v2ray-lang',publicLang)}}catch(e){{}}translatePublic(publicLang)}}
applyPublicAccent();translatePublic(publicLang);

function toast(msg,type=''){{
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}}
function fmtBps(b){{return fmtB(b)}}
let trafficHistory=[];
function drawTrafficChart(d){{const c=document.getElementById('traffic-chart');if(!c)return;const ctx=c.getContext('2d');const vals=[Math.max(0,d.download_speed_bps||0),Math.max(0,d.upload_speed_bps||0)];trafficHistory.push(vals);if(trafficHistory.length>24)trafficHistory.shift();const w=c.width,h=c.height;ctx.clearRect(0,0,w,h);ctx.strokeStyle='rgba(148,163,184,.18)';ctx.lineWidth=1;for(let y=15;y<h;y+=25){{ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(w,y);ctx.stroke()}}const max=Math.max(1,...trafficHistory.flat());for(let series=0;series<2;series++){{ctx.beginPath();trafficHistory.forEach((pair,i)=>{{const x=trafficHistory.length<2?w/2:(i/(trafficHistory.length-1))*w;const y=h-5-(pair[series]/max)*(h-18);if(i===0)ctx.moveTo(x,y);else ctx.lineTo(x,y)}});ctx.strokeStyle=series===0?'#60a5fa':'#34d399';ctx.lineWidth=2;ctx.stroke()}}}}
function toFa(n){{return String(n).replace(/\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}}
function protoChip(p){{
  if(p==='xhttp-stream-up')return '<span class="proto-chip pc-ultra"><i class="ti ti-bolt"></i> XHTTP ULTRA</span>';
  if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp">'+esc(p)+'</span>';
  return '<span class="proto-chip pc-ws">VLESS · WS</span>';
}}

function showQR(label,link){{
  document.getElementById('qr-label').textContent=label;
  document.getElementById('qr-img').src='/api/qr?data='+encodeURIComponent(link);
  document.getElementById('qr-modal').classList.add('open');
}}

function toggleLink(i){{
  const wrap=document.getElementById('vw-'+i);
  const btn=document.getElementById('vt-'+i);
  const open=wrap.classList.toggle('open');
  btn.classList.toggle('open',open);
  btn.querySelector('.ltl span').textContent = open ? 'پنهان کردن لینک' : 'نمایش لینک کانفیگ';
}}

async function loadData(pw=''){{
  const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');
  const r=await fetch(url);
  return r.json();
}}

function renderLock(name,errMsg=''){{
  document.getElementById('root').innerHTML=`
    <div class="lock-stage">
      <div class="lock-card">
        <div class="lock-banner">
          <div class="lock-shield"><i class="ti ti-shield-lock"></i></div>
          <div class="lock-title">${{esc(name)}}</div>
          <div class="lock-sub">این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز رو وارد کنید.</div>
        </div>
        <div class="lock-form">
          <div class="lock-err" id="lock-err">${{errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : ''}}</div>
          <div class="lock-field">
            <i class="ti ti-lock lock-lockicon"></i>
            <input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus>
            <button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button>
          </div>
          <button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود به گروه</button>
        </div>
        <div class="lock-footer"><i class="ti ti-shield-check"></i> اتصال شما رمزنگاری‌شده است</div>
      </div>
    </div>
  `;
  const inp=document.getElementById('lock-pw');
  inp.addEventListener('keydown',e=>{{if(e.key==='Enter')submitLock()}});
}}

function togglePwVis(){{
  const inp=document.getElementById('lock-pw');
  const icon=document.getElementById('lock-eye-icon');
  const toText = inp.type==='password';
  inp.type = toText ? 'text' : 'password';
  icon.className = 'ti '+(toText ? 'ti-eye-off' : 'ti-eye');
}}

async function submitLock(){{
  const pw=document.getElementById('lock-pw').value;
  const data=await loadData(pw);
  if(data.locked){{renderLock(data.name,'رمز اشتباه است');return}}
  savedPw=pw;
  renderContent(data);
}}

function renderContent(d){{
  const activeCount=d.links.filter(l=>l.active).length;
  if (!d.total_limit_bytes) {{
    document.querySelectorAll('#stats-bar .stat-card').forEach(c => {{ c.style.gridColumn=''; }});
  }}
  const baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/sub-group/' + UUID_KEY);
  const subUrl = baseSubUrl + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : '');

  window._finevpnSubUrl  = subUrl;
  window._finevpnSubName = d.name;
  window._finevpnLinks   = d.links.map(l => ({{
    vless : l.vless_link,
    sub   : l.sub_url + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : ''),
    label : l.display_name || l.label,
  }}));

  document.getElementById('root').innerHTML=`
    <div class="sub-info">
      <div class="sub-eyebrow"><i class="ti ti-folders"></i> گروه دسترسی</div>
      <div class="sub-name">${{esc(d.name)}}</div>
      ${{d.desc ? `<div class="sub-desc">${{esc(d.desc)}}</div>` : ''}}
      <div class="sub-meta-row"><i class="ti ti-clock"></i> آخرین بروزرسانی: ${{new Date().toLocaleTimeString('fa-IR')}}</div>
      <div class="sub-sub-box">
        <span class="sub-sub-url">${{esc(subUrl)}}</span>
        <button class="btn btn-pur" style="padding:7px 12px;font-size:10.5px"
          onclick="navigator.clipboard.writeText(window._finevpnSubUrl).then(()=>toast('لینک ساب کپی شد ✓','ok'))">
          <i class="ti ti-copy"></i> کپی لینک ساب
        </button>
        <button class="btn btn-g" style="padding:7px 12px;font-size:10.5px"
          onclick="showQR(window._finevpnSubName + ' — کل گروه', window._finevpnSubUrl)">
          <i class="ti ti-qrcode"></i> QR کل
        </button>
      </div>
    </div>

    <div class="copy-all-bar">
      <div class="copy-all-text">
        <div class="copy-all-title"><i class="ti ti-copy"></i> کپی همه‌ی کانفیگ‌ها</div>
        <div class="copy-all-sub">تمام لینک‌های فعال این گروه را یک‌جا کپی کن</div>
      </div>
      <button class="copy-all-btn" onclick="copyAllConfigs()"><i class="ti ti-clipboard-copy"></i> کپی همه (${{toFa(activeCount)}})</button>
    </div>

    <div class="stats-bar" id="stats-bar">
      <div class="stat-card">
        <div class="stat-label">کانفیگ‌های فعال</div>
        <div class="stat-val">${{toFa(activeCount)}}</div>
        <div class="stat-sub">از ${{toFa(d.links.length)}} کانفیگ</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">اتصالات زنده</div>
        <div class="stat-val">${{toFa(d.active_connections)}}</div>
        <div class="stat-sub" style="color:var(--green-t);display:flex;align-items:center;gap:4px"><span class="dot"></span> آنلاین</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">کل مصرف</div>
        <div class="stat-val" style="font-size:17px;margin-top:3px">${{esc(d.total_used_fmt)}}</div>
        <div class="stat-sub">${{d.total_limit_bytes ? 'از ' + esc(d.total_limit_fmt) : 'همه کانفیگ‌ها'}}</div>
      </div>
      <div class="stat-card" style="grid-column:span 3">
        <div class="stat-label">سهمیه و اعتبار گروه</div>
        <div class="stat-val" style="font-size:15px;margin-top:4px;display:flex;align-items:center;gap:7px;flex-wrap:wrap">
          <i class="ti ti-database" style="font-size:17px;color:var(--accent2)"></i>
          ${{d.total_limit_bytes ? `سهمیه: <b>${{esc(d.total_limit_fmt)}}</b>` : 'سهمیه: <b>نامحدود</b>'}}
          <span style="opacity:.35">•</span>
          <i class="ti ti-clock" style="font-size:17px;color:var(--amber)"></i>
          ${{d.expires_at
              ? `اعتبار: <b>${{d.days_left}} روز</b> (تا ${{new Date(d.expires_at).toLocaleDateString('fa-IR')}})`
              : 'اعتبار: <b>نامحدود</b>'}}
        </div>
        <div class="stat-sub">${{d.total_limit_bytes ? 'مصرف‌شده: ' + esc(d.total_used_fmt) + ' از ' + esc(d.total_limit_fmt) : 'محدودیت حجمی فعال نیست'}}</div>
      </div>
    </div>

    <div class="speed-panel">
      <div class="cfg-title" style="margin:0 0 12px"><i class="ti ti-activity"></i> آمار زندهٔ انتقال داده</div>
      <div class="speed-grid">
        <div class="speed-chip"><label>سرعت دانلود</label><strong>${{esc(fmtBps(d.download_speed_bps||0))}}/s</strong></div>
        <div class="speed-chip"><label>سرعت آپلود</label><strong>${{esc(fmtBps(d.upload_speed_bps||0))}}/s</strong></div>
        <div class="speed-chip"><label>حجم دانلود</label><strong>${{esc(fmtB(d.download_bytes||0))}}</strong></div>
        <div class="speed-chip"><label>حجم آپلود</label><strong>${{esc(fmtB(d.upload_bytes||0))}}</strong></div>
      </div>
      <canvas id="traffic-chart" width="720" height="90" aria-label="نمودار سرعت واقعی" role="img"></canvas>
      <div class="stat-sub">سرعت از اختلاف شمارنده‌های واقعی بین درخواست‌های متوالی محاسبه می‌شود؛ در اولین بارگذاری ممکن است صفر باشد.</div>
    </div>

    <div class="cfg-title"><i class="ti ti-link"></i> کانفیگ‌ها (${{toFa(d.links.length)}} عدد)</div>
    <div class="cfg-grid">
      ${{d.links.map((l, i) => {{
        const pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
        const bc  = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--green)';
        const lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
        return `
          <div class="cfg-card${{l.active ? '' : ' inactive'}}">
            <div class="cfg-top">
              <div class="cfg-head">
                <div>
                  <div class="cfg-label">${{esc(l.display_name || l.label)}}</div>
                  <div class="cfg-badges">
                    ${{protoChip(l.protocol)}}
                    ${{l.connections > 0 ? `<span class="conn-chip"><span class="dot"></span> ${{toFa(l.connections)}} اتصال</span>` : ''}}
                  </div>
                </div>
                <span class="cfg-status ${{l.active ? 'ok' : 'no'}}">${{l.active ? '<i class="ti ti-circle-check"></i> فعال' : '<i class="ti ti-circle-x"></i> غیرفعال'}}</span>
              </div>
              <div class="cfg-usage">
                <div class="ubar"><div class="ubar-f" style="width:${{pct}}%;background:${{bc}}"></div></div>
                <div class="utxt"><span>${{esc(l.used_fmt)}} مصرف شده</span><span>سهمیه: ${{lim}}</span></div>
              </div>
            </div>
            <div class="cfg-tear"></div>
            <div class="cfg-bottom">
              <button class="cfg-link-toggle" id="vt-${{i}}" onclick="toggleLink(${{i}})">
                <span class="ltl"><i class="ti ti-eye"></i> <span>نمایش لینک کانفیگ</span></span>
                <i class="ti ti-chevron-down"></i>
              </button>
              <div class="cfg-vless-wrap" id="vw-${{i}}">
                <div class="cfg-vless-inner">
                  <div class="cfg-link-label"><span class="ll-vless"><i class="ti ti-key"></i> لینک کانفیگ</span></div>
                  <div class="cfg-vless">${{esc(l.vless_link)}}</div>
                  <div class="cfg-link-label"><span class="ll-sub"><i class="ti ti-rss"></i> لینک ساب کلاینت</span></div>
                  <div class="cfg-vless is-sub">${{esc(l.sub_url)}}</div>
                </div>
              </div>
              <div class="cfg-actions">
                <button class="btn btn-p"
                  onclick="navigator.clipboard.writeText(window._finevpnLinks[${{i}}].vless).then(()=>toast('لینک کپی شد ✓','ok'))">
                  <i class="ti ti-copy"></i> کپی لینک
                </button>
                <button class="btn btn-pur"
                  onclick="navigator.clipboard.writeText(window._finevpnLinks[${{i}}].sub).then(()=>toast('لینک ساب کلاینت کپی شد ✓','ok'))">
                  <i class="ti ti-rss"></i> کپی ساب کلاینت
                </button>
                <button class="btn btn-g"
                  onclick="showQR(window._finevpnLinks[${{i}}].label, window._finevpnLinks[${{i}}].vless)">
                  <i class="ti ti-qrcode"></i> QR کانفیگ
                </button>
                <button class="btn btn-g"
                  onclick="showQR('ساب گروه: '+window._finevpnSubName, window._finevpnSubUrl)">
                  <i class="ti ti-rss"></i> QR ساب
                </button>
              </div>
            </div>
          </div>
        `;
      }}).join('')}}
    </div>
  `;
  drawTrafficChart(d);
  translatePublic(publicLang);
  setTimeout(() => autoRefresh(), 10000);
}}

function copyAllConfigs(){{
  const links=window._finevpnLinks||[];
  if(!links.length){{toast('کانفیگی برای کپی نیست','');return}}
  const text=links.map(l=>l.vless).join('\\n');
  navigator.clipboard.writeText(text).then(()=>toast('همه‌ی '+toFa(links.length)+' کانفیگ کپی شد ✓','ok'));
}}

async function refreshSubscription(){{
  const btn=document.getElementById('refresh-sub-btn');if(btn)btn.disabled=true;
  try{{const data=await loadData(savedPw);if(data.locked){{renderLock(data.name);return}}renderContent(data);toast(publicLang==='fa'?'اطلاعات تازه شد':'Data refreshed','ok')}}catch(e){{toast(publicLang==='fa'?'تازه‌سازی ناموفق بود':'Refresh failed','err')}}finally{{if(btn)btn.disabled=false}}
}}
async function autoRefresh(){{
  try{{
    const data = await loadData(savedPw);
    if (!data.locked) renderContent(data);
  }} catch(e) {{}}
}}

async function init(){{
  try{{
    const data = await loadData();
    if (data.locked) {{ renderLock(data.name); return; }}
    renderContent(data);
  }} catch(e) {{
    document.getElementById('root').innerHTML =
      '<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>خطا در بارگذاری</div>';
  }}
}}

init();
</script>
</body></html>"""
