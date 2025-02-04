from collections import defaultdict

def unique_character_count(s):
    """
    Counts the frequency of unique characters in a string.

    Args:
        s (str): The input string.

    Returns:
    
        dict: A dictionary where keys are unique characters and values are their frequencies.
    """
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    return dict(freq)

# Example usage
if __name__ == "__main__":
    # Input string
    input_string = "characteristics"
    # Get the frequency of unique characters
    result = unique_character_count(input_string)
    # Print the result
    print("Input String:", input_string)
    print("Unique Character Frequencies:", result)
