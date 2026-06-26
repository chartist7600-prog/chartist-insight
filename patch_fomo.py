with open('/home/ubuntu/chartist-insight/index.html', 'r') as f:
    content = f.read()

fomo_css = """
  .fomo-section{background:#0a0a0a;padding:28px 20px;border-bottom:0.5px solid rgba(255,255,255,0.06);}
  .fomo-container{max-width:900px;margin:0 auto;}
  .fomo-title{font-size:12px;color:#888;letter-spacing:0.8px;font-weight:500;margin-bottom:4px;}
  .fomo-subtitle{font-size:10px;color:#555;margin-bottom:16px;}
  .fomo-list{display:flex;flex-direction:column;gap:8px;}
  .fomo-item{background:#111;border:0.5px solid rgba(255,255,255,0.07);border-radius:10px;padding:12px 16px;display:flex;align-items:center;gap:12px;position:relative;overflow:hidden;}
  .fomo-item.blurred .fomo-right{filter:blur(6px);user-select:none;}
  .fomo-item.blurred .fomo-coin{filter:blur(4px);user-select:none;}
  .fomo-blur-overlay{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(10,10,10,0.6);border-radius:10px;}
  .fomo-blur-cta{background:#C9A84C;color:#0e0e0e;padding:6px 16px;border-radius:6px;font-size:11px;font-weight:700;text-decoration:none;}
  .fomo-rank{font-size:13px;color:#555;width:20px;text-align:center;flex-shrink:0;}
  .fomo-coin{flex:1;}
  .fomo-coin-name{font-size:13px;font-weight:700;color:#f0f0f0;}
  .fomo-coin-meta{font-size:10px;color:#555;margin-top:2px;}
  .fomo-right{text-align:right;flex-shrink:0;}
  .fomo-pct{font-size:16px;font-weight:700;color:#4caf7d;}
  .fomo-pct.neg{color:#ff6b6b;}
  .fomo-days{font-size:10px;color:#555;margin-top:2px;}
  .fomo-cta-row{text-align:center;margin-top:14px;}
  .fomo-cta-btn{background:transparent;border:0.5px solid rgba(201,168,76,0.4);color:#C9A84C;padding:8px 24px;border-radius:7px;font-size:12px;text-decoration:none;display:inline-block;}
"""

fomo_html = '<section class="fomo-section">\n  <div class="fomo-container">\n    <div class="fomo-title">🚀 멤버십 포착 코인 · 최근 30일 추세전환 신호</div>\n    <div class="fomo-subtitle">신호 발생 시점 대비 현재 수익률 · 실시간 업데이트</div>\n    <div class="fomo-list" id="fomo-list"><div style="text-align:center;color:#555;padding:20px;font-size:12px;">로딩 중...</div></div>\n    <div class="fomo-cta-row">\n      <a href="https://fanding.kr/@bzcLu6QCTdMe/membership/" target="_blank" class="fomo-cta-btn">전체 신호 보기 → 멤버십 가입</a>\n    </div>\n  </div>\n</section>\n'

fomo_js = '<script>\nfunction loadFomoSection(){\n  fetch("/data/fomo_history.json?t="+Date.now()).then(function(r){return r.json();}).then(function(data){\n    if(!data||!data.length){document.getElementById("fomo-list").innerHTML=\'<div style="text-align:center;color:#555;padding:20px;font-size:12px;">신호 데이터 준비 중...</div>\';return;}\n    var top5=data.slice(0,5);\n    var syms=JSON.stringify(top5.map(function(x){return x.ticker+"USDT";}));\n    fetch("https://api.binance.com/api/v3/ticker/price?symbols="+encodeURIComponent(syms)).then(function(r){return r.json();}).then(function(prices){\n      var pm={};\n      prices.forEach(function(p){pm[p.symbol]=parseFloat(p.price);});\n      renderFomo(top5,pm);\n    }).catch(function(){renderFomo(top5,{});});\n  }).catch(function(){});\n}\nfunction renderFomo(items,pm){\n  var el=document.getElementById("fomo-list");\n  if(!el)return;\n  var html="";\n  items.forEach(function(item,i){\n    var cur=pm[item.ticker+"USDT"]||0;\n    var entry=item.entry_price||0;\n    var pct=entry>0&&cur>0?((cur-entry)/entry*100):null;\n    var pctStr=pct!==null?(pct>=0?"+":"")+pct.toFixed(1)+"%":"—";\n    var neg=pct!==null&&pct<0?" neg":"";\n    var dt=item.entry_time?item.entry_time.split(" ")[0]:"";\n    var days=dt?Math.floor((Date.now()-new Date(dt))/86400000):"?";\n    var blur=i>=3;\n    html+=\'<div class="fomo-item\'+(blur?\' blurred\':\'\')+\'">\'+\'<div class="fomo-rank">\'+(i+1)+\'</div>\'+\'<div class="fomo-coin"><div class="fomo-coin-name">\'+item.ticker+\'<span style="font-size:11px;color:#666;font-weight:400;margin-left:6px;">\'+(item.name||"")+\'</span></div><div class="fomo-coin-meta">신호일: \'+dt+\'</div></div>\'+\'<div class="fomo-right"><div class="fomo-pct\'+neg+\'">\'+pctStr+\'</div><div class="fomo-days">\'+days+\'일 전</div></div>\';\n    if(blur)html+=\'<div class="fomo-blur-overlay"><a href="https://fanding.kr/@bzcLu6QCTdMe/membership/" target="_blank" class="fomo-blur-cta">멤버십 가입</a></div>\';\n    html+=\'</div>\';\n  });\n  el.innerHTML=html;\n}\nloadFomoSection();\n</script>\n'

ok = True
if '</style>\n</head>' in content:
    content = content.replace('</style>\n</head>', fomo_css + '</style>\n</head>', 1)
    print("CSS OK")
else:
    print("CSS FAIL"); ok=False

marker = '<section class="service-section">'
if marker in content:
    content = content.replace(marker, fomo_html + marker, 1)
    print("HTML OK")
else:
    print("HTML FAIL"); ok=False

if '</body>' in content:
    content = content.replace('</body>', fomo_js + '</body>', 1)
    print("JS OK")
else:
    print("JS FAIL"); ok=False

if ok:
    with open('/home/ubuntu/chartist-insight/index.html', 'w') as f:
        f.write(content)
    print("저장 완료")
else:
    print("실패 - 저장 안함")
