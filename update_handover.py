update = """
---

## 2026-06-26~27 완료 작업 ✅

### 홈페이지 대규모 리디자인

**GitHub 계정 변경**
- 기존: BTCchartist (정지됨)
- 신규: chartist7600-prog / chartist7600@gmail.com
- Cloudflare Pages 자동배포 재연결 완료

**홈페이지 구조 변경 (index.html)**
- 주식 탭(tab-stock), 매크로 탭(tab-macro) 완전 제거
- 히어로 섹션 추가: "데이터 기반 크립토 인사이트" + 슬로건 + CTA 버튼
- 서비스 네비 메뉴 추가: [₿ 비트코인🔒] [📊 알트코인🔒] [🧮 매매계산기] [📒 매매일지]
  - 비로그인 시 비트코인/알트코인 클릭 → 텔레그램 로그인 팝업
  - 로그인 후 → 해당 탭으로 스크롤 이동
- 크립토 버블맵 섹션: 서비스 소개 섹션 다음 위치
- 포모(FOMO) 섹션: 최근 3일 추세전환 신호 수익률 상위 (플러스만 표시, 3개 공개+2개 블러)
- 서비스 소개 카드: 무료(매매계산기/매매일지) / 유료(비트코인/알트코인)

**텔레그램 OAuth 로그인**
- 봇: ChartMasterBot (토큰: 8458968839:AAECe9jx2k5e7zAFquBtlroQ3pXSXwhq57w)
- 백엔드: /home/ubuntu/tg_auth.py (port 8083)
- nginx: /tg 경로 → tg_auth.py
- BotFather /setdomain → chartist-insight.com 등록 완료
- 로그인 팝업 URL: https://oauth.telegram.org/auth?bot_id=8458968839&origin=https%3A%2F%2Fchartist-insight.com&embed=1&request_access=write

**접근 제한**
- 비로그인 시 탭 네비게이션 숨김 (CSS: body.tg-logged)
- 로그인 성공 시 body.classList.add('tg-logged') → 탭 노출
- BTC 탭: is_member OR rsi_unlocked 시 블러 해제

**네비바 변경**
- 순서: LIVE · 🔔 · 유튜브 · 구독하기 · 로그인
- 텔레그램 버튼 제거
- 매뉴얼(📖) 버튼 제거

**매매일지 변경**
- 팬딩 아이디/비번 로그인 팝업 → 텔레그램 로그인 버튼으로 교체

**포모 히스토리**
- trend_scanner.py에 fomo_history.json 자동 기록 코드 추가
- 파일: /home/ubuntu/chartist-insight/data/fomo_history.json
- 최근 3일 신호 + 수익률 플러스인 것만 표시 + 수익률 높은 순 정렬

---

## 미완료 항목 (PENDING)

| 항목 | 설명 |
|------|------|
| 텔레그램 로그인 후 UI | 로그인 성공 후 네비바 이름/멤버배지 표시 미완성 (postMessage 수신 문제) |
| 멤버/비멤버 구분 | is_member 기반 콘텐츠 잠금 - 로그인 UI 해결 후 구현 |
| 매매일지 텔레그램 연동 | 로그인 버튼만 있고 실제 서버 저장 연동 미완료 |
| "실시간 비트코인 신호..." 텍스트 | 버블맵 위에 노출되는 구 설명 텍스트 제거 필요 |

---

## 주요 파일 경로 (2026-06-27 기준)

| 파일 | 설명 |
|------|------|
| /home/ubuntu/chartist-insight/index.html | 홈페이지 메인 (2746줄) |
| /home/ubuntu/chartist-insight/data/fomo_history.json | 포모 히스토리 데이터 |
| /home/ubuntu/tg_auth.py | 텔레그램 OAuth 백엔드 (port 8083) |
| /home/ubuntu/trend_scanner.py | 추세전환 스캐너 (fomo_history 자동 기록) |
| /home/ubuntu/patch_fomo.py | 포모 섹션 패치 스크립트 |
| /home/ubuntu/patch_nav.py | 네비게이션 메뉴 패치 스크립트 |
| /home/ubuntu/patch_bubble.py | 버블맵 이동 패치 스크립트 |

---

## 핵심 설정값 추가

| 항목 | 값 |
|------|-----|
| ChartMasterBot 토큰 | 8458968839:AAECe9jx2k5e7zAFquBtlroQ3pXSXwhq57w |
| tg_auth.py 포트 | 8083 |
| GitHub 새 계정 | chartist7600-prog / chartist7600@gmail.com |
| maphack_bot 토큰 | 7777308406:AAHs9otXX64ij4udsftAMDJY77R4KVfyrps |
"""

with open('/home/ubuntu/인수인계서_20260608.md', 'r') as f:
    content = f.read()

content = content + update

with open('/home/ubuntu/인수인계서_20260608.md', 'w') as f:
    f.write(content)

print("완료")
