# Build Notes — Ghosting

- Competition: u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72
  ("One Word for Your Wi-Fi", $2, closes 28 Nov 2026 18:35 WIB).
- Gate (RULES.txt): /output/entry.txt must be UTF-8, 1–20 chars, not only
  whitespace. Entry is a single word judged pairwise by an AI judge on
  subject fit, instant humour, truth, freshness, and standalone clarity.
- Word choice: "Ghosting" (8 chars). Candidates considered: "Buffering"
  (most recognisable but the word everyone reaches for), "Flaky" (true but
  flat), "PartTime" (funny, but reads as a schedule joke). "Ghosting" won:
  instantly funny, true (signal vanishes mid-call/game/download, then
  returns like nothing happened), fresher than the obvious picks, and a
  natural Wi-Fi network name.
- main.py v1: plain write of the word to MAKEFUN_OUTPUT_DIR/entry.txt.
  Tested OK (8 chars, one word).
- main.py v2 (revision): added validate() — strips, rejects empty,
  >20 chars, or multi-word input before writing; prints a confirmation
  line. Re-tested OK.
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
  → out/entry.txt contains exactly `Ghosting` (8 chars, 8 bytes, one word).
  Test folder out/ removed afterwards.
- Stdlib only, no network, no secrets. Entry dir was created empty.
