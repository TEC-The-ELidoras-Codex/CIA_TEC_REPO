import os
from pathlib import Path
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import spacy
from collections import Counter
import fitz  # PyMuPDF
import pytesseract
from PIL import Image

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')

UNZIPPED_DIR = Path('UNZIPPED')
SUMMARY_DIR = Path('summaries')
SUMMARY_DIR.mkdir(exist_ok=True)

# Function to summarize text using sumy
def summarize_text(text, sentence_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return ' '.join(str(sentence) for sentence in summary)

# Function to extract key points (keywords/entities)
def extract_key_points(text, top_n=10):
    doc = nlp(text)
    # Extract named entities and noun chunks
    entities = [ent.text for ent in doc.ents]
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    # Combine and count
    all_phrases = entities + noun_chunks
    counter = Counter(all_phrases)
    most_common = counter.most_common(top_n)
    return [phrase for phrase, count in most_common]

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def extract_text_from_tif(tif_path):
    try:
        image = Image.open(tif_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error reading {tif_path}: {e}")
        return ""

# Process all supported files in UNZIPPED and subfolders
for file_path in UNZIPPED_DIR.rglob('*'):
    if file_path.suffix.lower() == '.txt':
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
    elif file_path.suffix.lower() == '.pdf':
        text = extract_text_from_pdf(file_path)
    elif file_path.suffix.lower() == '.tif':
        text = extract_text_from_tif(file_path)
    else:
        continue
    if not text.strip():
        print(f'Skipped (empty): {file_path}')
        continue
    summary = summarize_text(text)
    key_points = extract_key_points(text)
    # Preserve subfolder structure in summaries
    relative_path = file_path.relative_to(UNZIPPED_DIR)
    out_file = SUMMARY_DIR / relative_path.parent / f'{file_path.stem}_summary.txt'
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as out:
        out.write(f'SUMMARY:\n{summary}\n\nKEY POINTS:\n')
        for point in key_points:
            out.write(f'- {point}\n')
    print(f'Processed {file_path}')

print('All files processed. Summaries saved in summaries/.')
