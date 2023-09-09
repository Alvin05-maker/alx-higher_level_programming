#!/usr/bin/python3
def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a list to store the lines of the formatted text
    formatted_lines = []

    # Split the input text into lines using '\n' as the delimiter
    lines = text.split('\n')

    # Process each line
    for line in lines:
        # Initialize a string to store the current line without leading or trailing spaces
        current_line = line.strip()

        # Initialize a flag to indicate whether a special character was found
        special_char_found = False

        # Initialize a string to store the current sentence
        current_sentence = ""

        # Iterate over characters in the line
        for char in current_line:
            # Check for '.', '?', or ':'
            if char in ['.', '?', ':']:
                special_char_found = True
                current_sentence += char
            else:
                # If a special character was found before, add two newlines
                if special_char_found:
                    formatted_lines.append(current_sentence)
                    formatted_lines.append('')
                    current_sentence = ""
                    special_char_found = False
                current_sentence += char

        # Add the last sentence to the formatted lines
        formatted_lines.append(current_sentence)

    # Join the formatted lines with '\n' to create the final text
    formatted_text = '\n'.join(formatted_lines)

    # Print the formatted text
    print(formatted_text)
