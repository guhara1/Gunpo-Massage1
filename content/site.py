# 사이트 공통 설정
BASE_URL = "https://gunpo-massage1.pages.dev"

BRAND = "바로 GO"
BRAND_MARK = "GO"          # 브랜드 원형 배지 글자
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 군포시 지역 SEO 기준 경로 (지역 확장을 고려한 폴더 구조)
HOME = "/"

# 텔레그램 문의 링크 (웹사이트 제작문의·제휴문의 공용)
TELEGRAM_URL = "https://t.me/googleseolab"

# 상단 메뉴 — 하위 메뉴에는 "출장마사지" 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", [
        ("군포시 메인", "/"),
        ("홈타이 이용 기준", "/#standard"),
        ("대표동 선택 안내", "/#areas"),
        ("예약 전 확인사항", "/#check"),
    ]),
    ("지역별 안내", "/#areas", [
        ("산본동", "/sanbon-dong/"),
        ("금정동", "/geumjeong-dong/"),
        ("군포동", "/gunpo-dong/"),
        ("당정동", "/dangjeong-dong/"),
        ("부곡동", "/bugok-dong/"),
        ("대야미동", "/daeyami-dong/"),
        ("송부동", "/songbu-dong/"),
    ]),
    ("역세권 안내", "/station/", [
        ("역 전체", "/station/"),
        ("산본역", "/station/sanbon-station/"),
        ("금정역", "/station/geumjeong-station/"),
        ("군포역", "/station/gunpo-station/"),
        ("당정역", "/station/dangjeong-station/"),
        ("대야미역", "/station/daeyami-station/"),
        ("수리산역", "/station/surisan-station/"),
        ("반월역 인접 생활권", "/station/banwol-nearby-area/"),
    ]),
    ("생활권 안내", "/area/", [
        ("생활권 전체", "/area/"),
        ("산본중심상가", "/area/sanbon-center/"),
        ("산본신도시", "/area/sanbon-newtown/"),
        ("금정역·군포시청", "/area/geumjeong-cityhall/"),
        ("군포역·당동", "/area/gunpo-station-dang-dong/"),
        ("당정역·한세대", "/area/dangjeong-hansei/"),
        ("부곡·송정지구", "/area/bugok-songjeong/"),
        ("대야미·수리산", "/area/daeyami-surisan/"),
        ("군포첨단산업단지", "/area/gunpo-industrial-complex/"),
        ("수리산역·오금동", "/area/surisan-ogeum/"),
        ("반월·대야미 인접", "/area/banwol-daeyami-nearby/"),
    ]),
    ("예약 안내", "/reservation/", [
        ("예약 가능 지역 확인", "/reservation/#place"),
        ("예약 가능 시간 안내", "/reservation/#hours"),
        ("추가 이동비 안내", "/reservation/#move"),
        ("결제 방식 안내", "/reservation/#payment"),
        ("예약 변경 안내", "/reservation/#change"),
        ("취소 기준 안내", "/reservation/#cancel"),
    ]),
    ("이용 전 확인사항", "/checklist/", [
        ("방문 가능 주소 확인", "/checklist/#address"),
        ("자택 이용 전 확인", "/checklist/#home"),
        ("숙소 이용 전 확인", "/checklist/#stay"),
        ("사무실 인근 이용 전 확인", "/checklist/#office"),
        ("개인정보 처리 기준", "/checklist/#privacy"),
        ("고객 안전 안내", "/checklist/#safety"),
    ]),
    ("홈타이 이용 가이드", "/guide/", [
        ("홈타이란?", "/guide/#what"),
        ("출장마사지와 홈타이 차이", "/guide/#diff"),
        ("군포시 홈타이 이용 기준", "/guide/#standard"),
        ("지역별 이동 기준", "/guide/#move"),
        ("추가 비용 확인 기준", "/guide/#cost"),
        ("처음 이용하는 고객 안내", "/guide/#first"),
    ]),
    ("고객센터", "/support/", [
        ("문의하기", "/support/#contact"),
        ("자주 묻는 질문", "/support/#faq"),
        ("운영 기준", "/support/#policy"),
        ("사이트 소개", "/about/"),
        ("개인정보 처리방침", "/privacy/"),
        ("이용약관", "/terms/"),
    ]),
]
