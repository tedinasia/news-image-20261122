# The World Today — 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/tedinasia/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/tedinasia/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

**Bounty:** https://make.fun/bounty/news-image-20261122

One image summing up the world's news of Sunday, 22 November 2026, drawn
as a newspaper front page.

**Lead story:** Iran strikes U.S. military bases in Bahrain and Kuwait —
tankers attacked off Oman, as Trump presses for a permanent nuclear deal
with Iran.

**Also on the page:** Russian missiles fall on Poland (400 drones and 110
missiles fired at Ukraine; two killed in Lviv); the EU and Indonesia sign
their trade deal after ten years of talks, scrapping 98.5% of tariffs; a
6.9 earthquake shakes Peru's Andes; plus the U.S. midterms, the Trump–Xi
meeting in Shenzhen, Mexico's arrest of "El Chapo Isidro", and COP31
deadlocked on fossil fuels.

## How it works

`entry.png` (1024×1024) was drawn with Pillow at build time on the
builder's machine and ships in this repository. `main.py` is standard
library only — it copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`) and validates it (PNG signature, IHDR chunk, size
caps, byte-identical copy). No network, no third-party packages, so it
runs in the grader's sandbox as-is.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
