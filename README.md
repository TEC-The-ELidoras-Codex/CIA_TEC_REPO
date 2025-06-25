# CIA Document Summarizer

This project processes and summarizes large volumes of CIA document text files. It extracts key points and main ideas from each `.txt` file in the `UNZIPPED` directory, producing concise summaries and keyword lists for easier review.

## Features
- Batch processing of thousands of text files
- Automatic extraction of key points and main ideas
- Outputs aggregated summaries and keywords

## Usage
1. Place all `.txt` files to be analyzed in the `UNZIPPED` directory.
2. Run the summarization script (see `summarize.py`).
3. Summaries and key points will be saved in the `summaries/` directory.

## Requirements
- Python 3.8+
- Install dependencies with `pip install -r requirements.txt`

## Output
- Summaries and key points are saved in `summaries/` (not tracked by git).

## Note
- The original `.txt` and `.tif` files are not tracked by git to save space and protect sensitive data.
