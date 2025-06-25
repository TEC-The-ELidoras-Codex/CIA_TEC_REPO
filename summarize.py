import os
from pathlib import Path
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import spacy
from collections import Counter

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

# Process all .txt files in UNZIPPED
for txt_file in UNZIPPED_DIR.glob('*.txt'):
    with open(txt_file, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    summary = summarize_text(text)
    key_points = extract_key_points(text)
    out_file = SUMMARY_DIR / f'{txt_file.stem}_summary.txt'
    with open(out_file, 'w', encoding='utf-8') as out:
        out.write(f'SUMMARY:\n{summary}\n\nKEY POINTS:\n')
        for point in key_points:
            out.write(f'- {point}\n')
    print(f'Processed {txt_file.name}')

print('All files processed. Summaries saved in summaries/.')
