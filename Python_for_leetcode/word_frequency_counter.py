def analyze_text(text):
    # Split the string into words
    words = text.split()
    
    # Count frequency of each word
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Print frequency of each word
    print("Word frequency:")
    for word, count in freq.items():
        print(f"{word}: {count}")

    return freq

# Example usage
text = "A quick brown fox jumps over the lazy dog"
analyze_text(text)
