"""
This module is designed to parse html and extract content from it.

The code blocks and functions are implemented assuming that html pages are
well written in html. Some weird cases will be handled. All links that page points
to are printed separately at the end.

Author: Narayan Jat
Date: 11 January 2024
"""


def html_tag_remover(content):
    # Defining flags.
    script_start = False
    style_start = False
    # Defining accumulators.
    previous_char = ''
    start_of_element = ""
    text = ""

    # Code to remove html tags.
    for char in content:
        if char == '<':
            start_of_element += char
        # This elif block is responsible for removing all the html tags.
        elif start_of_element != "":
            if char == '>':
                start_of_element += '>'
                start_of_element = start_of_element.lower()
                # If the ending html tag is encountered.
                if '</' in start_of_element:
                    if start_of_element == '</script>':
                        script_start = False
                    elif start_of_element == '</style>':
                        style_start = False
                    text += " "     # Adding the space after end tag to handle if no new line character is there.
                else:
                    # handling if the start of the starting html tag is encountered.
                    if '<script' in start_of_element:
                        script_start = True
                    elif '<style' in start_of_element:
                        style_start = True
                    elif '<title' in start_of_element:
                        title_start = True
                start_of_element = ""       # Making it empty if end tag is found
            else:
                start_of_element += char
        # Below code block in else deals with extracting main content from the page.
        else:
            if script_start or style_start:
                pass
            else:
                if not (previous_char == ' ' and char == ' '):      # removing extra spaces.
                    if not char == '\t':        # Removing tabs.
                        text += char
        previous_char = char        # Keeping track of previous character.
    return text

