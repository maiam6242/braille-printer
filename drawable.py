#This should figure out the position on the page and determine if the content needs to be split over multiple pages

def get_position_on_page():
    '''
    Gets the x, y position that the new braille segment should be on the page (based on the size of the matrix and how much of the page is taken up from the page object)
    Returns: an x and y starting position for the new segment to be written
    '''
    
    return 0

def set_position_on_page():
    '''
    Sets the x, y position that the new braille segment should be on the page based on the size of the matrix and how much of the page is taken up (from the page object)
    Args: size of segment, how much of page is currently being taken up
    '''
    return 0

def should_split():
    '''
    Determines whether or not the segment should be split over multiple pages based on the starting position and size of entire segment
    '''
    return 0