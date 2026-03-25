# ref: https://regexr.com/    (use this website tool for practising regex)

import re  # buildin regex package in python

text = "The quick brown fox jumps over fox the lazy dog."


# Search for a pattern
match = re.search("brown", text)
if match:
    print("Match found!")
    print("Start index:", match.start())
    print("End index:", match.end())


# Find all occurrences of a pattern
matches = re.findall("the", text, re.IGNORECASE)  # Case-insensitive search
print("Matches:", matches)


# Replace all occurrences of a pattern
new_text = re.sub("fox", "cat", text)
print("New text:", new_text)


# Compile a regex for efficiency (if used multiple times)

pattern = re.compile(r"\b\w+\b")  # Matches whole words
words = pattern.findall(text)
print("Words:", words)
