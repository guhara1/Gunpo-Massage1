# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://www.barogo-gunpo.example.com"

BRAND = "바로 GO"
BRAND_MARK = "GO"          # 브랜드 원형 배지 글자
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 군포시 지역 SEO 기준 경로 (지역 확장을 고려한 폴더 구조)
HOME = "/gyeonggi/gunpo/"

# 텔레그램 문의 링크 (웹사이트 제작문의·제휴문의 공용)
TELEGRAM_URL = "https://t.me/googleseolab"

# 상단 메뉴 — 하위 메뉴에는 "출장마사지" 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/gyeonggi/gunpo/", [
        ("군포시 메인", "/gyeonggi/gunpo/"),
        ("홈타이 이용 기준", "/gyeonggi/gunpo/#standard"),
        ("대표동 선택 안내", "/gyeonggi/gunpo/#areas"),
        ("예약 전 확인사항", "/gyeonggi/gunpo/#check"),
    ]),
    ("지역별 안내", "/gyeonggi/gunpo/#areas", [
        ("산본동", "/gyeonggi/gunpo/sanbon-dong/"),
        ("금정동", "/gyeonggi/gunpo/geumjeong-dong/"),
        ("군포동", "/gyeonggi/gunpo/gunpo-dong/"),
        ("당정동", "/gyeonggi/gunpo/dangjeong-dong/"),
        ("부곡동", "/gyeonggi/gunpo/bugok-dong/"),
        ("대야미동", "/gyeonggi/gunpo/daeyami-dong/"),
        ("송부동", "/gyeonggi/gunpo/songbu-dong/"),
    ]),
    ("역세권 안내", "/gyeonggi/gunpo/station/", [
        ("역 전체", "/gyeonggi/gunpo/station/"),
        ("산본역", "/gyeonggi/gunpo/station/sanbon-station/"),
        ("금정역", "/gyeonggi/gunpo/station/geumjeong-station/"),
        ("군포역", "/gyeonggi/gunpo/station/gunpo-station/"),
        ("당정역", "/gyeonggi/gunpo/station/dangjeong-station/"),
        ("대야미역", "/gyeonggi/gunpo/station/daeyami-station/"),
        ("수리산역", "/gyeonggi/gunpo/station/surisan-station/"),
        ("반월역 인접 생활권", "/gyeonggi/gunpo/station/banwol-nearby-area/"),
    ]),
    ("생활권 안내", "/gyeonggi/gunpo/area/", [
        ("생활권 전체", "/gyeonggi/gunpo/area/"),
        ("산본중심상가", "/gyeonggi/gunpo/area/sanbon-center/"),
        ("산본신도시", "/gyeonggi/gunpo/area/sanbon-newtown/"),
        ("금정역·군포시청", "/gyeonggi/gunpo/area/geumjeong-cityhall/"),
        ("군포역·당동", "/gyeonggi/gunpo/area/gunpo-station-dang-dong/"),
        ("당정역·한세대", "/gyeonggi/gunpo/area/dangjeong-hansei/"),
        ("부곡·송정지구", "/gyeonggi/gunpo/area/bugok-songjeong/"),
        ("대야미·수리산", "/gyeonggi/gunpo/area/daeyami-surisan/"),
        ("군포첨단산업단지", "/gyeonggi/gunpo/area/gunpo-industrial-complex/"),
        ("수리산역·오금동", "/gyeonggi/gunpo/area/surisan-ogeum/"),
        ("반월·대야미 인접", "/gyeonggi/gunpo/area/banwol-daeyami-nearby/"),
    ]),
    ("예약 안내", "/gyeonggi/gunpo/reservation/", [
        ("예약 가능 지역 확인", "/gyeonggi/gunpo/reservation/#place"),
        ("예약 가능 시간 안내", "/gyeonggi/gunpo/reservation/#hours"),
        ("추가 이동비 안내", "/gyeonggi/gunpo/reservation/#move"),
        ("결제 방식 안내", "/gyeonggi/gunpo/reservation/#payment"),
        ("예약 변경 안내", "/gyeonggi/gunpo/reservation/#change"),
        ("취소 기준 안내", "/gyeonggi/gunpo/reservation/#cancel"),
    ]),
    ("이용 전 확인사항", "/gyeonggi/gunpo/checklist/", [
        ("방문 가능 주소 확인", "/gyeonggi/gunpo/checklist/#address"),
        ("자택 이용 전 확인", "/gyeonggi/gunpo/checklist/#home"),
        ("숙소 이용 전 확인", "/gyeonggi/gunpo/checklist/#stay"),
        ("사무실 인근 이용 전 확인", "/gyeonggi/gunpo/checklist/#office"),
        ("개인정보 처리 기준", "/gyeonggi/gunpo/checklist/#privacy"),
        ("고객 안전 안내", "/gyeonggi/gunpo/checklist/#safety"),
    ]),
    ("홈타이 이용 가이드", "/gyeonggi/gunpo/guide/", [
        ("홈타이란?", "/gyeonggi/gunpo/guide/#what"),
        ("출장마사지와 홈타이 차이", "/gyeonggi/gunpo/guide/#diff"),
        ("군포시 홈타이 이용 기준", "/gyeonggi/gunpo/guide/#standard"),
        ("지역별 이동 기준", "/gyeonggi/gunpo/guide/#move"),
        ("추가 비용 확인 기준", "/gyeonggi/gunpo/guide/#cost"),
        ("처음 이용하는 고객 안내", "/gyeonggi/gunpo/guide/#first"),
    ]),
    ("고객센터", "/gyeonggi/gunpo/support/", [
        ("문의하기", "/gyeonggi/gunpo/support/#contact"),
        ("자주 묻는 질문", "/gyeonggi/gunpo/support/#faq"),
        ("운영 기준", "/gyeonggi/gunpo/support/#policy"),
        ("사이트 소개", "/gyeonggi/gunpo/about/"),
        ("개인정보 처리방침", "/gyeonggi/gunpo/privacy/"),
        ("이용약관", "/gyeonggi/gunpo/terms/"),
    ]),
]
