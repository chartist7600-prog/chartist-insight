with open('/home/ubuntu/chartist-insight/index.html', 'r') as f:
    content = f.read()

# 1. 네비게이션 메뉴 CSS
nav_css = """
  /* ══ 서비스 네비 메뉴 ══ */
  .service-nav{background:#0e0e0e;padding:0 20px;border-bottom:0.5px solid rgba(255,255,255,0.06);}
  .service-nav-inner{max-width:900px;margin:0 auto;display:flex;gap:0;}
  .service-nav-btn{flex:1;padding:14px 8px;background:none;border:none;border-bottom:2px solid transparent;color:#666;font-size:12px;font-weight:500;cursor:pointer;text-align:center;transition:all 0.15s;display:flex;align-items:center;justify-content:center;gap:5px;}
  .service-nav-btn:hover{color:#f0f0f0;border-bottom-color:rgba(201,168,76,0.3);}
  .service-nav-btn.active{color:#C9A84C;border-bottom-color:#C9A84C;}
  .service-nav-btn .nav-lock{font-size:9px;opacity:0.6;}
  @media(max-width:520px){.service-nav-btn{font-size:11px;padding:12px 4px;}}
"""

# 2. 네비게이션 메뉴 HTML - 히어로 다음, 포모 앞에
nav_html = """<nav class="service-nav">
  <div class="service-nav-inner">
    <button class="service-nav-btn" onclick="serviceNavClick('btc')">₿ 비트코인<span class="nav-lock">🔒</span></button>
    <button class="service-nav-btn" onclick="serviceNavClick('altcoin')">📊 알트코인<span class="nav-lock">🔒</span></button>
    <button class="service-nav-btn" onclick="serviceNavClick('calc')">🧮 매매계산기</button>
    <button class="service-nav-btn" onclick="serviceNavClick('journal')">📒 매매일지</button>
  </div>
</nav>
"""

# 3. 버블맵을 히어로 아래 독립 섹션으로 이동
bubble_html = """<section style="background:#0e0e0e;padding:20px;border-bottom:0.5px solid rgba(255,255,255,0.06);">
  <div style="max-width:900px;margin:0 auto;">
    <div style="font-size:11px;color:#555;margin-bottom:8px;letter-spacing:0.5px;">🫧 크립토 버블맵 &nbsp;·&nbsp; 시총 기준 · 색상 = 등락률</div>
    <iframe src="https://cryptobubbles.net" style="width:100%;height:420px;border:none;display:block;border-radius:10px;" loading="lazy" title="크립토 버블맵"></iframe>
  </div>
</section>
"""

# 4. JS
nav_js = """
function serviceNavClick(tab) {
  var tabNav = document.querySelector('.tab-nav');
  var logged = document.body.classList.contains('tg-logged');
  var freeTabs = ['calc', 'journal'];
  if (!logged && !freeTabs.includes(tab)) {
    tgLogin();
    return;
  }
  var btn = document.getElementById('tab-btn-' + tab);
  if (btn) switchTab(tab, btn);
  if (tabNav) tabNav.scrollIntoView({behavior: 'smooth', block: 'start'});
}
"""

ok = True

# CSS 삽입
if '</style>\n</head>' in content:
    content = content.replace('</style>\n</head>', nav_css + '</style>\n</head>', 1)
    print("CSS OK")
else:
    print("CSS FAIL"); ok=False

# HTML 삽입 - 히어로 섹션 바로 다음에
marker = '\n<section class="fomo-section">'
if marker in content:
    content = content.replace(marker, '\n' + nav_html + bubble_html + '\n<section class="fomo-section">', 1)
    print("HTML OK")
else:
    print("HTML FAIL"); ok=False

# JS 삽입
if '</body>' in content:
    content = content.replace('</body>', nav_js + '</body>', 1)
    print("JS OK")
else:
    print("JS FAIL"); ok=False

if ok:
    with open('/home/ubuntu/chartist-insight/index.html', 'w') as f:
        f.write(content)
    print("저장 완료")
else:
    print("실패")
