def get_num_words(text):
    words = text.split()
    return len(words)

def count_unique_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

#def count_unique_words(text):
    #words = text.lower().split()
    #word_count = {}
    #for word in words:
        #word_count[word] = word_count.get(word, 0) + 1
    #return word_count

def sort_char_count(char_count):
    """Sort character count dictionary by frequency in descending order.
    
    Args:
        char_count (dict): Dictionary with characters as keys and counts as values
        
    Returns:
        list: List of (character, count) tuples sorted by count in descending order
    """
    return sorted(char_count.items(), key=lambda x: x[1], reverse=True)

