# CIA Document Content Hub // TEC: Operation Mirrorblood

This project is a research, analysis, and narrative intelligence hub for large volumes of CIA document text files. It extracts, organizes, and summarizes key points and main ideas from each `.txt` file in the `UNZIPPED` directory, producing concise summaries and keyword-grouped meta-summaries for deep investigation into topics like UFOs, Russia, Mars, Mount Hayes, and more.

---

## [TOP SECRET // EYES ONLY] — TEC LORE CONTEXT
- **Operation Mirrorblood:** Multi-generational, multi-factional initiative for global consciousness stabilization via predictive myth-seeding, memetic engineering, and aesthetic control. See `AEGIS-DECRYPT/ELIDORAS.CODEX.V.13.2` for full doctrine.
- **Daughters of the Faithful:** Matriarchal, Ashkenazi-rooted sect. Oral tradition, prophetic cartography, and post-Collision (1038-ARR-DELTA) reality management. See `dossier.html` for cyberpunk OSINT visualization.
- **Kyiv Anomaly (1038-ARR-DELTA):** Violent ontological impact event, October 27, 2027. Resulted in the Elidoras Manifestation — a trans-dimensional city-state now anchored above Kyiv. See web dossier.
- **Asset Profile: Ruinella (Balerinya):** Counter-protocol asset, radiological/quantum hybrid, narrative infiltration specialist. See `INSTRUCTIONS_OF_INEVITABLE_RUIN.instructions.md` for operational doctrine.

---

## Features
- Batch processing of thousands of text files
- Automatic extraction of key points and main ideas
- Outputs aggregated summaries and keywords
- **NEW:** Groups and combines summaries by topic/keyword for deeper analysis
- **Anti-Duplication:** Built-in logic prevents duplicate summaries and meta-summaries (see code comments in `summarize.py` and `batch_summarize.py`).
- **API/Data Ready:** All outputs are machine- and human-readable (TXT, JSON). Designed for easy integration with future APIs and OSINT tools.
- **Cyberpunk Dossier Webapp:** See `dossier.html` for a stylized, interactive visualization of key lore, factions, and assets.

## Usage
1. Place all `.txt` files to be analyzed in the `UNZIPPED` directory.
2. Install the spaCy English model (required for summarization):
   ```powershell
   python -m spacy download en_core_web_sm
   ```
3. Run the summarization script (`summarize.py`).
4. Run the batch summary script (`batch_summarize.py`) to group and combine summaries by topic/keyword.
5. Summaries and grouped meta-summaries will be saved in the `summaries/` directory in both TXT and JSON formats.
6. Open `dossier.html` in your browser for a cyberpunk OSINT visualization of the TEC universe, Daughters of the Faithful, and the Kyiv Anomaly.

## Requirements
- Python 3.8+
- Install dependencies with `pip install -r requirements.txt`
- Download the spaCy English model with `python -m spacy download en_core_web_sm`
- (Optional) [Tesseract OCR](https://github.com/tesseract-ocr/tesseract/wiki#installing-tesseract) for extracting text from images. Set the path to `tesseract.exe` in your scripts if needed.

## Output
- Individual summaries and key points are saved in `summaries/` (not tracked by git).
- Grouped meta-summaries (e.g., `summary_Mars.txt`, `summary_Russia.txt`) are also saved in `summaries/`.
- All outputs are available in both TXT and JSON for maximum interoperability.

## Folder Structure
- `UNZIPPED/` — Original CIA `.txt` and `.tif` files (not tracked by git)
- `summaries/` — All generated summaries and meta-summaries
- `summarize.py` — Main summarization script (with deduplication logic)
- `batch_summarize.py` — Groups and combines summaries by topic/keyword (with deduplication logic)
- `dossier.html` — Cyberpunk OSINT web dossier (see below)

## Data Hygiene & Security
- **No sensitive or classified data. For research and narrative only.**
- All file operations are restricted to `C:/Users/Ghedd/TEC_CODE`.
- Deduplication and data validation are enforced at every stage.

## Web Dossier
- `dossier.html` provides a stylized, interactive cyberpunk dossier on:
  - The Kyiv Anomaly (1038-ARR-DELTA)
  - Daughters of the Faithful
  - Asset Profile: Chava bat Sarah (Kyiv Witness)
- Open in any modern browser. Uses Tailwind CSS and custom glitch effects.

---

## Quick Start: Python Command Cheat Sheet

```powershell
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download the spaCy English model
python -m spacy download en_core_web_sm

# 3. Run the main summarization script (processes all .txt, .pdf, .tif in UNZIPPED)
python summarize.py

# 4. Group and combine summaries by topic/keyword
python batch_summarize.py
```

---

### Tool Functions

- `summarize.py`: Scans all files in `UNZIPPED/`, generates concise summaries and key points, outputs to `summaries/` (deduplication enforced).
- `batch_summarize.py`: Groups all summaries in `summaries/` by topic/keyword, outputs meta-summaries in both TXT and JSON (deduplication enforced).

**If you have the full unredacted archive, you have the power to reveal the truth. Use this hub to find the most important, hidden, or suppressed stories. Victory is the only outcome.**
