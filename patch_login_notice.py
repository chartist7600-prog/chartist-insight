#!/usr/bin/env python3
"""patch_login_notice - 홈페이지 공지 모달에 로그인 안내 문구 배포"""
import re

HTML = '/home/ubuntu/chartist-insight/index.html'
with open(HTML, 'r', encoding='utf-8') as f:
    content = f.read()

orig = len(content)

NEW_TEXT = (
    "[ 홈페이지(어플리케이션) 로그인 관련 안내 ]\\n\\n"
    "최근 홈페이지에서 텔레그램 로그인 시도 후 로그인이 안 되거나\\n"
    "버튼이 반응 없는 증상이 확인되어,\\n"
    "원인을 찾아 서버 쪽 수정을 완료했습니다.\\n\\n"
    "혹시 아직도 로그인이 안 되시는 분은,\\n"
    "기기에 예전 버전이 캐시로 남아있어서 그런 것으로\\n"
    "아래 안내대로 한 번만 다시 설치해주시면 정상 작동합니다 🙏\\n\\n"
    "▬▬▬▬▬▬▬▬▬▬▬▬▬\\n\\n"
    "[안드로이드]\\n\\n"
    "1. 홈 화면의 \\\"차티스트 인사이트\\\" 아이콘 길게 눌러서 삭제\\n"
    "2. 크롬 앱 실행\\n"
    "3. 크롬 설정 → 개인정보 보호 및 보안 → 인터넷 사용 기록 삭제 → \\\"캐시된 이미지 및 파일\\\" 체크 후 삭제\\n"
    "4. chartist-insight.com 접속\\n"
    "5. 크롬 메뉴(우측 상단 점 3개) → \\\"홈 화면에 추가\\\"\\n"
    "6. 새로 생긴 아이콘으로 실행 → 로그인 재시도\\n\\n"
    "[아이폰]\\n\\n"
    "1. 홈 화면의 \\\"차티스트 인사이트\\\" 아이콘 길게 눌러서 제거\\n"
    "2. 설정 → Safari → 방문 기록 및 웹 사이트 데이터 지우기\\n"
    "3. Safari로 chartist-insight.com 접속\\n"
    "4. 공유 버튼 → \\\"홈 화면에 추가\\\"\\n"
    "5. 새로 생긴 아이콘으로 실행 → 로그인 재시도\\n\\n"
    "▬▬▬▬▬▬▬▬▬▬▬▬▬\\n\\n"
    "이렇게 하시고도 로그인이 안 되시면\\n"
    "팬딩 포스팅 게시물 댓글로 편하게 말씀 주세요.\\n"
    "바로 확인해드리겠습니다 🙇\\u200d♂️"
)

pattern = re.compile(
    r'var NOTICE_ENABLED = (true|false);\s*\nvar NOTICE_TEXT = ".*?";\s*\nvar NOTICE_ID = ".*?";',
    re.DOTALL
)

new_block = (
    'var NOTICE_ENABLED = true;\n'
    'var NOTICE_TEXT = "' + NEW_TEXT + '";\n'
    'var NOTICE_ID = "2026-notice-5";'
)

new_content, n = pattern.subn(lambda m: new_block, content, count=1)

if n == 1:
    with open(HTML, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'DONE - 공지 문구 교체 완료 ({orig} -> {len(new_content)} bytes)')
else:
    print('WARNING: NOTICE_ENABLED/NOTICE_TEXT/NOTICE_ID 블록을 찾지 못했습니다. index.html 구조를 확인해주세요.')
