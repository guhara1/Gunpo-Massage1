# 메인 페이지 — 군포시 허브. 모든 키워드를 밀어 넣지 않고 대표동·역세권·생활권 상세로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY, HOME
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}{HOME}",
  "logo": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/og-image.png",
    "width": 1200,
    "height": 630
  }},
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "경기도 군포시 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 군포시"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "군포시 출장마사지·홈타이 지역별 예약 안내",
  "url": "{BASE_URL}{HOME}",
  "primaryImageOfPage": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/og-image.png"
  }},
  "inLanguage": "ko-KR"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "군포시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 달라집니다. 지역별 안내에서 산본동, 금정동, 군포동, 당정동, 부곡동, 대야미동, 송부동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "산본역이나 금정역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "주요 역세권은 역 상세 페이지에서 인근 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "산본1동·산본2동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "산본1동·산본2동은 산본동 대표 페이지로, 군포1동·군포2동은 군포동 대표 페이지로 통합해 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "추가 이동비가 있나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "대야미동·송부동·부곡동 일부 외곽 생활권은 시간대에 따라 이동 기준이 달라질 수 있습니다. 예약 시 추가 이동비 여부를 먼저 안내해 드립니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Care · 경기도 군포시 전지역</p>
    <h1>군포시 출장마사지·홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>산본·금정·군포역·당정·대야미 생활권을 확인하고 전화 한 통으로 예약하세요.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/reservation/">예약 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>7개</strong><span>대표 동</span></li>
      <li><strong>7개</strong><span>역세권 안내</span></li>
      <li><strong>10개</strong><span>생활권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="standard">
<h2>군포시에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>군포시 출장마사지를 찾는 분들은 보통 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 군포시는 산본신도시와 산본역 중심 생활권, 금정역과 군포시청 주변 생활권, 군포역과 당동 구도심 생활권, 당정역과 한세대·산업단지 생활권, 대야미와 수리산 인접 생활권이 함께 있는 지역입니다. 그래서 군포 안내는 단순히 "전지역 가능"만 적는 방식보다 대표동과 역세권을 나누어 보여 드리는 구조가 더 정확합니다. 이 페이지는 군포시 전체 구조를 설명하는 허브 역할을 하며, 자세한 내용은 대표동, 역세권, 생활권 안내 페이지에서 확인하실 수 있습니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차로 진행하며, 군포시 홈타이를 처음 이용하는 분도 어렵지 않게 예약하실 수 있도록 각 단계를 분명하게 안내합니다.</p>
</section>

<section id="diff">
<h2>산본·금정·군포역·당정·대야미 생활권 차이</h2>
<p>같은 군포시라도 생활권마다 주거 형태와 이동 기준이 다릅니다. 산본동은 산본신도시와 산본중심상가를 끼고 있어 검색 의도가 가장 넓은 대표 생활권이고, 금정동은 금정역 환승 수요와 군포시청 주변 업무 생활권이 섞여 있습니다. 군포동은 당동과 군포역을 중심으로 한 구도심 주거지이며, 당정동은 당정역·한세대·군포첨단산업단지가 함께 있는 복합 생활권입니다. 대야미동과 송부동, 부곡동은 군포 남서쪽 외곽 주거 생활권으로 차량 이동 기준이 더 중요해집니다. 본인 위치가 어느 생활권에 가까운지 먼저 가늠해 두시면, 예약 가능 시간과 추가 이동비 안내를 한층 빠르게 받으실 수 있습니다.</p>
</section>

<section id="areas">
<h2>대표동별 방문 가능 지역 안내</h2>
<p>군포시 대표동은 산본동, 금정동, 군포동, 당정동, 부곡동, 대야미동, 송부동 일곱 곳입니다. 산본1동·산본2동은 산본동으로, 군포1동·군포2동은 군포동으로 통합해 안내하며, 오금동·수리동·궁내동·광정동은 산본신도시 생활권에서 보조 설명합니다. 아래에서 거주하시거나 머무시는 동을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/sanbon-dong/">산본동</a></li>
<li><a href="/geumjeong-dong/">금정동</a></li>
<li><a href="/gunpo-dong/">군포동</a></li>
<li><a href="/dangjeong-dong/">당정동</a></li>
<li><a href="/bugok-dong/">부곡동</a></li>
<li><a href="/daeyami-dong/">대야미동</a></li>
<li><a href="/songbu-dong/">송부동</a></li>
</ul>
<p>산본동은 군포시에서 출장마사지와 홈타이 검색 수요가 가장 넓은 대표 생활권으로, <a href="/sanbon-dong/">산본동 방문 관리 안내</a>에서 산본역·산본중심상가·산본신도시·수리산역 인접권을 함께 확인할 수 있습니다. 금정역 환승 생활권은 <a href="/geumjeong-dong/">금정동 안내</a>, 당동 구도심은 <a href="/gunpo-dong/">군포동 안내</a>, 산업단지·대학 생활권은 <a href="/dangjeong-dong/">당정동 안내</a>를 참고해 주세요.</p>
</section>

