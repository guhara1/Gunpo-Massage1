#!/usr/bin/env python3
"""Google Indexing API 색인 통보 (선택).

Google 은 IndexNow 에 참여하지 않으므로, 구글에 즉시 통보하려면 이 스크립트를 쓴다.
주의: Indexing API 는 공식적으로 JobPosting/BroadcastEvent 용이며, 일반 페이지에는
보장되지 않는다. 가장 확실한 구글 경로는 Search Console 의 sitemap 제출 + URL 검사다.
(sitemap ping 엔드포인트는 2023년 폐기되어 더 이상 동작하지 않는다.)

사전 준비:
    1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
    2) 서비스 계정 생성 → JSON 키 다운로드
    3) Search Console 속성에 그 서비스 계정 이메일을 "소유자"로 추가
    4) 의존성 설치: pip install google-auth requests

사용법:
    export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
    python3 tools/google_indexing.py                 # sitemap.xml 전체
    python3 tools/google_indexing.py /sanbon-dong/    # 특정 경로 (새 글)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content.site import BASE_URL  # noqa: E402

BASE = BASE_URL.rstrip("/")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def urls_from_sitemap() -> list[str]:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    return re.findall(r"<loc>(.*?)</loc>", open(path, encoding="utf-8").read())


def normalize(arg: str) -> str:
    return arg if arg.startswith("http") else BASE + "/" + arg.lstrip("/")


def main() -> None:
    cred = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred or not os.path.exists(cred):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스 계정 JSON 경로를 지정하세요.")
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성이 필요합니다:  pip install google-auth requests")

    args = sys.argv[1:]
    urls = [normalize(a) for a in args] if args else urls_from_sitemap()

    creds = service_account.Credentials.from_service_account_file(cred, scopes=SCOPES)
    session = AuthorizedSession(creds)

    ok = 0
    for u in urls:
        r = session.post(ENDPOINT, json={"url": u, "type": "URL_UPDATED"})
        status = "OK" if r.status_code == 200 else f"{r.status_code}"
        if r.status_code == 200:
            ok += 1
        print(f"  {status}  {u}")
    print(f"완료: {ok}/{len(urls)} 통보 성공")


if __name__ == "__main__":
    main()
