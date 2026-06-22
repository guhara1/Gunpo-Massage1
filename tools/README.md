# 색인(인덱싱) 도구

가장 빠른 색인 통보 구성입니다. 모두 표준 라이브러리 기반(구글 API만 예외).

## 한눈에

| 대상 | 방법 | 즉시성 |
|------|------|--------|
| Bing·Naver·Yandex | **IndexNow** (`tools/indexnow.py`) | 즉시 통보 |
| Google | Search Console sitemap 제출 + URL 검사 / (선택) Indexing API | 빠름 |
| 전체 발견 | `sitemap.xml`, `rss.xml`, `robots.txt` | 자동 크롤 |

> sitemap ping(`google.com/ping`, `bing.com/ping`)은 2023년 폐기되어 동작하지 않습니다.
> 그래서 Bing 계열은 IndexNow, 구글은 Search Console/Indexing API 로 대체합니다.

## 1. 빌드 시 자동 생성물 (`python3 build.py`)

- `sitemap.xml` — 색인 허용 32페이지, `lastmod` 포함
- `rss.xml` — 콘텐츠 발견용 RSS 2.0 피드 (head 에 autodiscovery 링크 포함)
- `robots.txt` — 전 봇 + 네이버 Yeti 허용, sitemap·rss 안내
- `<INDEXNOW_KEY>.txt` — IndexNow 키 파일 (루트 배포)
- 모든 페이지 `<head>` 에 네이버 소유확인 메타 자동 삽입

## 2. IndexNow — Bing·Naver·Yandex 즉시 통보

```bash
python3 build.py                       # 키 파일·사이트맵 생성
# 사이트 배포 후 (키 파일이 루트에 떠 있어야 함)
python3 tools/indexnow.py              # 전체 URL 일괄 통보
python3 tools/indexnow.py /sanbon-dong/ /guide/   # 글 올릴 때마다 해당 URL만
```

키는 `content/site.py` 의 `INDEXNOW_KEY`. 키 파일은 `https://gunpo-massage1.pages.dev/<KEY>.txt` 에서 열려야 합니다.

## 3. Google — 가장 확실한 경로

1. [Search Console](https://search.google.com/search-console) 에 `https://gunpo-massage1.pages.dev/` 속성 추가
   - 소유확인: 네이버처럼 HTML 메타 태그 방식이면 `content/site.py` 의 `GOOGLE_VERIFICATION` 에 값 넣고 재빌드
2. **사이트맵 제출**: `sitemap.xml`
3. 새 글은 **URL 검사 → 색인 요청**

### (선택) Indexing API 자동화

```bash
pip install google-auth requests
export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
python3 tools/google_indexing.py            # 전체
python3 tools/google_indexing.py /guide/    # 특정 URL
```

준비: GCP 에서 Indexing API 사용 설정 → 서비스 계정 JSON → Search Console 속성에 그 계정을 **소유자**로 추가.
(공식 지원은 JobPosting/BroadcastEvent 범위이나, URL_UPDATED 통보 자체는 동작합니다.)

## 4. 네이버 서치어드바이저

1. [서치어드바이저](https://searchadvisor.naver.com) 사이트 등록 (메타 태그 이미 삽입됨)
2. **사이트맵 제출**: `sitemap.xml`, **RSS 제출**: `rss.xml`
3. IndexNow 로 신규 URL 즉시 통보 (위 2번)
