import re

def process_text(text):
    lines = [line.strip() for line in text if line.strip() != '.']
    phrases = []  # Changed from set to list
    all_phrases = []
    # Function to handle phrase replacements
    def replace_phrase(match):
        quality = match.group(1)  # Capture the Q value
        phrase = match.group(2)
        phrase_with_underscores = phrase.replace(' ', '_')
        phrases.append(phrase_with_underscores)
        all_phrases.append(phrase_with_underscores)  # Changed from add to append
        return f"PLACEHOLDER_{len(phrases)-1}_PLACEHOLDER"
    
    processed_lines = []
    for line in lines:
        # Reset phrases list for each line to maintain correct indexing
        phrases.clear()
        
        # First, replace phrases with placeholders to protect them
        processed = re.sub(r'<phrase_Q=(\d+\.?\d*)>(.*?)</phrase>', replace_phrase, line)
        
        # Replace punctuation with spaces
        processed = re.sub(r'[^\w\s]', ' ', processed)
        
        for i, phrase in enumerate(phrases):
            processed = processed.replace(f"PLACEHOLDER_{i}_PLACEHOLDER", " "+phrase+" ")
        # Replace multiple spaces with a single space
        processed = re.sub(r'\s+', ' ', processed)
        processed = processed.lstrip()
        processed = processed.strip()
        # Restore the original phrases with underscores
        
        
        processed_lines.append(processed)
        
    # Create a set only for the unique phrases output file
    unique_phrases = set(all_phrases)

    return processed_lines, unique_phrases

def read_file(file):
    lines = []
    with open(file, 'r') as file:
        for line in file:
            lines.append(line)
    return lines

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python parse_phrase.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]

    lines = read_file(filename)
    processed_lines, phrase_set = process_text(lines)

    with open("parsed_phrases.txt", 'w') as outfile:
        for line in processed_lines:
            outfile.write(line + '\n')
    with open('phrases.txt', 'w') as outfile:
        for phrase in phrase_set:
            outfile.write(phrase + '\n')
if __name__ == "__main__":
    main()
