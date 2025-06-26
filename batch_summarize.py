import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Ghedd\Tesseract-OCR\tesseract.exe"import os
import re
import json
from collections import defaultdict

# Directory containing individual summaries
dir_path = os.path.join(os.path.dirname(__file__), 'summaries')

# Define keywords/topics to group by (add more as needed)
KEYWORDS = [
    'Russia', 'Soviet', 'KGB', 'Mars', 'Mount Hayes', 'UFO', 'alien', 'extraterrestrial',
    'psychic', 'remote viewing', 'propaganda', 'coverup', 'CIA', 'NSA', 'FBI', 'moon', 'space',
    'Roswell', 'Area 51', 'abduction', 'conspiracy', 'paranormal', 'ESP', 'telepathy', 'mind control'
]

# Compile regex for each keyword (case-insensitive)
keyword_patterns = {kw: re.compile(r'\b' + re.escape(kw) + r'\b', re.IGNORECASE) for kw in KEYWORDS}

groups = defaultdict(list)

# Scan all summary files
for fname in os.listdir(dir_path):
    if fname.endswith('_summary.txt'):
        fpath = os.path.join(dir_path, fname)
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        matched = False
        for kw, pat in keyword_patterns.items():
            if pat.search(content):
                groups[kw].append((fname, content))
                matched = True
        if not matched:
            groups['Other'].append((fname, content))

# Helper: Check for duplicate meta-summary

def is_duplicate_meta(meta_text, meta_path):
    if os.path.exists(meta_path):
        with open(meta_path, 'r', encoding='utf-8', errors='ignore') as f:
            if meta_text.strip() == f.read().strip():
                return True
    return False

# Write grouped meta-summaries
for kw, docs in groups.items():
    out_path = os.path.join(dir_path, f'summary_{kw.replace(" ", "_")}.txt')
    json_path = os.path.join(dir_path, f'summary_{kw.replace(" ", "_")}.json')
    meta_text = f'=== Group: {kw} ===\n\n' + '\n'.join(f'--- {fname} ---\n{content.strip()}\n' for fname, content in docs) + f'\n=== End of {kw} summaries ===\n'
    # Deduplication check
    if is_duplicate_meta(meta_text, out_path):
        print(f"Duplicate meta-summary for {kw}, skipping.")
        continue
    # Write TXT meta-summary
    with open(out_path, 'w', encoding='utf-8') as out:
        out.write(meta_text)
    # Write JSON meta-summary
    with open(json_path, 'w', encoding='utf-8') as jout:
        json.dump({
            'group': kw,
            'summaries': [
                {'file': fname, 'content': content.strip()} for fname, content in docs
            ]
        }, jout, ensure_ascii=False, indent=2)

print('Batch grouping and meta-summaries complete.')
