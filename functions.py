def title_case(sentence):
    """
    Capitalizes the first letter of each word in a sentence.
    """
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    return sentence.title()

def write_and_read_file(filename, text):
    """
    Writes text to a file and reads it back.
    """
    with open(filename, "w") as f:
        f.write(text)
    
    with open(filename, "r") as f:
        return f.read()