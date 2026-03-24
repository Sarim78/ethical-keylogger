from collections import Counter
import re

LOG_FILE = "log.txt"

def load_log():
    """Read the log file and return its contents as a string."""
    with open(LOG_FILE, "r") as f:
        return f.read()

def count_characters(text):
    """Count how many times each regular character appears."""
    # Strip out anything in [brackets] like [enter], [backspace]
    clean = re.sub(r"\[.*?\]", "", text)
    return Counter(clean)

def count_words(text):
    """Extract and count all words from the log."""
    clean = re.sub(r"\[.*?\]", " ", text)
    words = re.findall(r"[a-zA-Z]+", clean)
    return Counter(words)

# Run the report 
text = load_log()

char_counts = count_characters(text)
word_counts = count_words(text)

print(f"Total characters typed: {sum(char_counts.values())}")
print("\nTop 10 keys:")
for char, count in char_counts.most_common(10):
    print(f"  '{char}' — {count} times")

print("\nTop 10 words:")
for word, count in word_counts.most_common(10):
    print(f"  '{word}' — {count} times")