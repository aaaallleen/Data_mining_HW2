def parse_phrases(filename, top_n = 100):
    phrases = []
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                if not line.strip():
                    continue
                try: 
                    score, phrase = line.strip().split('\t')
                except Exception as e:
                    print(f"Error at line {line_num}")

                if not score or not phrase:
                    raise ValueError(f"Invalid entry at line {line}")
                phrases.append(phrase)

            return phrases[-top_n:]
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found")

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python parse.py <filename> [top_n]:")
        sys.exit(1)
    
    filename = sys.argv[1]
    n = 100
    if len(sys.argv) > 2:
        try:
            n = int(sys.argv[2])
        except ValueError:
            print("n must be an int")
            sys.exit(1)
    
    top_words = parse_phrases(filename, n)

    with open("bottom_n.txt", 'w') as outfile:
        for word in top_words:
            outfile.write(word + '\n')

if __name__ == "__main__":
    main()
        
        
