file_path = "/home/maia/Documents/School/19-20/PoE/braille-printer/test_story.txt"

<<<<<<< HEAD
segments = []
=======
characters = np.array([])
>>>>>>> cd9416e2238f8db29548a49e3f3e1f84dfb9c2d7

def read_text_file(path):
    '''
    Opens and Reads in Text File
    Args: the file path of a text file
    Returns: the string of a file that has been read in
    '''
    open_file = open(path, 'r')
    text = open_file.read()
    print(text)
    return text

def break_up_text_input(text):
    '''
    Breaks the text into space based separations (title, paragraph etc)
    Args: string of text or other input
    Returns: text in an array which is broken up BY SECTION and 
    ready to pass to the translator class
    '''
    global segments
    section = ''
    for char in text:
        # this is every char in the text sequence
        if (char == '\n'):
            segments.append(section)
            section = ''
        else: 
            section += char
    print(segments)
    return segments

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

break_up_text_input(read_text_file(file_path))
