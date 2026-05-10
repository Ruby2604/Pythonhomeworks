import os
import re
from collections import Counter

INPUT_FILE = "sample.txt"
REPORT_FILE = "word_count_report.txt"

# 1. File Input handling
if not os.path.exists(INPUT_FILE):
    content = input("sample.txt not found. Please enter a paragraph to create it: ")
    with open(INPUT_FILE, "w") as f:
        f.write(content)

# 2. Count Word Frequency
with open(INPUT_FILE, "r") as f:
    text = f.read().lower()
    # Remove punctuation using regex and split into words
    words = re.findall(r'\b\w+\b', text)

total_words = len(words)
word_counts = Counter(words)
top_5 = word_counts.most_common(5)

# 3. Console Output
print(f"\nTotal words: {total_words}")
print("Top 5 most common words:")
for word, count in top_5:
    unit = "times" if count != 1 else "time"
    print(f"{word} - {count} {unit}")

# 4. Save to word_count_report.txt
with open(REPORT_FILE, "w") as f:
    f.write("Word Count Report\n")
    f.write(f"Total Words: {total_words}\n")
    f.write("Top 5 Words:\n")
    for word, count in top_5:
        f.write(f"{word} - {count}\n")

print(f"\nReport saved to {REPORT_FILE}")