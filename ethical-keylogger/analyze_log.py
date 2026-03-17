"""
analyze_log.py
==============
Parses and analyzes the keylogger output log.
Generates keystroke statistics and a frequency report.
"""

import os
import re
from collections import Counter

LOG_FILE = os.path.join("logs", "keylog.txt")


def load_log(path):
    if not os.path.exists(path):
        print(f"[ERROR] Log file not found: {path}")
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_keystrokes(raw):
    """Separate regular characters from special key tags."""
    special_keys = re.findall(r"\[([A-Z_↑↓←→]+)\]", raw)
    clean_text = re.sub(r"\[.*?\]", "", raw)
    return clean_text, special_keys


def char_frequency(text):
    """Return character frequency excluding whitespace and header lines."""
    filtered = [c for c in text if c.strip() and c.isalpha()]
    return Counter(filtered)


def word_frequency(text):
    """Split cleaned text into words and count frequency."""
    words = re.findall(r"[a-zA-Z]{2,}", text)
    return Counter(words)


def print_report(raw):
    clean_text, special_keys = extract_keystrokes(raw)

    total_chars = len(clean_text.replace("\n", "").replace(" ", ""))
    total_special = len(special_keys)
    total_keystrokes = total_chars + total_special

    char_freq = char_frequency(clean_text)
    word_freq = word_frequency(clean_text)
    special_freq = Counter(special_keys)

    print("\n" + "="*55)
    print("   KEYSTROKE ANALYSIS REPORT")
    print("="*55)
    print(f"  Total keystrokes logged  : {total_keystrokes}")
    print(f"  Printable characters     : {total_chars}")
    print(f"  Special key presses      : {total_special}")

    print("\n─── Top 10 Characters ───────────────────────────────")
    for char, count in char_freq.most_common(10):
        bar = "█" * min(count, 40)
        print(f"  '{char}'  {bar} ({count})")

    print("\n─── Top 10 Words Typed ──────────────────────────────")
    for word, count in word_freq.most_common(10):
        print(f"  {word:<20} {count} times")

    print("\n─── Special Key Breakdown ───────────────────────────")
    for key, count in special_freq.most_common():
        print(f"  [{key}]{'.'*(25-len(key))} {count} times")

    print("\n─── Captured Text Preview (first 300 chars) ─────────")
    preview = clean_text.strip()[:300].replace("\n", " ")
    print(f"  {preview}...")
    print("="*55 + "\n")


def main():
    print("\n[*] Loading log file...")
    raw = load_log(LOG_FILE)
    if raw:
        print_report(raw)


if __name__ == "__main__":
    main()
