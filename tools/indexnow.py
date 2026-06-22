#!/usr/bin/env python3
"""IndexNow 일괄 색인 통보 — Bing·Naver·Yandex 등 IndexNow 참여 엔진에 즉시 통보.

사용법:
    python3 tools/indexnow.py              # sitemap.xml 의 모든 URL 통보
    python3 tools/indexnow.py /sanbon-dong/ /guide/   # 특정 경로만 통보 (새 글 올릴 때)

동작:
    - content/site.py 의 BASE_URL, INDEXNOW_KEY 를 읽는다.
    - 키 파일(<KEY>.txt)이 사이트 루트에 배포돼 있어야 한다(build.py 가 생성).
    - 표준 라이브러리만 사용(추가 설치 불필요).

참고:
    - Google 은 IndexNow 미참여. 구글 색인은 tools/google_indexing.py 또는
      Search Console 에서 sitemap 제출/URL 검사를 사용한다.
    - sitemap ping(google.com/ping, bing.com/ping)은 2023년 폐기되어 동작하지 않는다.
"""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE).split("/")[0]

# IndexNow 엔드포인트 — 하나에 보내면 참여 엔진 간 공유되지만,
# 통보 속도를 위해 일반 허브 + 네이버 전용 엔드포인트에 함께 보낸다.
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://searchadvisor.naver.com/indexnow",
    "https://www.bing.com/indexnow",
]


def urls_from_sitemap() -> list[str]:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    xml = open(path, encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", xml)


def normalize(arg: str) -> str:
    if arg.startswith("http"):
        return arg
    return BASE + "/" + arg.lstrip("/")


def main() -> None:
    if not INDEXNOW_KEY:
        sys.exit("INDEXNOW_KEY 가 비어 있습니다. content/site.py 를 확인하세요.")

    args = sys.argv[1:]
    url_list = [normalize(a) for a in args] if args else urls_from_sitemap()
    if not url_list:
        sys.exit("통보할 URL 이 없습니다.")

    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": url_list,
    }
    data = json.dumps(payload).encode("utf-8")
    print(f"IndexNow 통보: {len(url_list)}개 URL (host={HOST})")

    for ep in ENDPOINTS:
        req = urllib.request.Request(
            ep, data=data,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                print(f"  {ep} → {resp.status} {resp.reason}")
        except urllib.error.HTTPError as e:
            # 200/202 외 코드도 정상 처리되는 경우가 있어 본문을 함께 출력
            print(f"  {ep} → {e.code} {e.reason}")
        except Exception as e:  # 네트워크 등
            print(f"  {ep} → 실패: {e}")

    print("완료. (반영까지 수 분~수 시간 소요될 수 있음)")


if __name__ == "__main__":
    main()