<section id="stations">
<h2>산본역·금정역·군포역·당정역 역세권 안내</h2>
<p>역을 기준으로 위치를 설명하는 것이 편하시다면 역세권 안내가 도움이 됩니다. 산본역, 금정역, 군포역, 당정역, 대야미역, 수리산역과 반월역 인접 생활권을 역마다 한 페이지로 정리했습니다. 금정역은 환승역이어도 노선별 페이지로 나누지 않고 역명 기준 하나의 안내로 운영합니다.</p>
<ul class="card-grid">
<li><a href="/station/sanbon-station/">산본역</a></li>
<li><a href="/station/geumjeong-station/">금정역</a></li>
<li><a href="/station/gunpo-station/">군포역</a></li>
<li><a href="/station/dangjeong-station/">당정역</a></li>
<li><a href="/station/daeyami-station/">대야미역</a></li>
<li><a href="/station/surisan-station/">수리산역</a></li>
<li><a href="/station/banwol-nearby-area/">반월역 인접</a></li>
</ul>
<p>산본역 출장마사지, 금정역 출장마사지, 군포역 출장마사지처럼 역명 기준 검색이 익숙하시다면 <a href="/station/">군포시 역세권 안내</a>에서 전체 역을 한눈에 확인하실 수 있습니다. 생활권 단위가 더 익숙하시면 <a href="/area/">생활권 안내</a>에서 산본중심상가·산본신도시·금정역·군포시청 생활권을 확인해 주세요.</p>
</section>

<section id="check">
<h2>군포시 홈타이 예약 전 확인사항</h2>
<p>군포시 출장마사지·홈타이 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하시는 것이 좋습니다. 산본역과 금정역처럼 접근성이 좋은 지역도 있지만, 대야미동·송부동·부곡동 일부 외곽 생활권은 시간대에 따라 차량 이동 기준이 달라질 수 있습니다. 자세한 절차는 <a href="/reservation/">예약 안내</a>에, 방문 전 준비 기준은 <a href="/checklist/">이용 전 확인사항</a>에 정리되어 있습니다. 군포시 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스이며, 불법·선정적 요청은 어떤 경우에도 진행하지 않습니다.</p>
</section>

<section id="dedup">
<h2>군포시 페이지 중복 방지 운영 기준</h2>
<p>군포 홈타이 사이트를 만들 때 가장 중요한 부분은 번호 동을 무리하게 쪼개지 않는 것입니다. 산본1동·산본2동, 군포1동·군포2동을 각각 개별 페이지로 만들면 페이지 수는 늘지만 본문이 비슷해질 위험이 큽니다. 그래서 산본동·군포동 대표 페이지로 통합하고 각 페이지 안에서 세부 생활권을 설명합니다. 오금동·수리동·궁내동·광정동은 단독 얇은 페이지 대신 산본신도시 생활권과 수리산역 생활권에서 보조 설명하고, 둔대동·속달동은 대야미·수리산 생활권에서, 도마교동은 송부동 페이지에서 다룹니다. 산본동 페이지와 산본역 페이지, 금정동 페이지와 금정역 페이지는 같은 본문을 쓰지 않고 지역 기준과 역세권 기준을 분리합니다. 지역명만 바꿔 같은 글을 반복하지 않는 것이 이 사이트의 기본 원칙입니다.</p>
</section>

<section id="how">
<h2>군포시 출장마사지 사이트 이용 방법</h2>
<p>메인페이지는 군포 전체 안내를 담당하고, 대표동 페이지는 산본동·금정동·군포동·당정동·부곡동·대야미동·송부동 검색을 담당합니다. 역세권 페이지는 산본역·금정역·군포역·당정역·대야미역·수리산역처럼 실제 검색 수요가 생기는 위치를 담당하고, 생활권 페이지는 산본중심상가·산본신도시·금정역·군포시청·군포역·당동·당정역·한세대·대야미·수리산처럼 본인 위치를 더 쉽게 찾도록 보조합니다. 홈타이가 처음이라면 <a href="/guide/">홈타이 이용 가이드</a>에서 출장마사지와 홈타이의 차이부터 확인해 보세요. 어느 페이지를 보셔도 예약 절차와 이용 기준은 동일하니, 본인에게 익숙한 기준으로 보시면 됩니다.</p>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>전화예약</h2>
<p>군포시 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "군포시 출장마사지｜산본·금정·당정·대야미 홈타이 지역 안내",
    "desc": "군포시 출장마사지·홈타이 예약 전 산본역, 금정역, 당정동, 대야미, 군포역 생활권을 확인하세요.",
    "h1": "군포시 출장마사지 · 군포시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
