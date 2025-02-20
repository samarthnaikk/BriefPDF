import re
from helper import *
import time
# Read the transcript and remove timestamps
with open("transcript.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()

# Regex pattern to match timestamps like: hh:mm:ss, h:mm:ss, mm:ss, m:ss
timestamp_pattern = r"^\d{1,2}:\d{2}(?::\d{2})?$"

# Remove timestamp lines
cleaned_text = "".join(line for line in lines if not re.match(timestamp_pattern, line.strip()))

# Save the cleaned transcript
with open("tc.txt", "w", encoding="utf-8") as outfile:
    outfile.write(cleaned_text)

# Define chunk size and split text
len_chars = 5600
chunks = [cleaned_text[i:i+len_chars] for i in range(0, len(cleaned_text), len_chars)]

print("Timestamps removed. Clean transcript saved as 'tc.txt'.")
print(f"Text split into {len(chunks)} chunks of 5600 characters each.")

# Generate summaries and write to notes.txt
summary = ""

with open("notes.txt", "a", encoding="utf-8") as notes_file:
    for i in range(len(chunks)):  # Process first 3 chunks or total chunks if less
        print(f"Completed {i/len(chunks)*100:.2f}%")
        if i%7==0:
            time.sleep(4)
        chunk_summary = response(chunks[i])  # Generate summary
        summary += chunk_summary + "\n"
        notes_file.write(chunk_summary + "\n\n")  # Write summary to file

print("Summary written to 'notes.txt'.")
