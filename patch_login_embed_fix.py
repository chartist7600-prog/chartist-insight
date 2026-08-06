#!/usr/bin/env python3
"""patch_login_embed_fix - 텔레그램 로그인 embed=1 → embed=0 수정 (승인은 되는데 앱 비로그인 버그)"""
import os

HTML = '/home/ubuntu/chartist-insight/index.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

orig = len(content)
done = []

# ══ 텔레그램 OAuth 로그인 URL: embed=1 → embed=0
# 원인: embed=1은 "iframe에 실제로 임베드된 위젯"용 플래그로, 이 모드에서는
#       텔레그램이 postMessage로만 결과를 돌려주고 return_to 해시 리다이렉트를
#       생략/누락시킬 수 있음. 반면 이 페이지 코드는 #tgAuthResult 해시를 직접
#       파싱하는 "리다이렉트 방식"을 쓰고 있으므로 embed=0이 맞는 값.
old_embed = "var loginUrl = 'https://oauth.telegram.org/auth?bot_id=8458968839&origin=https%3A%2F%2Fchartist-insight.com&embed=1&request_access=write&return_to=' + returnUrl;"
new_embed = "var loginUrl = 'https://oauth.telegram.org/auth?bot_id=8458968839&origin=https%3A%2F%2Fchartist-insight.com&embed=0&request_access=write&return_to=' + returnUrl;"

if old_embed in content:
    content = content.replace(old_embed, new_embed)
    done.append('embed=1 -> embed=0 (텔레그램 로그인 리다이렉트 수정)')
else:
    print('⚠ old_embed 앵커를 찾지 못함 - 파일이 이미 수정되었거나 내용이 다릅니다. 수동 확인 필요.')

if done:
    with open(HTML, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✅ 패치 완료 ({orig} -> {len(content)} bytes)')
    for d in done:
        print(' -', d)
else:
    print('❌ 적용된 패치 없음')
