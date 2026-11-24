[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Chapo1245/news-image-20261124-chapo124574/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Chapo1245/news-image-20261124-chapo124574/reward.svg)](https://make.fun/bounty/news-image-20261124)

# The World Today — 24 November 2026

A one-page front page summing up the world's news of Tuesday 24 November
2026: 36 stories across 9 regions — Nvidia brings Jensen Huang back as CEO
and shares soar 31%, CrowdStrike buys Zscaler for $43.9bn, Oxfam warns Gaza
is now a toxic wasteland, NATO vows space defence, the Indonesia factory
fire toll rises to 24, and the UK sanctions Myanmar's generals after the
genocide ruling — plus 30 more stories, a world map and a stat strip.

Built for the [make.fun bounty news-image-20261124](https://make.fun/bounty/news-image-20261124)
($100, top 50). The image is drawn fresh with PIL from news verified
against live sources (Reuters, BBC, AP, ICC, NVIDIA, Oxfam/CEOBS, UKMTO);
see `RESEARCH.md` in the build folder for the story list and sources.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` and refuses to leave a zero-byte or
truncated copy behind. Running it twice writes byte-identical output.

## Entry

- Image: `entry.png` — 1024×1024 PNG, 175,278 bytes, sha256
  `9ef1da4831f5e5492880d5a7c7f5ce444c70049878697b8b12283a86911e16ea`
- Competition: [news-image-20261124](https://make.fun/bounty/news-image-20261124)
- Deadline: 26 November 2026, 00:00 UTC
