# 전체 페이지 목록 집계
from . import main, areas, stations, area, info, about

PAGES = [main.PAGE] + areas.PAGES + stations.PAGES + area.PAGES + info.PAGES + [about.PAGE]
