import numpy as np

file_path = "/home/maia/Documents/School/19-20/PoE/braille-printer/test_story.txt"

def read_text_file(path):
    '''
    Opens and Reads in Text File
    Args: the file path of a text file
    Returns: the string of a file that has been read in
    '''
    open_file = open(path, 'r')
    text = open_file.read()
    print(text)
    print("let's see what this does")
    return text

def break_up_input(text):
    '''
    Breaks the text into space based separations (title, paragraph etc)
    Args: string of text or other input
    Returns: text in an array which is broken up and ready to pass to the translator class
    '''
    for char in text:
        # this is every char in the text sequence
        last_char = ''
        if (char == '\n'):
            print ('yep!')
            print (last_char)
        last_char = char
    return 0
        # print(char)

def set_segment_type(segment):
    '''
    Sets the type of segment being looked at or taken in (paragraph, title, image, table etc)
    Args: Segment of Document
    '''
    return 0

def get_segment_type():
    '''
    Returns the type of segment being looked at or taken in
    Returns: Type (paragraph, title, image, table) etc
    '''
    # TODO: Figure out if this is what we want. Do we need this? Is it a later sprint? Does it make sense to do this? What is our application?

    return 0

break_up_input(read_text_file(file_path))
